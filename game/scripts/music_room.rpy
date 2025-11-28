## Music Room ##################################################################
##
## Allows the player to re-play music from the game.
##
## https://www.renpy.org/doc/html/rooms.html#music-room
init python:
    def get_next_track_idx(offset):
        global current_track_idx

        curr_idx = current_track_idx
        track_ids = list(music_tracks.keys())

        next_idx = (curr_idx + offset) % len(track_ids)
        track_id = track_ids[next_idx]

        while(not mr.is_unlocked(music_tracks[track_ids[next_idx]]['file'])):
            next_idx = (next_idx + offset) % len(track_ids)
            track_id = track_ids[next_idx]
        
        current_track_idx = next_idx

    def get_duration(channel):
        dur = renpy.music.get_duration(channel)
        return dur if dur is not None else 0

    def enter_music_room():
        global current_track_idx

        current_track_idx = -1
    
    def seek_music(value):
        renpy.music.pump()

        playing = renpy.music.get_playing()
        prefix_end = renpy.music.get_playing().find('>')
        if prefix_end != -1:
            playing = renpy.music.get_playing()[prefix_end+1:]

        renpy.music.play(f"<from {round(value, 2)} loop 0.0>{playing}")


    def set_bar_value(widget_id):
        widget = renpy.get_widget("music_room", widget_id)
        x, y = renpy.get_mouse_pos()
        bar_x, bar_y, width, height = renpy.focus_coordinates()

        rel = max(0, min(1, (x - bar_x) / width))
        seek_music(get_duration("music") * rel)

    def unpause():
        global music_room_paused

        music_room_paused = False

default current_track_idx = -1
default music_room_paused = True

style music_list_btn:
    color "#00f0ff"
    hover_color "#8af7ff"
    insensitive_color "#00a4af"

screen music_room():
    tag menu
    default track_ids = list(music_tracks.keys())
    
    
    use game_menu(_("Cassette Player")):
        fixed:
            vbox:
                spacing 10
                xfill True
                yfill True

                frame:
                    xfill True
                    yfill False
                    ymaximum 700

                    viewport:
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        xfill True
                        yfill False

                        vbox id "btns-vbox":
                            spacing 8
                            for idx, track in enumerate(list(music_tracks.values())):
                                vbox:
                                    yfill False
                                    frame:
                                        background None
                                        ypadding 20
                                        vbox:
                                            yfill False
                                            ymaximum 100
                                            hbox:
                                                spacing 5
                                                frame:
                                                    background None
                                                    xfill False
                                                    yfill False
                                                    yalign 0.5
                                                    xsize 100
                                                    
                                                    fixed:
                                                        add (track["album_art"] or "gui/music_room/default_album_art.png"):
                                                            xalign 0.5
                                                            yalign 0.5
                                                            ysize 100
                                                            xsize 100
                                                        text f"{idx+1}":
                                                            xalign 0.5
                                                            yalign 0.5
                                                            outlines [(2, "#000000")]

                                                vbox:
                                                    xfill True
                                                    yfill False
                                                    
                                                    textbutton f"{track['title']}":
                                                        text_style "music_list_btn"
                                                        action [mr.Play(track["file"]), SetVariable("current_track_idx", idx), Function(unpause)]
                                                    text f"{track['artist']}":
                                                        xalign 0.007
                                                        size 24
                                                        italic True
                                                        color "#10bbc8"

                                    frame:
                                        background None
                                        xfill True
                                        add Solid("#009cd1", xysize=(1370,2))

                frame:
                    xfill True
                    yfill True
                    padding (50,0)
                    background Frame("gui/music_room/bottom_frame.png", 10, 10, 10, 10)

                    hbox:
                        spacing 50
                        yalign 0.5
                        hbox:
                            align (0.5, 0.5)
                            spacing 25
                            imagebutton auto "gui/music_room/previous_%s.png":
                                action [mr.Previous(), Function(get_next_track_idx, -1)]
                            imagebutton auto ("gui/music_room/play_%s.png" if music_room_paused else "gui/music_room/pause_%s.png"):
                                action [mr.TogglePause(), SetScreenVariable("music_room_paused", not music_room_paused)]
                                sensitive current_track_idx != -1
                            imagebutton auto "gui/music_room/next_%s.png":
                                action [mr.Next(), Function(get_next_track_idx, 1)]

                        hbox:
                            spacing 25
                            if current_track_idx != -1:
                                add (track["album_art"] or "gui/music_room/default_album_art.png"):
                                    xalign 0.5
                                    yalign 0.5
                                    ysize 100
                                    xsize 100

                            vbox:
                                spacing 10
                                yfill True
                                frame:
                                    background None
                                    padding (10, 10)
                                    vbox:
                                        text (music_tracks[track_ids[current_track_idx]]['title'] if current_track_idx != -1 else 'Not Playing')
                                        text (music_tracks[track_ids[current_track_idx]]['artist'] if current_track_idx != -1 else '-'):
                                            # xalign 0.007
                                            size 24
                                            italic True
                                            color "#737373"

                                if current_track_idx != -1:
                                    fixed:
                                        ysize 25
                                        bar:
                                            value AudioPositionValue("music", update_interval=0.1)
                                            xfill True
                                            ysize 20
                                        button id "pbar":
                                            background None
                                            ymaximum 20
                                            action Function(lambda: set_bar_value("pbar"))

        add "gui/music_room/cassette_thing.png":
            align (.6, -.2125)
    on "replace" action [Stop("music"), Function(enter_music_room)]
    on "replaced" action Play("music", "audio/bgm/cafe-restaurant-bossa-nova-music.ogg")
