init python:
  music_tracks = {
    "pachelbels-canon": {
      "title": "Pachelbel's Canon (Canon in D)",
      "artist": "Johann Pachelbel",
      "file": "audio/bgm/canon-in-d-pachelbel.ogg",
    },
    "gran-vals": {
      "title": "Gran Vals",
      "artist": "Francisco Tarrega",
      "file": "audio/bgm/gran-vals-francisco-tarrega.ogg"
    },
    "gymnopedie-no-1": {
      "title": "Gymnopédie no. 1",
      "artist": "Erik Satie",
      "file": "audio/bgm/gymnopedie-1-erik-satie.ogg"
    },
    "fur-elise": {
      "title": "Für Elise",
      "artist": "Ludwig van Beethoven",
      "file": "audio/bgm/fur-elise-beethoven.ogg"
    }
  }

  mr = MusicRoom(fadeout=1.0)

  for track in list(music_tracks.values()):
    mr.add(track["file"])