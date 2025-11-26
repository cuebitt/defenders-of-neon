transform up_lean:
  # Move the sprite slightly upward
  yoffset 0
  rotate 0
  rotate_pad True
  transform_anchor True
  subpixel True

  # Rotate by 2 degrees clockwise and up 100 px
  easein 0.5 rotate 2 yoffset -100

label start:
  jump a1_s1_comic_panels

