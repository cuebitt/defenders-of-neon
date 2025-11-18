label a1_s1_comic_panels: 
  # BEGIN COMIC SECTION
  scene bg comic

  show expression Text("Placeholder - comic goes here", xalign=0.5, yalign=0.005, color="#71717a") as top_label with dissolve

  play music peril_theme fadein 0.5 fadeout 0.5

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
  jump a1_s1_main

label a1_s1_main:

  #scene bg Haven Mall
  scene bg mall with fade
  play music phase_theme fadein 0.5 fadeout 0.5

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

  jump a1_s2

label a1_s2:
  scene bg arcade with fade
  play music arcade_theme fadein 0.5 fadeout 0.5

  show phase normal at left, Transform(xalign=.25) with moveinleft
  show jeff normal at right, Transform(xzoom=-1) with moveinright

  p "Everything looks good here. You don’t have to worry about anything, Jeff. As long as I’m around, the Defends of Neon will make sure the Haven Mall is safe."

  j "Thanks, dude. Ya, I was doing some cleaning while you were all gone. Couldn’t even find a cobweb."

  j "But I didn’t see you around helping me do any of that cleaning."

  p "We took care of a different cleaning. Don’t worry about it."

  j "I never do when you say anything."

  p "How’s the Heart holding up today?"

  j "Beating steady as it ever does. That old thing will outlive all of us. You should try one of the newer machines."

  j "Check this one, I just rolled it out from the back. It’s got this little mechanical crane you can move around."

  show boost normal at left, Transform(xalign=0.4) with moveinleft

  b "Woah, that’s retro."

  j "I knew I liked you for a reason. You’ve got the best taste of the bunch."

  j "Tell you what, give it a go. It’s free today."

  show crash normal at left, Transform(xalign=0.15) with moveinleft
  pause 0.5
  show phase normal at up_lean
  c "You tell us they are all free every day we come over."

  j "Do I? Huh. Well, they are extra free today then."

  hide crash with moveoutright
  pause 0.1
  show swage normal at left, Transform(xalign=0.15) with moveinleft

  s "We can come back later. We’ve got a jam sesh first."

  j "Rad. One of these days I’ll come check out one of your shows. But I gotta watch the arcade or nobody else will."

  p "It’s all sweet, Jeff. We’ll hang with you later!"

  hide jeff with moveoutright

  scene bg mall with fade
  play music mall_theme fadein 0.5 fadeout 0.5

  show phase normal at left, Transform(xalign=.1) with moveinleft

  show crash normal at right, Transform(xalign=1-.0001, xzoom=-1) with moveinleft
  show swage normal at right, Transform(xalign=1-.25, xzoom=-1) with moveinleft
  show boost normal at right, Transform(xalign=1-.5, xzoom=-1) with moveinleft

  p "Alright, so are we finally gonna talk about how awesome I was there taking on Limiter like that on my own?"

  p "I told you that we could tap into the Heart Machine to amp our sound to even more powerful levels."

  p "I can take it all the way to 11 easily."

  c "It was risky, Phase. Too risky. What if it hadn’t worked?"

  b "Even with all my testing and sampling, I wasn’t totally convinced it would work."

  b "The dramatic irony of it failing was just as likely to play out as a success. It kind of depended on the narrative."

  s "I never doubted your skills, Boost. Nobody knows the Haven Mall better than you. But Phase didn’t have to run off like that just so he could come in as the big hero."

  p "Hey hey hey! I {b}am{/b} the big hero here!"

  c "It was stupid, Phase! Your big hero moment doesn’t need to come at the cost of putting us in danger!"

  p "I’m not sure what you aren’t vibing with here, Crash. You weren’t in any danger because I was always going to come in and save the day."

  c "We were half way to being turned into drones, and you say that we weren’t in any danger. Do you hear yourself when you say things like that?"

  p "Of course. I hear my singing being the thing that got Limiter out of our fur again."

  "{i}Boost coughs awkwardly.{/i}"

  p "...and feathers. And scales. Tsk, whatever. It was a fine plan, I still don’t get why you’re all so upset about it."

  s "We’re upset because ‘the plan’ was your idea and your decision and you didn’t listen to any of us when we told you it was too risky!"

  s "Are we a band or not, Phase?"

  p "We’re a band. But I’m the face, and I think I deserve a little more credit for that."

  p "I’m the leader. If sometimes I have to prove it, then I’m going to prove it."

  s "You really think that? So what, you being the leader is more important than working together? That you need to just show us all up because you can?"

  s "Because we’ve had harmony from day one, but if you’ve been holding on to some discord, I think we need to hear you resolve it."

  s "This isn’t about who’s the face. You risked our lives for your ego, bro."

  p "Why do you keep needing me to explain this to you? You weren’t in danger! I was always going to be there to push Limiter back."

  p "Tapping into the Heart Machine has radicalized my sound. I can take on Limiter any day he tries to ruin our show."

  p "Maybe it’s you who isn't trusting me, thinking that I wouldn’t be there."

  p "Maybe you’re the ones holding me back from reaching stardom."

  c "That’s… that’s nasty."

  s "So what? You want to go solo now?"

  p "I think I just proved I could, and that you're just the backup to my show."

  s "Fine!! Then go! See if any label is going to pick you up with an attitude like you’ve got."

  hide swage with moveoutright

  c "Swage!! Ugh, Phase! We’ll talk about this later. Swage! Calm down!"

  hide crash with moveoutright

  b "Tension! Perhaps we’ve got a two parter ahead of us?"

  b "For what it’s worth, Phase, I think you’re making a mistake here."

  b "But it’s yours to make. So, whenever you want to jam together again, I’ll be waiting for you."

  hide boost with moveoutleft
  pause 0.1
  show phase normal at center with move

  p "As if I’d want to jam with a band that’s holding me back."

  p "YOU’LL SEE! I’M GOING TO BE EVEN BIGGER AND BETTER THAN DEFENDERS OF NEON! AND I’LL DO IT ON MY OWN!"

  hide phase with dissolve
  pause 1.0
  
  "...who was he talking to?"

  jump end
