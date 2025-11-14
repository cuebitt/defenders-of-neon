label s1_comic_panels: 
  # BEGIN COMIC SECTION
  scene bg comic

  show expression Text("Placeholder - comic goes here", xalign=0.5, yalign=0.005, color="#71717a") as top_label with dissolve

  play music peril_theme

  show swage normal at left with moveinleft # temp: replace with comic panels

  s "This is bad, bros."

  show crash normal at left, Transform(xalign=0.15) with moveinleft # temp: replace with comic panels

  c "Seems like this might be our closing act."

  show boost normal at left, Transform(xalign=0.4) with moveinleft # temp: replace with comic panels

  b "It does feel kind of good, though."

  show limiter normal at right, Transform(xzoom=-1) with moveinright: # temp: replace with comic panels
    on hide:
      rotate 0
      alpha 1.0
      easein 3.0 rotate 720 xpos 1.5 alpha 0.0

  l "Mwehehehe! At last! You’ll all be turned into my mindless drones!"

  l "And with you half rate musicians out of the way, the Heart Machine will finally be mine!"

  hide top_label with dissolve

  # END COMIC SECTION

  #scene bg Haven Mall
  scene bg mall with fade
  play music phase_theme

  show limiter normal at right, Transform(xzoom=-1) with moveinright:
    on hide:
      rotate 0
      alpha 1.0
      easein 3.0 rotate 720 xpos 1.5 alpha 0.0

  show swage normal at left with moveinright
  show crash normal at left, Transform(xalign=0.1) with moveinright
  show boost normal at left, Transform(xalign=0.3) with moveinright

  show phase normal at center zorder 10 with moveinleft

  p "Hate to slow your tempo, Limiter, but you won’t be getting your dirty coils around the Heart Machine today!"

  s "Phase!"

  c "About time you showed up!"

  b "Oh. Yay, I guess."

  p "Time to send you back to the coda with a sick riff."

  $ renpy.music.set_volume(0.5, delay=1.0, channel="music")
  play sound phase_instrument_sfx loop

  c "The goo is retreating!"

  s "Get your instruments, bros, and let’s rock!"

  b "You sure we can’t just enjoy it for another minute? No? Fiiiiiiiiine."

  p "Relax, gang. I told you before, I got this one."

  hide swage
  hide crash
  hide boost

  show phase normal at left with moveinright

  l "Pathetic fool! You think you can take me on by yourself?"

  p "I know I can. Dig this solo and find out for yourself."

  $ renpy.music.set_volume(1.25, delay=0.5, channel='sound')

  p "Match my souped up rhythm if you can, Limiter."

  l "Urgh! When did you get so strong?!"

  p "While you’ve been scheming, I’ve been shredding. Try all you like, Limiter, but you’ll never be better than me."

  l "Gaaaaaaaaaaaah! The groove is too powerful! Curse you, Defenders of Neon!"

  stop sound fadeout 0.5
  $ renpy.music.set_volume(1.0, delay=0, channel='sound')
  $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

  hide limiter

  l "You may have won this day, but you can’t keep the Haven Mall safe forever! I’ll be back! And you’ll all become a part of my drone army!"
  
  show boost normal at right, Transform(xalign=.5, xzoom=-1) with moveinleft
  show crash normal at right, Transform(xalign=.7, xzoom=-1) with moveinleft
  show swage normal at right, Transform(xalign=.9, xzoom=-1) with moveinleft

  b "Sure, just like you said last episode. Whatever. Later, snake. Until the next one."

  p "Did you catch that? I sent that tone deaf loser packing without even breaking a sweat. Told you I’d be able to do it. I never doubted myself for a beat."

  s "We didn’t doubt you could, bro."

  c "We just said that it was too dangerous and an unnecessary risk to go off on your own like that."

  p "Well it all worked out. So there’s nothing to worry about."

  c "No. This isn’t harmonizing. We have to talk about this. Let’s get a jam session in while we debrief."

  p "Wicked. You'll get to hear for yourself just how much better I sound now."

  # jump scene 2
