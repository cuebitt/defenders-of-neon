# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character(_("Phase"), color="#C13D3C", callback=name_callback, cb_name="phase")
define s = Character(_("Swage"), color="#41447D", callback=name_callback, cb_name="swage")
define c  = Character(_("Crash"), color="#46523D", callback=name_callback, cb_name="crash")
define b = Character(_("Boost"), color="#603353", callback=name_callback, cb_name="boost")
define l = Character(_("Limiter"), color="#534C72", callback=name_callback, cb_name="limiter")
define j = Character(_("Jeff"), color="#574A4A", callback=name_callback, cb_name="jeff")

image phase normal = At('phase_normal', sprite_highlight('phase'))
image swage normal = At('swage_normal', sprite_highlight('swage'))
image crash normal = At('crash_normal', sprite_highlight('crash'))
image boost normal = At('boost_normal', sprite_highlight('boost'))
image limiter normal = At('limiter_normal', sprite_highlight('limiter'))
image jeff normal = At('jeff_normal', sprite_highlight('jeff'))
