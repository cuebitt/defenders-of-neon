init python:
  music_tracks = {
    "peril_theme": {
      "title": "Peril Theme (Dubstep - Imminent Danger)",
      "artist": "AntipodeanWriter",
      "file": "audio/bgm/dubstep-imminent-danger-13039.mp3"
    },
    "phase_theme": {
      "title": "Phase Theme (Crimson Shadows of the Electric Night)",
      "artist": "susan-lu4esm",
      "file": "audio/bgm/crimson-shadows-of-the-electric-night-433424.mp3"
    }
  }

  for track_id, track_data in music_tracks.items():
      setattr(audio, track_id, track_data["file"])  # add to audio object

define audio.phase_instrument_sfx = "audio/sfx/electric-guitar-metal-riff-107087.mp3"
