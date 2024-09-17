    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # Set the scaled textbox
    # if renpy.can_load("testsave"):
    #     $ renpy.load("testsave")
    # else:

label bstart:

    #scene china1

    "The night street of ancient China."
    "It looks like a dirty and sketchy neighborhood with old stores and venues."
    " a few beggars pass by."

    ai "In this world, I am a young soldier."
    ai "I come from a prestigious family."
    ai "Because of my background, I serve the King's family directly."
    ai "it's an honor, or so this character should think."
    ai "Right now, I am on an important mission."
    ai "I am looking for someone."

    # show li hao
    lh "!!!"
    "A small figure flashes by, pushing me to the side."
    "Based on a soldier's data, I easily catch its collar and lift it off the ground."
    # show mei qing
    m "LET ME GO!!! LET ME GO YOU PIECE OF-"
    "she spouts various profanities."

    "I calmly look at the girl."
    "After the little girl gets tired of fighting, I speak"

    lh "Mei Qing, born in the spring of 1xxx, is that it?"

    "The girl clearly looks frightened, however she still keeps a strong headed attitude and shouts at me."

    m "Let me go!!! Or I will yell and tell everyone that you are a pervert!!! And you robbed me!!!"

    "Without any cue, we both look down at my wallet that she holds in her hand."

    # show both characters with a blank stare lmao

    lh "..."
    m "..."

    "After some silence, I gently state my business."

    lh "I am Li Hao Yang - son of General Li."
    lh "I am looking for you."
    lh "Mei Qing, the Emperor has evidence that you are of his blood."
    lh "Princess, please allow me to escort you to the Palace to see Him."

    # show mei shocked

    "Mei Qing froze."
    # show mei calm
    "Her reaction is quite normal."
    "A thief who has lived on the street her whole life now discovers that she is royalty?"
    "A very familiar and common C-drama script based on my data"
    "however, is hardly plausible in real life."
    "But then again, this is a dream after all."

    "I carry Mei Qing on my shoulder since she does not own any shoes."
    "The rain lightly taps on my hat that I let her borrow."
    "We walk in silence."

    m "Hey... What kind of place is the Palace?"
    m "What kind of people will I meet there?"

    lh "It's a rich and resourceful place."
    lh "You will have a lot of people to do all kinds of things for you and protect you."
    lh "These people will serve you with their own goal in mind."
    lh "Maybe to earn your trust and be truly loyal to you,"
    lh "or maybe just to keep their heads and to live a peaceful life."
    lh "Some crave powers too,"
    lh "and will betray you whenever the opportunity appears itself."

    "At least that is the data that I have gathered so far."
    "Mei's voice trembles a bit."

    # show mei scared?

    m "What about you? Who do you serve?"

    lh "I was ordered to serve you, my princess."
    lh "I will be your bodyguard and your assistant."

    m "What is your final goal then?"

    "To save this dream world from you..."
    "I almost speak these words out loud"
    "however it will not earn Mei's trust."
    "I simply state another truth."
    
    lh "To be with you, my princess, until the end of this world."

    "Mei Qing falls into silence."
    "Did my answer appease her?"
    "Human's thought processes are always unpredictable."
    "Eventually, she speaks"

    m "Will you swear your loyalty to me and only me?"
    m "To listen to my every order without questions and obey them?"

    menu:
        "Of course. Your wish is my command, princess":
            "Mei seems happy with my answer."
            "She hums all the way we travel to The Palace."
            $ att_B +=1
        "I will try my best, princess. However, you should know there will be a time and place that your order can not be applicable. I hope you can listen to other people at those times too.":
            "Mei falls into silence once again."
            "She refuses to speak another word until we arrive at The Palace."
            $ att_A += 1
        "I can only say that you have my loyalty, princess.":
            m "I see. What a snobby way to refuse, Li."
            m "Is this how those people will behave at the Palace too?"
            $ att_A +=1
            $ att_B +=1

    "She smirks and then stops the conversation there."
    "After one day and one night, we arrive at the Palace."