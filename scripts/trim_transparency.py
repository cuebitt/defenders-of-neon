import os
from pathlib import Path
import argparse
from PIL import Image


def trim_transparent_edges(image_path):
    """Trim transparent edges from an image."""
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Ensure image is in RGBA mode for transparency handling
            if img.mode != "RGBA":
                img = img.convert("RGBA")

            # Get bounding box of non-transparent pixels
            bbox = img.getbbox()
            if bbox:
                # Crop to the bounding box
                img = img.crop(bbox)

                # Save back to the original file
                img.save(image_path)
                print(f"Processed: {image_path}")
            else:
                print(f"No transparent edges found: {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")


def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Rename OGG files to snake_case")
    parser.add_argument("path", help="Path to directory containing OGG files to rename")
    args = parser.parse_args()

    # Convert to Path object
    directory = Path(args.path)

    # Check if path exists
    if not directory.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return

    # Process all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Only process regular files
        if os.path.isfile(filepath):
            trim_transparent_edges(filepath)


if __name__ == "__main__":
    main()
