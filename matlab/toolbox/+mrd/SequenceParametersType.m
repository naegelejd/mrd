% This file was generated by the "yardl" tool. DO NOT EDIT.

classdef SequenceParametersType < handle
  properties
    t_r
    t_e
    t_i
    flip_angle_deg
    sequence_type
    echo_spacing
    diffusion_dimension
    diffusion
    diffusion_scheme
  end

  methods
    function self = SequenceParametersType(kwargs)
      arguments
        kwargs.t_r = single.empty();
        kwargs.t_e = single.empty();
        kwargs.t_i = single.empty();
        kwargs.flip_angle_deg = single.empty();
        kwargs.sequence_type = yardl.None;
        kwargs.echo_spacing = single.empty();
        kwargs.diffusion_dimension = yardl.None;
        kwargs.diffusion = mrd.DiffusionType.empty();
        kwargs.diffusion_scheme = yardl.None;
      end
      self.t_r = kwargs.t_r;
      self.t_e = kwargs.t_e;
      self.t_i = kwargs.t_i;
      self.flip_angle_deg = kwargs.flip_angle_deg;
      self.sequence_type = kwargs.sequence_type;
      self.echo_spacing = kwargs.echo_spacing;
      self.diffusion_dimension = kwargs.diffusion_dimension;
      self.diffusion = kwargs.diffusion;
      self.diffusion_scheme = kwargs.diffusion_scheme;
    end

    function res = eq(self, other)
      res = ...
        isa(other, "mrd.SequenceParametersType") && ...
        isequal(self.t_r, other.t_r) && ...
        isequal(self.t_e, other.t_e) && ...
        isequal(self.t_i, other.t_i) && ...
        isequal(self.flip_angle_deg, other.flip_angle_deg) && ...
        isequal(self.sequence_type, other.sequence_type) && ...
        isequal(self.echo_spacing, other.echo_spacing) && ...
        isequal(self.diffusion_dimension, other.diffusion_dimension) && ...
        isequal(self.diffusion, other.diffusion) && ...
        isequal(self.diffusion_scheme, other.diffusion_scheme);
    end

    function res = ne(self, other)
      res = ~self.eq(other);
    end
  end

  methods (Static)
    function z = zeros(varargin)
      elem = mrd.SequenceParametersType();
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
