#!/bin/bash
set -euo pipefail

usage()
{
  cat << EOF

Builds the mrd conda package.

Usage: $0
EOF
}

output_path="$(dirname "$0")/build_pkg"

# Build up channel directives
channels=(
  conda-forge
  ismrmrd
)

channel_directives=$(printf -- "-c %s " "${channels[@]}")

mkdir -p "$output_path"
bash -c "conda mambabuild --no-anaconda-upload --output-folder $output_path $channel_directives $(dirname "$0")"
