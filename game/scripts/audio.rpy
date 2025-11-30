# "defenders_theme_distorted": {
#       "title": "Defenders of Neon Theme (Distorted) (Band Practice)",
#       "artist": "freesound_community",
#       "file": "audio/bgm/band-practice-67276.ogg",
#       "album_art": ""
#     },
#     "peril_theme": {
#       "title": "Peril Theme (Dubstep - Imminent Danger)",
#       "artist": "AntipodeanWriter",
#       "file": "audio/bgm/dubstep-imminent-danger-13039.ogg",
#       "album_art": ""
#     },
#     "phase_theme": {
#       "title": "Phase Theme (Crimson Shadows of the Electric Night)",
#       "artist": "susan-lu4esm",
#       "file": "audio/bgm/crimson-shadows-of-the-electric-night-433424.ogg",
#       "album_art": ""
#     },
#     "arcade_theme": {
#       "title": "Arcade Theme (Retro Arcade Game Music)",
#       "artist": "MFCC",
#       "file": "audio/bgm/retro-arcade-game-music-297305.ogg",
#       "album_art": ""
#     },
#     "mall_theme": {
#       "title": "Mall Theme (The Ghost of Shepherd's Pie - GBML)",
#       "artist": "GeoffreyBurch",
#       "file": "audio/bgm/the-ghost-of-shepardx27s-pie-glbml-112816.ogg",
#       "album_art": ""
#     },
#     "limiter_theme": {
#       "title": "Limiter Theme (Epic Sci-Fi Villain Theme for Cinematic Projects)",
#       "artist": "nickpanek",
#       "file": "audio/bgm/epic-sci-fi-villain-theme-for-cinematic-projects-224750.ogg",
#       "album_art": ""
#     }



init python:
    # "": {
    #     "title": "",
    #     "artist": "KOMODOMODE",
    #     "file": "audio/bgm/komodomode",
    #     "album_art": ""
    # }

    music_tracks = {
        "band_practice": {
            "title": "Band Practice",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/band_practice.ogg",
            "album_art": ""
        },
        "band_practice_bird_vocals": {
            "title": "Band Practice (Bird Vocals)",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/band_practice_bird_vocals.ogg",
            "album_art": ""
        },
        "haven_mall_vaporwave": {
            "title": "Haven Mall (Vaporwave)",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/haven_mall_vaporwave_edition.ogg",
            "album_art": ""
        },
        "haven_mall": {
            "title": "Haven Mall",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/haven_mall_music.ogg",
            "album_art": ""
        },
        "get_zonked": {
            "title": "Get Zonked (Limiter's Theme)",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/get_zonked.ogg",
            "album_art": ""
        },
        "defenders_of_neon_theme_bromance_loop": {
            "title": "Defenders of Neon Theme (Bromance Loop)",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/defenders_of_neon_theme_bromance_loop.ogg",
            "album_art": ""
        },
        "defenders_of_neon_theme_loop": {
            "title": "Defenders of Neon Theme (Loop)",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/defenders_of_neon_theme_loop.ogg",
            "album_art": ""
        },
        "defenders_of_neon_theme": {
            "title": "Defenders of Neon Theme",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/defenders_of_neon_theme.ogg",
            "album_art": ""
        },
        "limiters_lair": {
            "title": "Limiter's Lair",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/limiters_lair_theme.ogg",
            "album_art": ""
        },
        "jeffs_arcade": {
            "title": "Jeff's Arcade",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/jeffs_arcade.ogg",
            "album_art": ""
        },
        "jeffs_funky_beatz": {
            "title": "Jeff's Funky Beatz",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/jeffs_funky_beatz.ogg",
            "album_art": ""
        },
        "phase_keytar_solo": {
            "title": "Keytar Solo",
            "artist": "KOMODOMODE",
            "file": "audio/bgm/komodomode/phase_solo_riff.ogg"
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
define audio.phase_instrument_sfx = "audio/sfx/komodomode/keytar_noises_angry.ogg"
define audio.phase_instrument_sfx_distorted = "audio/sfx/komodomode/keytar_noises_off_notes.ogg"
define audio.inhale_exhale_sfx = "audio/sfx/komodomode/jeff_joint_inhale.ogg"
define audio.siren_sfx = "audio/sfx/komodomode/mall_alarm.ogg"

define audio.record_scratch_sfx = "audio/sfx/record_scratch-108233.ogg"
define audio.splat_sfx = "audio/sfx/cartoon-splat-310479.ogg"
