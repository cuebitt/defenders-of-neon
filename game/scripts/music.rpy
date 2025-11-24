init python:
  music_tracks = {
    "pachelbels_canon": {
      "title": "Pachelbel's Canon (Canon in D)",
      "artist": "Johann Pachelbel",
      "file": "audio/bgm/canon-in-d-pachelbel.ogg",
    },
    "gran_vals": {
      "title": "Gran Vals",
      "artist": "Francisco Tarrega",
      "file": "audio/bgm/gran-vals-francisco-tarrega.ogg"
    },
    "gymnopedie_no_1": {
      "title": "Gymnopédie no. 1",
      "artist": "Erik Satie",
      "file": "audio/bgm/gymnopedie-1-erik-satie.ogg"
    },
    "fur_elise": {
      "title": "Für Elise",
      "artist": "Ludwig van Beethoven",
      "file": "audio/bgm/fur-elise-beethoven.ogg"
    }
  }

  # Create a music room
  mr = MusicRoom(fadeout=1.0)

  # Add music tracks to music room and audio object
  for track_id, track_data in music_tracks.items():
    mr.add(track_data["file"])                    # add to music room
    setattr(audio, track_id, track_data["file"])  # add to audio object
