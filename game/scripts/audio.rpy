init python:
  music_tracks = {
    "peril_theme": {
      "title": "Peril Theme (Dubstep - Imminent Danger)",
      "artist": "AntipodeanWriter",
      "file": "audio/bgm/dubstep-imminent-danger-13039.ogg"
    },
    "phase_theme": {
      "title": "Phase Theme (Crimson Shadows of the Electric Night)",
      "artist": "susan-lu4esm",
      "file": "audio/bgm/crimson-shadows-of-the-electric-night-433424.ogg"
    },
    "arcade_theme": {
      "title": "Arcade Theme (Retro Arcade Game Music)",
      "artist": "MFCC",
      "file": "audio/bgm/retro-arcade-game-music-297305.ogg"
    },
    "mall_theme": {
      "title": "Mall Theme (The Ghost of Shepherd's Pie - GBML)",
      "artist": "GeoffreyBurch",
      "file": "audio/bgm/the-ghost-of-shepardx27s-pie-glbml-112816.ogg"
    },
    "limiter_theme": {
      "title": "Limiter Theme",
      "artist": "nickpanek",
      "file": "audio/bgm/epic-sci-fi-villain-theme-for-cinematic-projects-224750.ogg"
    }
  }

  for track_id, track_data in music_tracks.items():
      setattr(audio, track_id, track_data["file"])  # add to audio object

define audio.phase_instrument_sfx = "audio/sfx/electric-guitar-metal-riff-107087.ogg"
