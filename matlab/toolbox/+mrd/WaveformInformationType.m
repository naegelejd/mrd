% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef WaveformInformationType < handle
  properties
    waveform_name
    waveform_type
    user_parameters
  end

  methods
    function self = WaveformInformationType(kwargs)
      arguments
        kwargs.waveform_name = "";
        kwargs.waveform_type = mrd.WaveformType.ECG;
        kwargs.user_parameters = mrd.UserParametersType();
      end
      self.waveform_name = kwargs.waveform_name;
      self.waveform_type = kwargs.waveform_type;
      self.user_parameters = kwargs.user_parameters;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.WaveformInformationType") && ...
        isequal(self.waveform_name, other.waveform_name) && ...
        isequal(self.waveform_type, other.waveform_type) && ...
        isequal(self.user_parameters, other.user_parameters);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.WaveformInformationType();
      if nargin == 0
        z = elem;
        return;
      end
      sz = [varargin{:}];
      if isscalar(sz)
        sz = [sz, sz];
      end
      z = reshape(repelem(elem, prod(sz)), sz);
    end
  end
end
