init python:
  music_tracks = {
    "defenders_theme_distorted": {
      "title": "Defenders of Neon Theme (Distorted) (Band Practice)",
      "artist": "freesound_community",
      "file": "audio/bgm/band-practice-67276.ogg",
      "album_art": ""
    },
    "peril_theme": {
      "title": "Peril Theme (Dubstep - Imminent Danger)",
      "artist": "AntipodeanWriter",
      "file": "audio/bgm/dubstep-imminent-danger-13039.ogg",
      "album_art": ""
    },
    "phase_theme": {
      "title": "Phase Theme (Crimson Shadows of the Electric Night)",
      "artist": "susan-lu4esm",
      "file": "audio/bgm/crimson-shadows-of-the-electric-night-433424.ogg",
      "album_art": ""
    },
    "arcade_theme": {
      "title": "Arcade Theme (Retro Arcade Game Music)",
      "artist": "MFCC",
      "file": "audio/bgm/retro-arcade-game-music-297305.ogg",
      "album_art": ""
    },
    "mall_theme": {
      "title": "Mall Theme (The Ghost of Shepherd's Pie - GBML)",
      "artist": "GeoffreyBurch",
      "file": "audio/bgm/the-ghost-of-shepardx27s-pie-glbml-112816.ogg",
      "album_art": ""
    },
    "limiter_theme": {
      "title": "Limiter Theme (Epic Sci-Fi Villain Theme for Cinematic Projects)",
      "artist": "nickpanek",
      "file": "audio/bgm/epic-sci-fi-villain-theme-for-cinematic-projects-224750.ogg",
      "album_art": ""
    }
  }

  music_tracks = {key: music_tracks[key] for key in sorted(music_tracks, key=str.lower)}

    # Create a music room
  mr = MusicRoom(fadeout=1.0)

  # Add music tracks to music room and audio object
  for track_id, track_data in music_tracks.items():
    mr.add(track_data["file"])                    # add to music room
    setattr(audio, track_id, track_data["file"])  # add to audio object

# SFX
define audio.phase_instrument_sfx = "audio/sfx/electric-guitar-metal-riff-107087.ogg"
define audio.inhale_exhale_sfx = "audio/sfx/inhale-exhale-230173.ogg"
define audio.siren_sfx = "audio/sfx/air-raid-siren-sound-effect-241383.ogg"
define audio.crow_caw_sfx = "audio/sfx/creepy-crow-caw-322991.ogg"
define audio.record_scratch_sfx = "audio/sfx/record_scratch-108233.ogg"
