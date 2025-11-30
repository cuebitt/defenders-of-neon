from pathlib import Path
import os
import casefy
import argparse


def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Rename OGG files to snake_case")
    parser.add_argument("path", help="Path to directory containing OGG files to rename")
    args = parser.parse_args()

    # Convert to Path object
    p = Path(args.path)

    # Check if path exists
    if not p.exists():
        print(f"Error: Directory '{p}' does not exist")
        return

    # Find all OGG files
    files = list(p.glob("*.ogg"))

    # Create new filenames
    newfiles = []
    for file in files:
        fname = file.stem
        ext = file.suffix
        newfiles.append(p / f"{casefy.snakecase(fname)}{ext}")

    # Rename files
    for old, new in zip(files, newfiles):
        os.rename(old.resolve(), new.resolve())


if __name__ == "__main__":
    main()
