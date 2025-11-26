label a2_s1:
  scene bg mall with fade

  # music MallTheme
  play music mall_theme fadein 0.5 fadeout 0.5

  # Show Swage 25% from left edge
  show swage normal at left, Transform(xalign=0.15) with moveinleft
  pause 0.25

  # Show Boost & Crash 25% from right edge
  show boost normal at right, Transform(xalign=0.6, xzoom=-1) with moveinright
  pause 0.25
  show crash normal at right, Transform(xalign=0.85, xzoom=-1) with moveinright

  #show swage confident
  show swage normal # TODO replace with expression

  # show boost and crash neutral
  # (should already be neutral from above)

  s "Alright, bros, let’s take it from the top."

  play music defenders_theme_distorted fadein 0.25 fadeout 1.5
  s "One! Two! Three and Four!"
  window hide

  # Sfx music that’s just slightly off, lacking melody
  #play music defenders_theme_distorted fadein 0.25 fadeout 1.0
  pause 10

  # Show swage angry
  show swage normal # TODO expression
  pause 0.25

  # Show crash shock
  show crash normal # TODO expression
  pause 0.25

  window auto

  s "ARG!! Come on, guys! Get it together!"
  stop music fadeout 0.5
  pause 0.5

  play music mall_theme

  # Show crash angry
  show crash normal # TODO expression

  c "Well it’s not like you’re doing any better than us!"

  # Show boost angry
  show boost normal # TODO expression

  b "This feud is tearing us apart!!"

  b "And it’s only been fifteen minutes since Phase left."

  s "What did I tell you about saying his name around these parts?"

  # Show boost neutral
  show boost normal # TODO expression

  b "As far as I can recall, nothing. Again, it’s only been fifteen minutes."

  b "And we’ve been practicing the entire time."

  # Show crash sad
  show crash normal # TODO expression

  c "And you keep yelling at us. I can’t perform well under these conditions."

  # Show swage sad
  show swage normal # TODO expression

  s "{i}sigh{/i}... You’re right. Sorry. This whole leadership thing is harder than I thought it was going to be."

  # Show swage neutral
  show swage normal # TODO expression

  s "But if we want to have a well rounded sound still, we’re going to need to practice even harder than we did before."

  s "One of you two is going to have to sing now, too."

  # Show swage confident
  show swage normal # TODO expression

  s "Boost! How about you give us a verse, bro?"

  # Show boost shock
  show boost normal # TODO expression

  b "Me?! Okay sure, but you should cover your ears first."

  # Show crash confident
  show crash normal # TODO expression

  c "Awww, dude, don’t harsh yourself like that! I bet you’ve got wicked pipes."

  #Show swage neutral
  show swage normal # TODO expression

  #Show boost neutral
  show boost normal # TODO expression

  #Show crash neutral
  show crash normal # TODO expression

  play music defenders_theme_distorted fadeout 0.25
  s "Take it from the top! One, two, three and four!"

  window hide

  # Sfx bad music AND bird squaking
  play sound crow_caw_sfx loop

  pause 5.0

  #Show Crash shock
  show crash normal # TODO expression

  #Show Swage shock
  show swage normal # TODO expression

  stop music fadeout 1.0
  pause 0.5
  stop sound fadeout 1.0

  play music mall_theme fadein 0.5 fadeout 0.5

  window auto

  c "Woah…..Gnarly."

  s "Okay... so Boost is banned from ever singing again."

  # Show boost confident
  show boost normal # TODO expression

  b "I did tell you to cover your ears."

  # Show Swage neutral
  show swage normal

  s "How about you, Crash? Think you could do better?"

  # Show crash neutral
  show crash normal

  c "No way. I’ve got enough trouble keeping the beat as it is. You ask me to sing alongside that and I’d throw everybody off."

  # Show Swage confident
  show swage normal # TODO expression

  s "Come on, dude. Give it a try! We know you’ve got a hell of a voice."

  b "In the sense that I think you could summon devils accidentally."

  # Show Crash sad
  show crash normal # TODO expression

  c "Give me a break, Swage. I’m still the newest member here. Since you’re the leader, shouldn’t you also be the vocalist?"

  # Show Swage neutral
  show swage normal

  s "Well yeah, but I just can’t hit the range for our current songs. We’d have to pump out a whole new EC for me to feel comfortable with it."

  s "And if Limiter shows up before we’re ready, Haven Mall is at risk of permanent closure."

  # Show Swage confident
  show swage normal # TODO expression

  s "So we have to do this, bros. It’s the only way."

  b "You could always try and reconcile with Pha-"
  play sound record_scratch_sfx

  # Show swage angry
  show swage normal # TODO expression

  s "DON’T SAY HIS NAME!"

  s "Whatever. We don’t need a vocalist. We can do this all instrumental."

  s "Take it from the top! One, two, three and four!"

  # Sfx bad music
  play music defenders_theme_distorted fadeout 0.25

  # Show boost sad
  show boost normal # TODO expression

  # Show Crash confident
  show crash normal # TODO expression

  # Show Swage neutral
  show swage normal

  pause 2.0
  "..."
  
  stop music fadeout 1.0
  play music mall_theme fadein 0.5 fadeout 0.5

  b "We’re all going to die."

  c "I thought we sounded pretty good that time. I think we got this!"

  b "In your dreams, and those seem more like nightmares if you thought that noise was any good."

  # Show boost neutral
  show boost normal

  b "Just fess up to it, Swage. We can’t do this without him."

  # Show Swage sad
  show swage normal # TODO expression

  # Show Crash neutral
  show crash normal

  s "I know, bro…."

  s "You think I don’t know that? Phase took over for his father without missing a beat."

  s "And though I miss the older guy, his younger treble maker of a son knows how to put on a good proper show."

  # Show Crash sad
  show crash normal # TODO expression

  c "But he didn’t have to make it all about himself, you know?"

  c "He wouldn’t even have center stage if we weren’t there."

  # Show Swage angry
  show swage normal # TODO expression

  s "Him pulling that solo stunt was still wrong. He put us in danger for a pretty bogus reason."

  # Show Swage neutral
  show swage normal

  s "We gotta talk to him about it again and see if we can get it through his thick skull that he can’t just use us for his own ego."

  b "About that…. So I’m not sorry for telling him about how we can all possibly tap into the Heart Machine."

  # Show Boost confident
  show boost normal # TODO expression

  b "He knew he could count on me. He trusted me to be right from the get go."

  s "Bro, you know we trust you too. I just think we should have had a practice session before going live with it."

  b "That’s what I said too. We’d have known for sure and been safer in the long run."

  # Show Boost neutral
  show boost normal

  b "Phase is over confident. But he’s also got a point."

  b "The fans think you’re the leader here, Swage."

  # Show Swage shock
  show swage normal # TODO expression

  s "Me? Well, I guess I’ve been a member of the band the longest."

  b "Exactly. And they love Crash for his newbie status."

  # Show Crash confident
  show crash normal # TODO expression

  c "Thanks!"

  b "And everybody loves a sarcastic edgy technophile, so I know they love me."

  # Show Boost confident
  show boost normal # TODO expression

  b "As they should."

  #Show Boost neutral
  show boost normal

  # Show Crash neutral
  show crash normal

  # Show Swage neutral
  show swage normal

  b "Phase just doesn’t seem to have the same draw. He might be the leader, but he’s never the face of the group."

  c "Hey come to think of it, whenever we do album covers, it’s either all of us or none of us."

  s "That’s the way it should be! It’s about the team! It’s not about which one of us people like more or less or getting extra attention just for being the leader."

  # Show Crash shock
  show crash normal # TODO expression

  c "Oh, I think I get it, Boost!"

  # Show Crash confident
  show crash normal # TODO expression

  c "You’re trying to get Swage to realize that now that he’s the leader, he’d feel pretty bad if he wasn’t treated better."

  b "Close enough."

  # Show Swage angry
  show swage normal # TODO expression

  s "Bros, I’m not picking up what you’re putting down. Just cause I’m the leader now doesn’t mean I want my name in lights and you to be in my shadow."

  c "Well sure, but like, what if you did all this extra work but nobody ever said thank you for it?"

  # Show Swage sad
  show swage normal # TODO expression

  s "…oh."

  # Show Crash sad
  show crash normal # TODO expression

  c "I don’t think I can remember the last time I said thank you to Phase."

  b "You’re right though, Crash. Phase needs us."

  # Show Crash neutral
  show crash normal # TODO expression

  b "But we need him too."

  # Show Swage neutral
  show swage normal # TODO expression

  s "Tsk. Fine. Let’s go find him and try and talk this out again."

  s "But I’m only giving him one chance to fess up. If he still acts all high and mighty after we play our chords, I’m out of here."

  hide swage with dissolve
  pause 0.1
  hide boost with dissolve
  pause 0.1
  hide crash with dissolve
  pause 0.25

  jump a2_s2

label a2_s2: # fourth scene, second scene in act 2

  show bg arcade with fade
  
  #music ArcadeTheme
  play music arcade_theme fadein 0.5 fadeout 0.5
  
  #Show Phase center screen
  show phase normal at center with moveinleft

  # sfx keytar noises, with some off notes
  "{i}Phase plays his keytar. He misses a few notes.{/i}"

  # Show Phase angry
  show phase normal # TODO insert expression here once finished

  p "Grrrrrrrrrr. Come on, Phase. You know you can do better than that."

  # Show Phase confident
  show phase normal # TODO insert expression here once finished

  p "V7Sus4 start is sounding kind of boss, at least."

  p "Needs more distortion for that out of this world feel."

  p "Maybe a little modulation?"

  # Show Phase sad
  show phase normal # TODO insert expression here once finished

  p "Oh what am I even saying? Boost is the one who handles all the audio babble."

  # Show Phase confident
  show phase normal # TODO insert expression here once finished

  p "I’m just going to play and sing, and it’ll sound amazing because I wrote it and I did it myself."

  # Show Phase angry
  show phase normal # TODO insert expression here once finished

  p "And maybe SOMEBODY will finally realize that I’m as awesome as I really am."

  # Sfx keytar noises, maybe with a bit more anger behind them?
  "Phase continues angrily playing his keytar."

  #Show Phase sad
  show phase normal # TODO insert expression here once finished

  p "No no no that’s not it either."

  # Show Phase angry
  show phase normal # TODO insert expression here once finished

  p "This was so easy last time! It was like just being near the Heart Machine synchronized my fingers to the music."

  p "I didn’t even have to think! I just played and the music was perfect."

  p "Why can’t I get a good sound out of it this time?"

  #Show Phase 25% right edge
  show phase normal at left, Transform(xalign=0.25) with move # TODO insert expression here once finished

  #Show Jeff 25% left edge
  show jeff normal at right, Transform(xalign=0.75, xzoom=-1) with moveinright

  # Show Jeff neutral

  j "I never thought you’d be the type who got angry at a game."

  j "But I feel you. That one is notorious for being a coin consumer."

  # Show Phase neutral
  show phase normal # TODO insert expression here once finished

  j "Try the pellet eater three machines down. Much easier, and good for warming up before the harder games."

  p "Oh, hey Jeff. Nah, man, I’m just trying to come up with some new tunes."

  j "Radical. What’s the inspiration for your band’s next hit? Some of these old games have some real slick tunes you could nick and nobody would even know."

  # Show Phase sad
  show phase normal # TODO insert expression here once finished

  p "There’s no band anymore, Jeff. It’s just me. And I can’t even come up with a single good starting chord that I like."

  # Show Jeff sad
  show jeff normal # TODO insert expression here once finished

  j "Bogus, man. How about you try practicing with some of your classic jams?"

  # Show Phase angry
  show phase normal # TODO insert expression here once finished

  p "I tried that too! But I kept getting the notes wrong, or forgetting the lyrics, and I couldn’t keep the meter on my own."

  # Show Phase sad
  show phase normal # TODO insert expression here once finished

  p "I didn’t think going solo would be this hard."

  # Show Jeff confident
  show jeff normal # TODO insert expression here once finished

  j "Sounds like you just need a break to relax. You’re trying to force yourself to work instead of just letting the world flow around and through you."

  j "Come on, try out that pellet eater. I’ll spot you the tokens necessary to give it a few goes."

  # Show Phase neutral
  show phase normal # TODO insert expression here once finished

  p "Fine…. But just for a few minutes."

  # some kind of little transition here to imply they moved?
  
  hide phase with dissolve
  hide jeff with dissolve
  window hide
  show bg black with fade
  pause 0.5
  show bg arcade with fade
  show phase normal at left, Transform(xalign=0.25) with dissolve # TODO insert expression here once finished
  show jeff normal at right, Transform(xalign=0.75, xzoom=-1) with dissolve
  window auto
  

  # Show Phase confident
  show phase normal # TODO insert expression here once finished
  
  # Show Jeff neutral
  show jeff normal # TODO insert expression here once finished

  p "Ha! Another level down. This is too easy."

  j "Good to see you more relaxed. You were looking real tense there."

  # Show Phase angry
  show phase normal # TODO insert expression here once finished

  p "Got into a fight with the guys. They just don’t get it."

  # Show Jeff shock
  show jeff normal # TODO insert expression here once finished

  j "Not sure I get ‘it’ either, but I’m chill to listen."

  # Show Phase neutral
  show phase normal # TODO insert expression here once finished

  p "You run this place yourself, right?"

  # Show Jeff confident
  show jeff normal # TODO insert expression here once finished

  j "Sure do. It’s a lot of work, but I enjoy it, so I guess it’s not really like work that way."

  p "Uh huh. And you get all the praise for doing all that work too, I bet."

  p "You don’t have to be just a note in a chord. You get to be your own melody."

  # Show Phase sad
  show phase normal # TODO insert expression here once finished

  p "Sounds nice."

  # Show Jeff neutral
  show jeff normal # TODO insert expression here once finished

  j "Hmmmm."

  # Sfx of jeff taking a drag
  play sound inhale_exhale_sfx
  
  j "You know, when I first started working here, I really looked up to the guy who ran this place."
  
  j "He wasn’t always the best manager. He’d call out sick regularly, or forget to assign shifts, and he’d let all sorts of bad behavior slide."
  
  j "But I liked him. He taught me how to just relax and do what needed to be done."
  
  j "He gave me the key to lockup one day and said ‘Jeff, this place is yours now.’"
  
  j "I didn’t see where he went. I thought he was just going to get lunch."
  
  j "Well, when he didn’t come back the next day, I figured I’d better step up until he did. So I went into his office in the back and checked around the place."
  
  j "The place was a mess. Still is. Haven’t had time to really give it a good clean."
  
  j "One thing really caught my attention though. A poster on the wall."
  
  j "’Friendship and Excellence’."

  # Show Phase neutral
  show phase normal # TODO insert expression here once finished

  p "Huh. Is that where you got that from?"

  j "I guess so. I started saying it because he said it all the time. That’s what made him such a good leader, though."

  j "At the end of the day, the thing he cared about most was maintaining the good vibes with people around him."

  j "That’s kind of like your dad, too."

  # Show Phase sad
  show phase normal # TODO insert expression here once finished

  p "…"

  # Show Jeff sad
  show jeff normal # TODO insert expression here once finished

  j "Sorry, shouldn’t be bringing him up, I know, I know. But you gotta understand, Phase."

  # Show Jeff neutral
  show jeff normal # TODO insert expression here once finished

  j "The folks here in Haven Mall who have had the best success weren’t the toughest, or the smartest, or the most skilled."

  j "It’s those who know how to harness Friendship and Excellence."

  # Show Phase neutral
  show phase normal # TODO insert expression here once finished

  p "The powers of radicalness…."

  # Show Jeff shock
  show jeff normal # TODO insert expression here once finished

  j "Haven’t heard that connection in some time, now that I think about it."

  # Show Jeff confident
  show jeff normal # TODO insert expression here once finished

  j "Seems like you know what it means, though. And how to use it properly."

  p "I guess… I guess I just forgot about it all."

  p "I was so jazzed up on my own meter that I was letting it disrupt the group rhythm."

  # Show Phase Confident
  show phase normal # TODO insert expression here once finished

  p "It just felt so good to really be the star finally, you know?"

  p "Have the limelights shining on me."

  # Show Jeff neutral
  show jeff normal # TODO insert expression here once finished

  j "Is that what you want the most?"

  # Show Phase neutral
  show phase normal # TODO insert expression here once finished

  p "I dunno, dude. As good as it felt, if it means now I’ve got nobody to jam with, it doesn’t seem worth it."

  # Sfx mall sirens going off
  play sound siren_sfx

  # Show Phase shock
  show phase normal # TODO insert expression here once finished
  
  p "Limiter!"

  p "Hate to cut this chat short, Jeff, but I’ve got to make sure that gooey cobra gets repulsed."

  # Show Phase confident
  show phase normal # TODO insert expression here once finished

  p "I’ll catch up with you later. Keep the Heart Machine safe!"

  # Exit Phase
  hide phase with dissolve

  # Sfx Jeff puffing on his joint
  play sound inhale_exhale_sfx

  pause 0.75

  # Show Jeff confident
  show jeff normal # TODO insert expression here once finished

  j "Yeah…. He’s got the potential to be the best."

  jump end

