#include "mrd/binary/protocols.h"
#include "shepp_logan_phantom.h"

#include <iostream>
#include <random>
#include <xtensor-fftw/basic.hpp>
#include <xtensor-fftw/helper.hpp>
#include <xtensor/xio.hpp>
#include <xtensor/xrandom.hpp>
#include <xtensor/xview.hpp>

using namespace mrd;

xt::xtensor<std::complex<float>, 4> fftshift(xt::xtensor<std::complex<float>, 4> x) {
  return xt::roll(xt::roll(x, x.shape(3) / 2, 3), x.shape(2) / 2, 2);
}

template <std::size_t N>
xt::xtensor<std::complex<float>, N> generate_noise(std::array<size_t, N> shape, float sigma, float mean = 0.0) {
  using namespace std::complex_literals;
  return xt::random::randn(shape, mean, sigma) + 1.0i * xt::random::randn(shape, mean, sigma);
}

mrd::ImageData<std::complex<float>> generate_coil_kspace(size_t matrix, size_t ncoils, uint32_t oversampling) {
  xt::xtensor<std::complex<float>, 4> phan = shepp_logan_phantom(matrix);
  xt::xtensor<std::complex<float>, 4> coils = generate_birdcage_sensitivities(matrix, ncoils, 1.5);
  coils = phan * coils;

  if (oversampling > 1) {
    std::array<size_t, 4> padded_shape = coils.shape();
    padded_shape[3] *= oversampling;
    xt::xtensor<std::complex<float>, 4> padded = xt::zeros<std::complex<float>>(padded_shape);
    auto pad = (oversampling - 1) * matrix / 2;
    xt::view(padded, xt::all(), xt::all(), xt::all(), xt::range(pad, pad + matrix)) = coils;
    coils = padded;
  }

  coils = fftshift(coils);
  for (unsigned int c = 0; c < ncoils; c++) {
    auto tmp1 = xt::fftw::fft2(xt::xarray<std::complex<float>>(xt::view(coils, c, 0, xt::all(), xt::all())));
    tmp1 /= std::sqrt(1.0f * tmp1.size());
    xt::view(coils, c, 0, xt::all(), xt::all()) = tmp1;
  }
  return fftshift(coils);
}

int main(int argc, char** argv) {
  uint32_t matrix = 256;
  uint32_t ncoils = 8;
  uint32_t repetitions = 1;
  uint32_t oversampling = 2;
  float noise_sigma = 0.05;
  std::string filename;

  auto print_usage = [&]() {
    std::cerr << "Usage: " << argv[0] << std::endl;
    std::cerr << "  -o|--output       <output stream>   (default: stdout)" << std::endl;
    std::cerr << "  -c|--coils        <number of coils> (default: " << ncoils << ")" << std::endl;
    std::cerr << "  -m|--matrix       <matrix size>     (default: " << matrix << ")" << std::endl;
    std::cerr << "  -r|--repetitions  <repetitions>     (default: " << repetitions << ")" << std::endl;
    std::cerr << "  -s|--oversampling <oversampling>    (default: " << oversampling << ")" << std::endl;
    std::cerr << "  -n|--noise-sigma  <noise level>     (default: " << noise_sigma << ")" << std::endl;
    std::cerr << "  -h|--help" << std::endl;
  };

  std::vector<std::string> args(argv, argv + argc);
  auto current_arg = args.begin() + 1;
  while (current_arg != args.end()) {
    if (*current_arg == "--help" || *current_arg == "-h") {
      print_usage();
      return 0;
    } else if (*current_arg == "--output" || *current_arg == "-o") {
      current_arg++;
      if (current_arg == args.end()) {
        std::cerr << "Missing output file" << std::endl;
        print_usage();
        return 1;
      }
      filename = *current_arg;
      current_arg++;
    } else if (*current_arg == "--coils" || *current_arg == "-c") {
      current_arg++;
      if (current_arg == args.end()) {
        std::cerr << "Missing number of coils" << std::endl;
        print_usage();
        return 1;
      }
      ncoils = std::stoi(*current_arg);
      current_arg++;
    } else if (*current_arg == "--matrix" || *current_arg == "-m") {
      current_arg++;
      if (current_arg == args.end()) {
        std::cerr << "Missing matrix size" << std::endl;
        print_usage();
        return 1;
      }
      matrix = std::stoi(*current_arg);
      current_arg++;
    } else if (*current_arg == "--repetitions" || *current_arg == "-r") {
      current_arg++;
      if (current_arg == args.end()) {
        std::cerr << "Missing number of frames" << std::endl;
        print_usage();
        return 1;
      }
      repetitions = std::stoi(*current_arg);
      current_arg++;
    } else if (*current_arg == "--oversampling" || *current_arg == "-s") {
      current_arg++;
      if (current_arg == args.end()) {
        std::cerr << "Missing oversampling factor" << std::endl;
        print_usage();
        return 1;
      }
      oversampling = std::stoi(*current_arg);
      current_arg++;
    } else if (*current_arg == "--noise-sigma" || *current_arg == "-n") {
      current_arg++;
      if (current_arg == args.end()) {
        std::cerr << "Missing noise sigma" << std::endl;
        print_usage();
        return 1;
      }
      noise_sigma = std::stof(*current_arg);
      current_arg++;
    } else {
      std::cerr << "Unknown argument: " << *current_arg << std::endl;
      print_usage();
      return 1;
    }
  }

  std::unique_ptr<MrdWriterBase> w;

  if (filename.empty()) {
    w = std::make_unique<mrd::binary::MrdWriter>(std::cout);
  } else {
    w = std::make_unique<mrd::binary::MrdWriter>(filename);
  }

  // Parameters
  auto nx = matrix;
  auto ny = matrix;
  auto nkx = oversampling * matrix;
  auto nky = ny;
  float fov = 300;
  float slice_thickness = 5;

  Header h;
  SubjectInformationType subject;
  subject.patient_id = "1234BGVF";
  subject.patient_name = "John Doe";
  h.subject_information = subject;

  ExperimentalConditionsType exp;
  exp.h1resonance_frequency_hz = 128000000;
  h.experimental_conditions = exp;

  AcquisitionSystemInformationType sys;
  sys.receiver_channels = ncoils;
  h.acquisition_system_information = sys;

  EncodingSpaceType e;
  e.matrix_size = {nkx, nky, 1};
  e.field_of_view_mm = {oversampling * fov, fov, slice_thickness};

  EncodingSpaceType r;
  r.matrix_size = {nx, ny, 1};
  r.field_of_view_mm = {fov, fov, slice_thickness};

  LimitType limits1;
  limits1.minimum = 0;
  limits1.center = std::round(ny / 2.0);
  limits1.maximum = ny - 1;

  LimitType limits_rep;
  limits_rep.minimum = 0;
  limits_rep.center = std::round(repetitions / 2.0);
  limits_rep.maximum = repetitions - 1;

  EncodingLimitsType limits;
  limits.kspace_encoding_step_1 = limits1;
  limits.repetition = limits_rep;

  EncodingType enc;
  enc.trajectory = Trajectory::kCartesian;
  enc.encoded_space = e;
  enc.recon_space = r;
  enc.encoding_limits = limits;
  h.encoding.push_back(enc);

  w->WriteHeader(h);

  // We will reuse this Acquisition object
  Acquisition acq;

  std::array<size_t, 2> acq_shape = {ncoils, nkx};
  acq.data.resize(acq_shape);
  for (unsigned int c = 0; c < ncoils; c++) {
    acq.head.channel_order.push_back(c);
  }
  acq.head.center_sample = std::round(nkx / 2.0);
  acq.head.read_dir[0] = 1.0;
  acq.head.phase_dir[1] = 1.0;
  acq.head.slice_dir[1] = 1.0;

  uint32_t scan_counter = 0;

  // Write a few noise scans
  for (unsigned int n = 0; n < 32; n++) {
    std::array<size_t, 2> noise_shape = {ncoils, nkx};
    auto noise = generate_noise(noise_shape, noise_sigma);
    acq.head.scan_counter = scan_counter++;
    acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kIsNoiseMeasurement);
    xt::view(acq.data, xt::all(), xt::all()) = noise;
    w->WriteData(acq);
  }

  // Generate phantom k-space
  auto phan = generate_coil_kspace(matrix, ncoils, oversampling);

  for (unsigned int r = 0; r < repetitions; r++) {
    auto noise = generate_noise(phan.shape(), noise_sigma);
    auto kspace = xt::xtensor<std::complex<float>, 4>(phan) + noise;

    for (size_t line = 0; line < nky; line++) {
      acq.head.flags.Clear();
      acq.head.scan_counter = scan_counter++;

      if (line == 0) {
        acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kFirstInEncodeStep1);
        acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kFirstInSlice);
        acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kFirstInRepetition);
      }
      if (line == matrix - 1) {
        acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kLastInEncodeStep1);
        acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kLastInSlice);
        acq.head.flags |= static_cast<uint64_t>(AcquisitionFlags::kLastInRepetition);
      }
      acq.head.idx.kspace_encode_step_1 = line;
      acq.head.idx.kspace_encode_step_2 = 0;
      acq.head.idx.slice = 0;
      acq.head.idx.repetition = r;
      acq.data = xt::view(kspace, xt::all(), 0, line, xt::all());
      w->WriteData(acq);
    }
  }
  w->EndData();
}
