transform up_lean:
  # Move the sprite slightly upward
  yoffset 0
  rotate 0
  rotate_pad True
  transform_anchor True
  subpixel True

  # Rotate by 5 degrees clockwise and up 150 px
  easein 0.5 rotate 5 yoffset -150

label start:
  jump a1_s1_comic_panels

