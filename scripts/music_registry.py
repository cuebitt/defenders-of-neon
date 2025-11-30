from pathlib import Path
import json
import argparse


def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(description="Generate music registry object")
    parser.add_argument("path", help="Path to directory containing OGG files")
    parser.add_argument("game", help="Path to game directory")
    args = parser.parse_args()

    # Convert to Path object
    p = Path(args.path)
    g = Path(args.game)

    # Check if path exists
    if not p.exists():
        print(f"Error: Directory '{p}' does not exist")
        return

    if not g.exists():
        print(f"Error: Directory '{g}' does not exist")
        return

    # Find all OGG files
    files = list(p.glob("*.ogg"))

    abs_g = g.parent.resolve()
    output = {}
    for file in files:
        abs_p = file.resolve()

        output[abs_p.stem] = {
            "title": "",
            "artist": "KOMODOMODE",
            "file": str(abs_p).replace(str(abs_g) + "/", ""),
            "album_art": "",
        }
        
    
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
