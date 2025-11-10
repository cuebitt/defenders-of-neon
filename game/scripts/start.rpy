# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # Jump to a label.

    e "This next section should unlock music!"

    e "Here's Pachelbel's Canon."

    play music "audio/bgm/canon-in-d-pachelbel.ogg"

    e "Now, here's Tarrega's Gran Vals."

    play music "audio/bgm/gran-vals-francisco-tarrega.ogg"

    e "Finally, here's Gymnopédie no. 1 by Erik Satie."

    play music "audio/bgm/gymnopedie-1-erik-satie.ogg"
    
    e "These songs should now be unlocked in the music room!"

    jump end
