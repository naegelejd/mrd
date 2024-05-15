% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef MultibandSpacingType < handle
  properties
    d_z
  end

  methods
    function self = MultibandSpacingType(kwargs)
      arguments
        kwargs.d_z = single.empty();
      end
      self.d_z = kwargs.d_z;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.MultibandSpacingType") && ...
        isequal(self.d_z, other.d_z);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.MultibandSpacingType();
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