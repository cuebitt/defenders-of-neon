init python:
  # Wrapper for auto-highlight
  # Changes the speaker's sprite to a talk sprite if they have a "normal" expression
  def _name_callback(event, interact=True, name=None, **kwargs):
    name_callback(event, interact=True, name=None, **kwargs)

    global speaking_char
    if event == "begin":
      speaking_char = name

    shown = renpy.get_attributes(speaking_char)
    if not shown:
      return
    is_normal = ("normal" in shown)
    is_talk = ("talk" in shown)

    if event == "begin":
      if is_normal:
        renpy.show(f"{speaking_char} talk")
    elif event == "end":
      if is_talk:
        renpy.show(f"{speaking_char} normal")

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define p = Character(_("Phase"), color="#C13D3C", callback=_name_callback, cb_name="phase", image="phase")
define s = Character(_("Swage"), color="#41447D", callback=name_callback, cb_name="swage")
define c  = Character(_("Crash"), color="#46523D", callback=name_callback, cb_name="crash")
define b = Character(_("Boost"), color="#603353", callback=name_callback, cb_name="boost")
define l = Character(_("Limiter"), color="#534C72", callback=name_callback, cb_name="limiter")
define j = Character(_("Jeff"), color="#574A4A", callback=name_callback, cb_name="jeff")

#image phase normal = At('phase_normal', sprite_highlight('phase'))
image swage normal = At('swage_normal', sprite_highlight('swage'))
image crash normal = At('crash_normal', sprite_highlight('crash'))
image boost normal = At('boost_normal', sprite_highlight('boost'))
image limiter normal = At('limiter_normal', sprite_highlight('limiter'))
image jeff normal = At('jeff_normal', sprite_highlight('jeff'))

layeredimage phase:
  at sprite_highlight('phase'), Transform(xzoom=0.45, yzoom=0.45, yoffset=100)
  always:
    "images/phase/phase_base.png"
  
  group face auto:
    pos (315, -540)
    attribute normal default

  always:
    pos (290, 85)
    "images/phase/phase_hood.png"
      

