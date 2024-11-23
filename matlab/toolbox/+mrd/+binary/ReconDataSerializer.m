% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef ReconDataSerializer < yardl.binary.RecordSerializer
  methods
    function self = ReconDataSerializer()
      field_serializers{1} = yardl.binary.VectorSerializer(mrd.binary.ReconAssemblySerializer());
      self@yardl.binary.RecordSerializer('mrd.ReconData', field_serializers);
    end

    function write(self, outstream, value)
      arguments
        self
        outstream (1,1) yardl.binary.CodedOutputStream
        value (1,1) mrd.ReconData
      end
      self.write_(outstream, value.buffers);
    end

    function value = read(self, instream)
      fields = self.read_(instream);
      value = mrd.ReconData(buffers=fields{1});
    end
  end
end