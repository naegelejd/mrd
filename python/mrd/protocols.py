# This file was generated by the "yardl" tool. DO NOT EDIT.

# pyright: reportUnusedImport=false

import abc
import collections.abc
import datetime
import typing

import numpy as np
import numpy.typing as npt

from .types import *
from .yardl_types import ProtocolError
from . import yardl_types as yardl

class MrdWriterBase(abc.ABC):
    """Abstract writer for the Mrd protocol."""


    def __init__(self) -> None:
        self._state = 0

    schema = r"""{"protocol":{"name":"Mrd","sequence":[{"name":"header","type":[null,"Mrd.Header"]},{"name":"data","type":{"stream":{"items":"Mrd.StreamItem"}}}]},"types":[{"name":"AccelerationFactorType","fields":[{"name":"kspaceEncodingStep1","type":"uint32"},{"name":"kspaceEncodingStep2","type":"uint32"}]},{"name":"Acquisition","fields":[{"name":"flags","type":"Mrd.AcquisitionFlags"},{"name":"idx","type":"Mrd.EncodingCounters"},{"name":"measurementUid","type":"uint32"},{"name":"scanCounter","type":[null,"uint32"]},{"name":"acquisitionTimeStamp","type":[null,"uint32"]},{"name":"physiologyTimeStamp","type":{"vector":{"items":"uint32"}}},{"name":"channelOrder","type":{"vector":{"items":"uint32"}}},{"name":"discardPre","type":[null,"uint32"]},{"name":"discardPost","type":[null,"uint32"]},{"name":"centerSample","type":[null,"uint32"]},{"name":"encodingSpaceRef","type":[null,"uint32"]},{"name":"sampleTimeUs","type":[null,"float32"]},{"name":"position","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"readDir","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"phaseDir","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"sliceDir","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"patientTablePosition","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"userInt","type":{"vector":{"items":"int32"}}},{"name":"userFloat","type":{"vector":{"items":"float32"}}},{"name":"data","type":"Mrd.AcquisitionData"},{"name":"trajectory","type":"Mrd.TrajectoryData"}]},{"name":"AcquisitionData","type":{"array":{"items":"complexfloat32","dimensions":[{"name":"coils"},{"name":"samples"}]}}},{"name":"AcquisitionFlags","base":"uint64","values":[{"symbol":"firstInEncodeStep1","value":1},{"symbol":"lastInEncodeStep1","value":2},{"symbol":"firstInEncodeStep2","value":4},{"symbol":"lastInEncodeStep2","value":8},{"symbol":"firstInAverage","value":16},{"symbol":"lastInAverage","value":32},{"symbol":"firstInSlice","value":64},{"symbol":"lastInSlice","value":128},{"symbol":"firstInContrast","value":256},{"symbol":"lastInContrast","value":512},{"symbol":"firstInPhase","value":1024},{"symbol":"lastInPhase","value":2048},{"symbol":"firstInRepetition","value":4096},{"symbol":"lastInRepetition","value":8192},{"symbol":"firstInSet","value":16384},{"symbol":"lastInSet","value":32768},{"symbol":"firstInSegment","value":65536},{"symbol":"lastInSegment","value":131072},{"symbol":"isNoiseMeasurement","value":262144},{"symbol":"isParallelCalibration","value":524288},{"symbol":"isParallelCalibrationAndImaging","value":1048576},{"symbol":"isReverse","value":2097152},{"symbol":"isNavigationData","value":4194304},{"symbol":"isPhasecorrData","value":8388608},{"symbol":"lastInMeasurement","value":16777216},{"symbol":"isHpfeedbackData","value":33554432},{"symbol":"isDummyscanData","value":67108864},{"symbol":"isRtfeedbackData","value":134217728},{"symbol":"isSurfacecoilcorrectionscanData","value":268435456},{"symbol":"isPhaseStabilizationReference","value":536870912},{"symbol":"isPhaseStabilization","value":1073741824}]},{"name":"AcquisitionSystemInformationType","fields":[{"name":"systemVendor","type":[null,"string"]},{"name":"systemModel","type":[null,"string"]},{"name":"systemFieldStrengthT","type":[null,"float32"]},{"name":"relativeReceiverNoiseBandwidth","type":[null,"float32"]},{"name":"receiverChannels","type":[null,"uint32"]},{"name":"coilLabel","type":{"vector":{"items":"Mrd.CoilLabelType"}}},{"name":"institutionName","type":[null,"string"]},{"name":"stationName","type":[null,"string"]},{"name":"deviceID","type":[null,"string"]},{"name":"deviceSerialNumber","type":[null,"string"]}]},{"name":"Calibration","values":[{"symbol":"separable2D","value":0},{"symbol":"full3D","value":1},{"symbol":"other","value":2}]},{"name":"CalibrationMode","values":[{"symbol":"embedded","value":0},{"symbol":"interleaved","value":1},{"symbol":"separate","value":2},{"symbol":"external","value":3},{"symbol":"other","value":4}]},{"name":"CoilLabelType","fields":[{"name":"coilNumber","type":"uint32"},{"name":"coilName","type":"string"}]},{"name":"DiffusionDimension","values":[{"symbol":"average","value":0},{"symbol":"contrast","value":1},{"symbol":"phase","value":2},{"symbol":"repetition","value":3},{"symbol":"set","value":4},{"symbol":"segment","value":5},{"symbol":"user0","value":6},{"symbol":"user1","value":7},{"symbol":"user2","value":8},{"symbol":"user3","value":9},{"symbol":"user4","value":10},{"symbol":"user5","value":11},{"symbol":"user6","value":12},{"symbol":"user7","value":13}]},{"name":"DiffusionType","fields":[{"name":"gradientDirection","type":"Mrd.GradientDirectionType"},{"name":"bvalue","type":"float32"}]},{"name":"EncodingCounters","fields":[{"name":"kspaceEncodeStep1","type":[null,"uint32"]},{"name":"kspaceEncodeStep2","type":[null,"uint32"]},{"name":"average","type":[null,"uint32"]},{"name":"slice","type":[null,"uint32"]},{"name":"contrast","type":[null,"uint32"]},{"name":"phase","type":[null,"uint32"]},{"name":"repetition","type":[null,"uint32"]},{"name":"set","type":[null,"uint32"]},{"name":"segment","type":[null,"uint32"]},{"name":"user","type":{"vector":{"items":"uint32"}}}]},{"name":"EncodingLimitsType","fields":[{"name":"kspaceEncodingStep0","type":[null,"Mrd.LimitType"]},{"name":"kspaceEncodingStep1","type":[null,"Mrd.LimitType"]},{"name":"kspaceEncodingStep2","type":[null,"Mrd.LimitType"]},{"name":"average","type":[null,"Mrd.LimitType"]},{"name":"slice","type":[null,"Mrd.LimitType"]},{"name":"contrast","type":[null,"Mrd.LimitType"]},{"name":"phase","type":[null,"Mrd.LimitType"]},{"name":"repetition","type":[null,"Mrd.LimitType"]},{"name":"set","type":[null,"Mrd.LimitType"]},{"name":"segment","type":[null,"Mrd.LimitType"]},{"name":"user0","type":[null,"Mrd.LimitType"]},{"name":"user1","type":[null,"Mrd.LimitType"]},{"name":"user2","type":[null,"Mrd.LimitType"]},{"name":"user3","type":[null,"Mrd.LimitType"]},{"name":"user4","type":[null,"Mrd.LimitType"]},{"name":"user5","type":[null,"Mrd.LimitType"]},{"name":"user6","type":[null,"Mrd.LimitType"]},{"name":"user7","type":[null,"Mrd.LimitType"]}]},{"name":"EncodingSpaceType","fields":[{"name":"matrixSize","type":"Mrd.MatrixSizeType"},{"name":"fieldOfViewMm","type":"Mrd.FieldOfViewMm"}]},{"name":"EncodingType","fields":[{"name":"encodedSpace","type":"Mrd.EncodingSpaceType"},{"name":"reconSpace","type":"Mrd.EncodingSpaceType"},{"name":"encodingLimits","type":"Mrd.EncodingLimitsType"},{"name":"trajectory","type":"Mrd.Trajectory"},{"name":"trajectoryDescription","type":[null,"Mrd.TrajectoryDescriptionType"]},{"name":"parallelImaging","type":[null,"Mrd.ParallelImagingType"]},{"name":"echoTrainLength","type":[null,"int64"]}]},{"name":"ExperimentalConditionsType","fields":[{"name":"h1resonanceFrequencyHz","type":"int64"}]},{"name":"FieldOfViewMm","fields":[{"name":"x","type":"float32"},{"name":"y","type":"float32"},{"name":"z","type":"float32"}]},{"name":"GradientDirectionType","fields":[{"name":"rl","type":"float32"},{"name":"ap","type":"float32"},{"name":"fh","type":"float32"}]},{"name":"Header","fields":[{"name":"version","type":[null,"int64"]},{"name":"subjectInformation","type":[null,"Mrd.SubjectInformationType"]},{"name":"studyInformation","type":[null,"Mrd.StudyInformationType"]},{"name":"measurementInformation","type":[null,"Mrd.MeasurementInformationType"]},{"name":"acquisitionSystemInformation","type":[null,"Mrd.AcquisitionSystemInformationType"]},{"name":"experimentalConditions","type":"Mrd.ExperimentalConditionsType"},{"name":"encoding","type":{"vector":{"items":"Mrd.EncodingType"}}},{"name":"sequenceParameters","type":[null,"Mrd.SequenceParametersType"]},{"name":"userParameters","type":[null,"Mrd.UserParametersType"]},{"name":"waveformInformation","type":{"vector":{"items":"Mrd.WaveformInformationType"}}}]},{"name":"Image","typeParameters":["T"],"fields":[{"name":"flags","type":"Mrd.ImageFlags"},{"name":"measurementUid","type":"uint32"},{"name":"fieldOfView","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"position","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"colDir","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"lineDir","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"sliceDir","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"patientTablePosition","type":{"array":{"items":"float32","dimensions":[{"length":3}]}}},{"name":"average","type":[null,"uint32"]},{"name":"slice","type":[null,"uint32"]},{"name":"contrast","type":[null,"uint32"]},{"name":"phase","type":[null,"uint32"]},{"name":"repetition","type":[null,"uint32"]},{"name":"set","type":[null,"uint32"]},{"name":"acquisitionTimeStamp","type":[null,"uint32"]},{"name":"physiologyTimeStamp","type":{"array":{"items":"uint32","dimensions":[{"length":3}]}}},{"name":"imageType","type":"Mrd.ImageType"},{"name":"imageIndex","type":[null,"uint32"]},{"name":"imageSeriesIndex","type":[null,"uint32"]},{"name":"userInt","type":{"vector":{"items":"int32"}}},{"name":"userFloat","type":{"vector":{"items":"float32"}}},{"name":"data","type":{"name":"Mrd.ImageData","typeArguments":["T"]}},{"name":"meta","type":{"map":{"keys":"string","values":{"vector":{"items":"string"}}}}}]},{"name":"ImageComplexDouble","type":{"name":"Mrd.Image","typeArguments":["complexfloat64"]}},{"name":"ImageComplexFloat","type":{"name":"Mrd.Image","typeArguments":["complexfloat32"]}},{"name":"ImageData","typeParameters":["Y"],"type":{"array":{"items":"Y","dimensions":[{"name":"channel"},{"name":"z"},{"name":"y"},{"name":"x"}]}}},{"name":"ImageDouble","type":{"name":"Mrd.Image","typeArguments":["float64"]}},{"name":"ImageFlags","base":"uint64","values":[{"symbol":"isNavigationData","value":1},{"symbol":"firstInAverage","value":16},{"symbol":"lastInAverage","value":32},{"symbol":"firstInSlice","value":64},{"symbol":"lastInSlice","value":128},{"symbol":"firstInContrast","value":256},{"symbol":"lastInContrast","value":512},{"symbol":"firstInPhase","value":1024},{"symbol":"lastInPhase","value":2048},{"symbol":"firstInRepetition","value":4096},{"symbol":"lastInRepetition","value":8192},{"symbol":"firstInSet","value":16384},{"symbol":"lastInSet","value":32768}]},{"name":"ImageFloat","type":{"name":"Mrd.Image","typeArguments":["float32"]}},{"name":"ImageInt","type":{"name":"Mrd.Image","typeArguments":["int32"]}},{"name":"ImageInt16","type":{"name":"Mrd.Image","typeArguments":["int16"]}},{"name":"ImageType","values":[{"symbol":"magnitude","value":1},{"symbol":"phase","value":2},{"symbol":"real","value":3},{"symbol":"imag","value":4},{"symbol":"complex","value":5}]},{"name":"ImageUint","type":{"name":"Mrd.Image","typeArguments":["uint32"]}},{"name":"ImageUint16","type":{"name":"Mrd.Image","typeArguments":["uint16"]}},{"name":"InterleavingDimension","values":[{"symbol":"phase","value":0},{"symbol":"repetition","value":1},{"symbol":"contrast","value":2},{"symbol":"average","value":3},{"symbol":"other","value":4}]},{"name":"LimitType","fields":[{"name":"minimum","type":"uint32"},{"name":"maximum","type":"uint32"},{"name":"center","type":"uint32"}]},{"name":"MatrixSizeType","fields":[{"name":"x","type":"uint32"},{"name":"y","type":"uint32"},{"name":"z","type":"uint32"}]},{"name":"MeasurementDependencyType","fields":[{"name":"dependencyType","type":"string"},{"name":"measurementID","type":"string"}]},{"name":"MeasurementInformationType","fields":[{"name":"measurementID","type":[null,"string"]},{"name":"seriesDate","type":[null,"date"]},{"name":"seriesTime","type":[null,"time"]},{"name":"patientPosition","type":"Mrd.PatientPosition"},{"name":"relativeTablePosition","type":[null,"Mrd.ThreeDimensionalFloat"]},{"name":"initialSeriesNumber","type":[null,"int64"]},{"name":"protocolName","type":[null,"string"]},{"name":"sequenceName","type":[null,"string"]},{"name":"seriesDescription","type":[null,"string"]},{"name":"measurementDependency","type":{"vector":{"items":"Mrd.MeasurementDependencyType"}}},{"name":"seriesInstanceUIDRoot","type":[null,"string"]},{"name":"frameOfReferenceUID","type":[null,"string"]},{"name":"referencedImageSequence","type":[null,"Mrd.ReferencedImageSequenceType"]}]},{"name":"MultibandSpacingType","fields":[{"name":"dZ","type":{"vector":{"items":"float32"}}}]},{"name":"MultibandType","fields":[{"name":"spacing","type":{"vector":{"items":"Mrd.MultibandSpacingType"}}},{"name":"deltaKz","type":"float32"},{"name":"multibandFactor","type":"uint32"},{"name":"calibration","type":"Mrd.Calibration"},{"name":"calibrationEncoding","type":"uint64"}]},{"name":"ParallelImagingType","fields":[{"name":"accelerationFactor","type":"Mrd.AccelerationFactorType"},{"name":"calibrationMode","type":[null,"Mrd.CalibrationMode"]},{"name":"interleavingDimension","type":[null,"Mrd.InterleavingDimension"]},{"name":"multiband","type":[null,"Mrd.MultibandType"]}]},{"name":"PatientGender","values":[{"symbol":"m","value":0},{"symbol":"f","value":1},{"symbol":"o","value":2}]},{"name":"PatientPosition","values":[{"symbol":"hFP","value":0},{"symbol":"hFS","value":1},{"symbol":"hFDR","value":2},{"symbol":"hFDL","value":3},{"symbol":"fFP","value":4},{"symbol":"fFS","value":5},{"symbol":"fFDR","value":6},{"symbol":"fFDL","value":7}]},{"name":"ReferencedImageSequenceType","fields":[{"name":"referencedSOPInstanceUID","type":{"vector":{"items":"string"}}}]},{"name":"SequenceParametersType","fields":[{"name":"tR","type":{"vector":{"items":"float32"}}},{"name":"tE","type":{"vector":{"items":"float32"}}},{"name":"tI","type":{"vector":{"items":"float32"}}},{"name":"flipAngleDeg","type":{"vector":{"items":"float32"}}},{"name":"sequenceType","type":[null,"string"]},{"name":"echoSpacing","type":{"vector":{"items":"float32"}}},{"name":"diffusionDimension","type":[null,"Mrd.DiffusionDimension"]},{"name":"diffusion","type":{"vector":{"items":"Mrd.DiffusionType"}}},{"name":"diffusionScheme","type":[null,"string"]}]},{"name":"StreamItem","type":[{"tag":"Acquisition","type":"Mrd.Acquisition"},{"tag":"WaveformUint32","type":"Mrd.WaveformUint32"},{"tag":"ImageUint16","type":"Mrd.ImageUint16"},{"tag":"ImageInt16","type":"Mrd.ImageInt16"},{"tag":"ImageUint","type":"Mrd.ImageUint"},{"tag":"ImageInt","type":"Mrd.ImageInt"},{"tag":"ImageFloat","type":"Mrd.ImageFloat"},{"tag":"ImageDouble","type":"Mrd.ImageDouble"},{"tag":"ImageComplexFloat","type":"Mrd.ImageComplexFloat"},{"tag":"ImageComplexDouble","type":"Mrd.ImageComplexDouble"}]},{"name":"StudyInformationType","fields":[{"name":"studyDate","type":[null,"date"]},{"name":"studyTime","type":[null,"time"]},{"name":"studyID","type":[null,"string"]},{"name":"accessionNumber","type":[null,"int64"]},{"name":"referringPhysicianName","type":[null,"string"]},{"name":"studyDescription","type":[null,"string"]},{"name":"studyInstanceUID","type":[null,"string"]},{"name":"bodyPartExamined","type":[null,"string"]}]},{"name":"SubjectInformationType","fields":[{"name":"patientName","type":[null,"string"]},{"name":"patientWeightKg","type":[null,"float32"]},{"name":"patientHeightM","type":[null,"float32"]},{"name":"patientID","type":[null,"string"]},{"name":"patientBirthdate","type":[null,"date"]},{"name":"patientGender","type":[null,"Mrd.PatientGender"]}]},{"name":"ThreeDimensionalFloat","fields":[{"name":"x","type":"float32"},{"name":"y","type":"float32"},{"name":"z","type":"float32"}]},{"name":"Trajectory","values":[{"symbol":"cartesian","value":0},{"symbol":"epi","value":1},{"symbol":"radial","value":2},{"symbol":"goldenangle","value":3},{"symbol":"spiral","value":4},{"symbol":"other","value":5}]},{"name":"TrajectoryData","type":{"array":{"items":"float32","dimensions":[{"name":"basis"},{"name":"samples"}]}}},{"name":"TrajectoryDescriptionType","fields":[{"name":"identifier","type":"string"},{"name":"userParameterLong","type":{"vector":{"items":"Mrd.UserParameterLongType"}}},{"name":"userParameterDouble","type":{"vector":{"items":"Mrd.UserParameterDoubleType"}}},{"name":"userParameterString","type":{"vector":{"items":"Mrd.UserParameterStringType"}}},{"name":"comment","type":[null,"string"]}]},{"name":"UserParameterBase64Type","fields":[{"name":"name","type":"string"},{"name":"value","type":"string"}]},{"name":"UserParameterDoubleType","fields":[{"name":"name","type":"string"},{"name":"value","type":"float64"}]},{"name":"UserParameterLongType","fields":[{"name":"name","type":"string"},{"name":"value","type":"int64"}]},{"name":"UserParameterStringType","fields":[{"name":"name","type":"string"},{"name":"value","type":"string"}]},{"name":"UserParametersType","fields":[{"name":"userParameterLong","type":{"vector":{"items":"Mrd.UserParameterLongType"}}},{"name":"userParameterDouble","type":{"vector":{"items":"Mrd.UserParameterDoubleType"}}},{"name":"userParameterString","type":{"vector":{"items":"Mrd.UserParameterStringType"}}},{"name":"userParameterBase64","type":{"vector":{"items":"Mrd.UserParameterBase64Type"}}}]},{"name":"Waveform","typeParameters":["T"],"fields":[{"name":"flags","type":"uint64"},{"name":"measurementUid","type":"uint32"},{"name":"scanCounter","type":"uint32"},{"name":"timeStamp","type":"uint32"},{"name":"sampleTimeUs","type":"float32"},{"name":"waveformId","type":"uint32"},{"name":"data","type":{"name":"Mrd.WaveformSamples","typeArguments":["T"]}}]},{"name":"WaveformInformationType","fields":[{"name":"waveformName","type":"string"},{"name":"waveformType","type":"Mrd.WaveformType"},{"name":"userParameters","type":"Mrd.UserParametersType"}]},{"name":"WaveformSamples","typeParameters":["T"],"type":{"array":{"items":"T","dimensions":[{"name":"channels"},{"name":"samples"}]}}},{"name":"WaveformType","values":[{"symbol":"ecg","value":0},{"symbol":"pulse","value":1},{"symbol":"respiratory","value":2},{"symbol":"trigger","value":3},{"symbol":"gradientwaveform","value":4},{"symbol":"other","value":5}]},{"name":"WaveformUint32","type":{"name":"Mrd.Waveform","typeArguments":["uint32"]}}]}"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type: typing.Optional[type[BaseException]], exc: typing.Optional[BaseException], traceback: object) -> None:
        if exc is None and self._state == 3:
            try:
                self._end_stream()
                return
            finally:
                self.close()
        self.close()
        if exc is None and self._state != 4:
            expected_method = self._state_to_method_name((self._state + 1) & ~1)
            raise ProtocolError(f"Protocol writer closed before all steps were called. Expected to call to '{expected_method}'.")

    def write_header(self, value: typing.Optional[Header]) -> None:
        """Ordinal 0"""

        if self._state != 0:
            self._raise_unexpected_state(0)

        self._write_header(value)
        self._state = 2

    def write_data(self, value: collections.abc.Iterable[StreamItem]) -> None:
        """Ordinal 1"""

        if self._state & ~1 != 2:
            self._raise_unexpected_state(2)

        self._write_data(value)
        self._state = 3

    @abc.abstractmethod
    def _write_header(self, value: typing.Optional[Header]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def _write_data(self, value: collections.abc.Iterable[StreamItem]) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def close(self) -> None:
        pass

    @abc.abstractmethod
    def _end_stream(self) -> None:
        pass

    def _raise_unexpected_state(self, actual: int) -> None:
        expected_method = self._state_to_method_name(self._state)
        actual_method = self._state_to_method_name(actual)
        raise ProtocolError(f"Expected to call to '{expected_method}' but received call to '{actual_method}'.")

    def _state_to_method_name(self, state: int) -> str:
        if state == 0:
            return 'write_header'
        if state == 2:
            return 'write_data'
        return "<unknown>"

class MrdReaderBase(abc.ABC):
    """Abstract reader for the Mrd protocol."""


    def __init__(self) -> None:
        self._state = 0

    schema = MrdWriterBase.schema

    def __enter__(self):
        return self

    def __exit__(self, exc_type: typing.Optional[type[BaseException]], exc: typing.Optional[BaseException], traceback: object) -> None:
        self.close()
        if exc is None and self._state != 4:
            if self._state % 2 == 1:
                previous_method = self._state_to_method_name(self._state - 1)
                raise ProtocolError(f"Protocol reader closed before all data was consumed. The iterable returned by '{previous_method}' was not fully consumed.")
            else:
                expected_method = self._state_to_method_name(self._state)
                raise ProtocolError(f"Protocol reader closed before all data was consumed. Expected call to '{expected_method}'.")
            	

    @abc.abstractmethod
    def close(self) -> None:
        raise NotImplementedError()

    def read_header(self) -> typing.Optional[Header]:
        """Ordinal 0"""

        if self._state != 0:
            self._raise_unexpected_state(0)

        value = self._read_header()
        self._state = 2
        return value

    def read_data(self) -> collections.abc.Iterable[StreamItem]:
        """Ordinal 1"""

        if self._state != 2:
            self._raise_unexpected_state(2)

        value = self._read_data()
        self._state = 3
        return self._wrap_iterable(value, 4)

    def copy_to(self, writer: MrdWriterBase) -> None:
        writer.write_header(self.read_header())
        writer.write_data(self.read_data())

    @abc.abstractmethod
    def _read_header(self) -> typing.Optional[Header]:
        raise NotImplementedError()

    @abc.abstractmethod
    def _read_data(self) -> collections.abc.Iterable[StreamItem]:
        raise NotImplementedError()

    T = typing.TypeVar('T')
    def _wrap_iterable(self, iterable: collections.abc.Iterable[T], final_state: int) -> collections.abc.Iterable[T]:
        yield from iterable
        self._state = final_state

    def _raise_unexpected_state(self, actual: int) -> None:
        actual_method = self._state_to_method_name(actual)
        if self._state % 2 == 1:
            previous_method = self._state_to_method_name(self._state - 1)
            raise ProtocolError(f"Received call to '{actual_method}' but the iterable returned by '{previous_method}' was not fully consumed.")
        else:
            expected_method = self._state_to_method_name(self._state)
            raise ProtocolError(f"Expected to call to '{expected_method}' but received call to '{actual_method}'.")
        	
    def _state_to_method_name(self, state: int) -> str:
        if state == 0:
            return 'read_header'
        if state == 2:
            return 'read_data'
        return "<unknown>"
