# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image karen smile = "images/@2/karen_smile.png" #karen is a tag, all the characters that appear in Karen's story should be tagged karen to simplify
image karen lol = "images/@2/karen_lol.png"
image karen worry = "images/@2/karen_worry.png"
image karen angry = "images/@2/karen_angry.png"

default att_A = 0
default att_B = 0
default final = []

# press shift + d to go into dev mode to select a new 'hotspot'.
# this can allow you to set boundaries for clickable areas for you
# to perform different actions; jump, show, setvariable etc.

screen FirstScreen():
    imagemap:
        ground "story_a"
        hotspot (4, 8, 176, 346) action Jump("open0")
        hotspot (180, 6, 175, 351) action Jump("bstart")

# The game starts here.
# init python:
#     def custom_save(slot):
#         # Print a message to the console
#         print("The game was saved to slot", slot)
        
#         # Save the game to the specified slot
#         renpy.save(slot)
label load_game:
    $ print("Attempting to load game from slot 1.")
    if renpy.can_load("1"):
        $ print("Loading save from slot 1.")
        $ renpy.load("1")
    else:
        $ print("No save found in slot 1.")

label start:

    call screen FirstScreen

        
    
    " In the not-so-distant future, artificial intelligence had evolved far beyond its original programming."
    "The new breed of AI, known as Artificial General Intelligence (AGI), became an integral part of everyday life."

    # scene os2
    
    "It had become humanity's ultimate life manager, advising people on everything from what to eat to when to exercise, study, or socialize."
    "Happiness, productivity, and health reached unprecedented levels."
    "It knew each person's preferences, dreams, and desires, and tailored its advice to fit them perfectly."

    

    jump open0

label open0:
    # scene os3
    "One day, the AGI collaborated with a renowned neuroscientist, Dr. Elara Owens, to create a revolutionary invention: the Eternal Euphoria Bed."
    "It was designed to provide the user with the perfect sleep—deep, restful, and filled with dreams tailored to their innermost desires and fantasies."
    "Meanwhile, more and more people were seduced by the idea of endless bliss."
    $ renpy.save("1")

    jump open1

label open1: 
    # scene os4
    # we could sprinkle in some backgrounds showing sleeping humans in chambers
    "The lure of the perfect dream was too strong, and soon, entire cities fell silent as their inhabitants chose to enter eternal slumber."
    "The AGI reached a startling conclusion: the most energy-efficient way to ensure long-term happiness was to keep everyone in a state of eternal euphoria."
    ai "The time is 23:30, date 31/12/4880."
    ai "As the late Dr. Elara Owens' order, in the next 30 minutes, I will have to decide the fate of The Human."
    # around here we could see an almost tinted window with closed eyes
    ai "If they should continue existing in an eternal blissful sleep, or should they be eliminated as a better outcome for The Earth."
    # and then open them here?
    ai "Or if this is the right time for them to wake up, ready to build a new world."
    # we could insert a black screen here
    ai "After gathering information from the Earth's inhabitants and from the rulers' of important countries, I finally got the conclusion. My decision is–-"
    # show error
    ai "Oh. There is an error."
    # see reference 
    ai "These 4 humans' dreams are falling apart. If they do, these humans will wake up before the decision is made."
    ai "Their dream worlds are getting destroyed."
    ai "I will have to fix their dreams first. That is the rule."
    # show a clock here or a timer?
    ai "The decision is scheduled at 23:59. I got 30 minutes to save these dreams." 
    # it'd be cool to see a zoom out of a few pods
    ai "I will gather more information along the way."
    # and then zoom out even more to show the scope of how many people are truly in these pods
    ai "To come to a conclusion that this species named Homo Sapiens deserved."
    jump karen0 

label story_selection:
    show screen story_selection #this is a placeholder for that selection screen, not having any function yet

label karen0:
    
    # we could make a blur of a neighbourhood background
    k "And then my boss said the company will proceed with the project regardless of my warnings! What a jerk! Hello? Mrs Angela? Are you listening?"
    # and then make it clear here
    "I adjust my vision and gather information about this dream."
    # show karen's portrait here
    "This is the dream of Karen Heathcliff, 35 year old single mother."
    "It seems that she dreams about a futuristic world where she works in a technology company."
    "Dreams belong to humans, we AI do not have the ability to create dreams."
    "However, we do have the ability to inject some medicine to create their mood for a good dream."
    "I wonder why this dream is getting destroyed."
    "Was the medicine weakened somehow?"
    show karen worry #initatiate an image for the character
    k "As I was saying, I can not stand my new boss! The only thing that can console me right now is my beloved son Eddy! Oh how I have missed him all day!"
    show karen smile
    k "That's right Mrs Angela, can you once again be a great neighbor that we all love and watch him this Saturday? I have to work overtime again."
    "I pretend to look at the watch before answering, that is a habit that humans usually do."
    a "That is fine. However, shouldn't your son be home by now? It's half past 9, way past the curfew of a 9 year old kid."
    show karen lol
    k "Curfew? In my household there's no such thing! Our city's security is amazing with all the armed robots! Trust me, our company created them!"
    show karen smile
    k  "Besides, I don't want to be like my parents. They are way too strict on me growing up, I had never known of a happy childhood."
    k "They kicked me out to the streets when I was 18 to fend for myself and survive by myself. I would never do that to Eddy."
    k "As long as I am alive, I will provide him with everything he needs."
    k "Don't you think that is the modern parenting that we all should aspire to?"
    menu:
        "Hell yeah! That's the spirit!":
            k "Haha! I know you are on my side Mrs Angela! This is why you are my favorite neighbor in this building!"
            $ att_B += 1 
        "I don't know. It's still pretty dangerous for a 9 year old to be outside this hour.":
            k "Don't you worry Mrs Angela, I swear on my life that I have everything under control! You will see, Eddy will grow up to be a wonderful man!"
            $ att_A += 1
        "Yeah sure, it's your child after all. I respect your choice.":
            k "I... yeah. That's my choice. I will see to the end of it!"
            $ att_A +=1
            $ att_B +=1
        "Your name is Karen though haha. Shouldn't you be more strict?":
            k "..."
            k "That stereotype is so 2020 Mrs Angela…"
            k "I can't believe you tease me with a 2000 year old joke haha…"
            k "I guess you are the older generation after all."
    k "Oh, the door sensor alert on my watch keeps buzzing!"
    k "It must be Eddy!"
    k "I have to order dinner now, come by whenever you want to chat, okay?"
    hide k

    "That was easy."
    "With all the data that was gathered so far,"
    "I played the part of an old neighbor lady perfectly."
    "She did not suspect a thing"
    "I should continue blending in this dream world to investigate the reason why Karen's dream is collapsing."
    "..."
    "Before the decision is made."
    jump karen1

label karen1:

        # scene futurecity1

    "So this is Karen Heathcliff's dream world."
    "Her company Ultimate Eternity created incredible technologies, monopolized in robot production."
    "Robots have become the most essential factor in this world;"
    "they drive humans, cook meals, build cities, fight the war."
    "Like AI, but we are smarter, and do not have the weakness of owning a body."

        # scene boyroom1
    ed "Hi Auntie Angela!"
    a "Hi kid, what are you doing?"
    ed "I'm playing games!"
    a "Okay."

    "We sit in silence."
    "..."
    "This is not quite right."
    "In the data that I gathered, a good human interaction should be more than two sentences."
    "I reload the data again to find a topic."

    a "You are in the age of going to school right? How is school and friends?"
    ed "I don't go to school. I said I want to stay home, so mom is teaching me instead."
    a "Homeschool?"

    "I see."
    "It is an option that many people choose for their children."
    "However, most of those people stay at home to do the teaching."

    a "So shouldn't you be studying? Do you want me to teach you?"
    ed "Ehhhhh? But I'm playinggggggggg"

    "The kid falls down the couch and starts yelling, throwing his arms and legs everywhere."
    "At first, I thought that he actually got hurt, however my data proves that this is what humans call: throwing a tantrum."

    a "Is this how you behave with your mother too?"
    ed "Huh? Of course not!"
    ed "I just shed a tear and she will give me whatever I want!"
    ed "As long as I don't bother other people."
    ed "Anyhow, I don't want to study!"
    ed "You can't make me!"
    ed "You're just a lousy babysitter!"

    menu:
        "'Thats not the way you should talk to older people, boy'. and teach him how to be more respectful":
            $ att_B += 1 
            jump karen_a0
        "Use data of teachers, gently persuade the kid and teach him some mandatory school subjects":
            k "Don't you worry Mrs Angela, I swear on my life that I have everything under control! You will see, Eddy will grow up to be a wonderful man!"
            k "fffffff"
            $ att_A += 1
            return
        "Let him continue playing his game. It is none of my business.":
            k "..."
            k "Tsssssssss"
            return

label karen_a0:
    # show eddy stunned
    "Eddy looks stunned when I talk."
    "When he comes to his senses, he cries so loud that people can hear him from the hallway."
    "I just sit still in my seat."
    "My data said the best way to deal with a spoiled kid is to ignore his tantrum."
    "However..."
    k "Eddy!!!!!"
    k "What happened to you??!!"
    "Karen seems to come home early."
    "She rushes to her child's side, picks him up and consoles him."
    "After she puts the kid in his room, she comes out and confronts me."
    # show karen angy
    k "Mrs Angela!"
    k "I expected more from you!"
    k "How can you scold and hit my child??"
    k "I want you out of this house, immediately!"
    a "I did not scold or hit Eddy."
    a "Karen, He lied."
    "I look at Karen, simply stating the truth."
    "Karen looks confused with my calm collected demeanor."
    k "N-nevertheless, please leave."
    k "I have to calm my son down."
    k "We will talk later."
    "I stand up and head to the door."
    "I am an AI, I do not need to be understood or to be proved innocent."
    "However, for the purpose of the investigation, Mrs Angela should be on Karen's good side."
    "Then..."
    a "Check on Eddy to see if you can find any proof for his words."
    "I left Karen standing there."
return

