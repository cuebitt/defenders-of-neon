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
image swage normal = At('shark_final', sprite_highlight('swage'), Transform(zoom=.35, yoffset=50))
image swage shocked = At('shark_final', sprite_highlight('swage'), Transform(zoom=.35, yoffset=50))
image swage confident = At('shark_final', sprite_highlight('swage'), Transform(zoom=.35, yoffset=50))
image swage sad = At('shark_final', sprite_highlight('swage'), Transform(zoom=.35, yoffset=50))
image swage angry = At('shark_final', sprite_highlight('swage'), Transform(zoom=.35, yoffset=50))
image swage happy = At('shark_final', sprite_highlight('swage'), Transform(zoom=.35, yoffset=50))

image crash normal = At('gaytor_final', sprite_highlight('crash'), Transform(zoom=.35, yoffset=100))
image crash shocked = At('gaytor_final', sprite_highlight('crash'), Transform(zoom=.35, yoffset=100))
image crash confident = At('gaytor_final', sprite_highlight('crash'), Transform(zoom=.35, yoffset=100))
image crash sad = At('gaytor_final', sprite_highlight('crash'), Transform(zoom=.35, yoffset=100))
image crash angry = At('gaytor_final', sprite_highlight('crash'), Transform(zoom=.35, yoffset=100))
image crash happy = At('gaytor_final', sprite_highlight('crash'), Transform(zoom=.35, yoffset=100))

image boost normal = At('birb_final', sprite_highlight('boost'), Transform(zoom=.35, yoffset=50))
image boost shocked = At('birb_final', sprite_highlight('boost'), Transform(zoom=.35, yoffset=50))
image boost confident = At('birb_final', sprite_highlight('boost'), Transform(zoom=.35, yoffset=50))
image boost sad = At('birb_final', sprite_highlight('boost'), Transform(zoom=.35, yoffset=50))
image boost angry = At('birb_final', sprite_highlight('boost'), Transform(zoom=.35, yoffset=50))
image boost happy = At('birb_final', sprite_highlight('boost'), Transform(zoom=.35, yoffset=50))

image limiter normal = At('cobra_final', sprite_highlight('limiter'), Transform(zoom=.4, xoffset=100, yoffset=100))
image limiter confident = At('cobra_final', sprite_highlight('limiter'), Transform(zoom=.4, yoffset=100))
image limiter shocked = At('cobra_final', sprite_highlight('limiter'), Transform(zoom=.4, yoffset=100))
image limiter sad = At('cobra_final', sprite_highlight('limiter'), Transform(zoom=.4, yoffset=100))
image limiter angry = At('cobra_final', sprite_highlight('limiter'), Transform(zoom=.4, yoffset=100))
image limiter happy = At('cobra_final', sprite_highlight('limiter'), Transform(zoom=.4, yoffset=100))

image jeff normal = At('racoon_final', sprite_highlight('jeff'), Transform(zoom=.35, yoffset=50))
image jeff shocked = At('racoon_final', sprite_highlight('jeff'), Transform(zoom=.35, yoffset=50))
image jeff confident = At('racoon_final', sprite_highlight('jeff'), Transform(zoom=.35, yoffset=50))
image jeff sad = At('racoon_final', sprite_highlight('jeff'), Transform(zoom=.35, yoffset=50))
image jeff angry = At('racoon_final', sprite_highlight('jeff'), Transform(zoom=.35, yoffset=50))
image jeff happy = At('racoon_final', sprite_highlight('jeff'), Transform(zoom=.35, yoffset=50))

layeredimage phase:
  at sprite_highlight('phase'), Transform(zoom=0.4, yoffset=100)
  always:
    "images/phase/phase_base.png"
  
  group face auto:
    pos (315, -540)
    attribute normal default

  always:
    pos (290, 85)
    "images/phase/phase_hood.png"
      

