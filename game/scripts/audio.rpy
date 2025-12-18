init python:
    import json

    # load music.json
    with renpy.open_file("data/music.json", encoding="utf-8") as f:
        music_tracks = json.load(f)

    # Extract and sort music tracks by track title
    music_tracks = {key: music_tracks[key] for key in sorted(music_tracks, key=str.lower)}

    # Create a music room
    mr = MusicRoom(fadeout=1.0)

    # Add music tracks to music room and audio object
    for track_id, track_data in music_tracks.items():
        mr.add(track_data["file"])                    # add to music room
        setattr(audio, track_id, track_data["file"])  # add to audio object

    # load sfx.json
    with renpy.open_file("data/sfx.json", encoding="utf-8") as f:
        sfx_data = json.load(f)
    
    # Add sound effects to audio object
    for sfx_id, sfx_data in sfx_data.items():
        setattr(audio, sfx_id, sfx_data["file"])  # add to audio object

