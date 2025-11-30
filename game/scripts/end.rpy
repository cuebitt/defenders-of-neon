# The game ends here.

label end:
  play music defenders_of_neon_theme fadein 0.5 fadeout 0.5
  scene black

  show image "gui/episode_title.png" with dissolve

  "{b}The End{/b}."

  "Thank you for playing our game, Defenders of Neon: Season 2, Episode 8: {i}Phase's Solo{/i}!"

  "We made this game for {a=https://itch.io/jam/novembuck-fvn-jam}Novembuck '25{/a}!"

  "For more information, see the {a=https://cuebitt.itch.io/defenders-of-neon}Defenders of Neon itch.io page{/a}."

  "Defenders of Neon: Season 2, Episode 8: {i}Phase's Solo{/i} is a game by {a=https://bsky.app/profile/bighufferpuffer.bsky.social}BigHufferPuffer{/a}, {a=https://bsky.app/profile/cuebitt.rip}Cuebitt{/a}, {a=https://bsky.app/profile/grufflo.bsky.social}Grufflo{/a}, {a=https://bsky.app/profile/komodomode.bsky.social}KOMODOMODE{/a}, and {a=https://bsky.app/profile/zevfox.bsky.social}Zev{/a}."

  play sound splat_sfx

  "Mwehehehehe!"

  # This ends the game.

  scene bg black with fade

  return
