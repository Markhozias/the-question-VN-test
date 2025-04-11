# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform top_middle:
  xalign 0.5
  yalign 0.2
  zoom 2.0

transform right_middle:

    xalign 2
    yalign 0.5
    zoom 1.5



default WorePajamas = False

default form = "Zoroark"

default size = "tall"

default name = "Lucas"

default age = "24"

default gender = ""

default ID_name = ""

default ID_age = "16"

default ID_species = ""

default ID_gender = ""

default ID_grade = "11th"

default ID_number = ""

define C = Character("Clippy")

define Le = Character("Letter")

define J = Character("Janitor")

define Lu = Character("Lucas")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene pcondefault
    with fade

    show clippy at top_middle

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show makes avatars appear

    # These display lines of dialogue.

    C "Welcome back, Lucas!"

    menu:

        C "You have new messages in your inbox!"

        "check inbox":
        
            jump checkingemails1

        "i'd rather sleep":

            jump choosehowtosleep

    label choosehowtosleep:

    scene black
    with fade

    menu:

        "go to sleep right now":
            $ WorePajamas = False
            jump badendingbedroom

        "get ready first":
            $ WorePajamas = True
            jump badendingbedroom 

    label badendingbedroom:

    scene black

    if WorePajamas:
        "you wear your pajamas neatly"

        "and lay down protected from the cold"
    else:
        "you go to sleep right now"

        "naked and all"

        "the cold haunts you all night"

    "You go to sleep and do nothing"

    "."    

    ". ."

    ". . ."
 
    "A morning you wake up to a letter on your inbox"

    Le "your rent is due, you are going to the streets"

    "congrats on doing NOTHING Lucas"

    return

    label checkingemails1: 

    scene pconzetflix

    C "click when you want to exit"

    menu:

        "next e-mail":
            jump checkingemails2

    label checkingemails2: 

    scene pconspam

    C "click when you want to exit"

    menu:

        "go back":
            jump checkingemails1

        "next e-mail":
            jump checkingemails3

    label checkingemails3: 

    scene pconschool

    C "click when you want to exit"

    menu:

        "go back":
            jump checkingemails2

        "go out":
            jump appearancechoice
    
    label appearancechoice:

        scene black
        with fade

        "just as you get up to get ready"

        "you look at the mirror and see yourself"

        scene black
        
        "you surely look older than a 16 years old, don't you?"

        "maybe you could change up a bit?"

        "no hardie for a grown Zoroark, is it?"

        menu:

            "use an illusion to look younger":
                $ size = "small"
                $ form = "Zorua"
                jump zoruatf

            "no need to hide":
                jump firstschooldayentrance

    label zoruatf:

        "infront of the mirror you see no other than you"

        "using your mind, your body is covered in a purple glow"

        "your body contorts, getting smaller, and all of a sudden"

        "you look like you but 8 years younger"

        "a zorua"

        "and while not the best, your extra height turned into fluff"

        "YOU ARE A ZORUA FLUFFBALL"

        "time to go?"

        menu:

            "yeah, time to go":
                jump firstschooldayentrance

            "nah, i don't need to go to school":
                jump badendingbedroom

    label firstschooldayentrance:

        "the sun is shining"

        "cuties are walking the streets"

        "but as you enter, a school officer stops you and says"

        show janitor at right_middle

        J "i see no ID"

        if size == "small":

            J "do you have your student ID with you?"

            $ renpy.save('hidden_save') #Force save in a slot named 'hidden_save'

            menu:

                "yeah, i totally do":
                    jump noyoudont1

                "no, i don't":
                    jump idmaking

        if size == "tall":

            J "You look grown"

            J "don't get too close to the kids" 

            jump schoolhalls

    label noyoudont1:

        "no, you don't"
        
        $ renpy.load('hidden_save')

    label idmaking:

        "you are scorted to a office deep into the halls"

        "the yellow walls have a kind of smell"

        "a bad smell that is but still a smell"

        scene black

        "as you reach the office, you are met by a tall spruce door"

        "the handle glisting a cold metallic handle"

        "the janitor walks off, saying to you before leaving"

        J "just talk with her"

        J "she loves new students"

        J "i bet she will love you too"


    # This ends the game.

    return
