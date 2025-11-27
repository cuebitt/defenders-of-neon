#!/bin/sh

# Trims transparent pixels from each edge of every image in a directory.
# Requires ImageMagick
# Usage: ./trim.sh /path/to/images

set -eu

DIR="${1:-}"

if [ -z "$DIR" ] || [ ! -d "$DIR" ]; then
    echo "Usage: $0 DIRECTORY" >&2
    exit 1
fi

for img in "$DIR"/*; do
    # Skip non-files
    [ -f "$img" ] || continue

    # Use mogrify to modify in-place
    # -trim removes surrounding transparent (or uniform) pixels
    # +repage resets the canvas after trimming
    mogrify -trim +repage "$img"
done
