% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef ReferencedImageSequenceTypeSerializer < yardl.binary.RecordSerializer
  methods
    function self = ReferencedImageSequenceTypeSerializer()
      field_serializers{1} = yardl.binary.VectorSerializer(yardl.binary.StringSerializer);
      self@yardl.binary.RecordSerializer('mrd.ReferencedImageSequenceType', field_serializers);
    end

    function write(self, outstream, value)
      arguments
        self
        outstream (1,1) yardl.binary.CodedOutputStream
        value (1,1) mrd.ReferencedImageSequenceType
      end
      self.write_(outstream, value.referenced_sop_instance_uid);
    end

    function value = read(self, instream)
      fields = self.read_(instream);
      value = mrd.ReferencedImageSequenceType(referenced_sop_instance_uid=fields{1});
    end
  end
end