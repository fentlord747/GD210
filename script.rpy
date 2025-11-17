# Bussy Studio V1 - Ren'Py Conversion (Plain text-only)
# Converted from Twine/Harlowe - plain Ren'Py dialog & choices

define lucas = Character("Lucas Rivera", color="#5ca0ff")
define mc = Character("You", color="#ffd966")
define narrator = Character(None)

label start:
    scene black
    with fade

    lucas "Lucas Rivera in his bus driver outfit looks over to you. Being friends with him since childhood, he looks to you holding the radio."

    menu:
        "Tune left":
            jump tune_left
        "Tune right":
            jump tune_right

label tune_left:
    narrator "The radio crackles less. Slowly turning the dial, a voice comes in clear."
    narrator "\"ATTENTION ATTENTION ALL LIVING AND CONSCIOUS NEW YORKERS, A SAFE LOCATION HAS BEEN SECURED IN VAN CORTLANDT PARK. THERE IS FOOD, SHELTER, AND WATER.\""

    menu:
        "We have to check it out":
            jump check_it_out
        "Think it's real?":
            jump think_its_real

label tune_right:
    narrator "Slowly moving the knob right, a voice can barely be heard over the already spotty sound of the radio."
    narrator "\"ATTENTION ----- ALL ---- NEW YOR --- SAFE LOC--- HAS BEEN SECURED IN VAN CORT  ----- ARK. THERE IS ---- SHEL -------\""

    lucas "van cortlandt? that's mad deep. you think it's real?"

    menu:
        "Of course":
            jump of_course
        "Wait it out":
            jump wait_it_out

label of_course:
    mc "They have to be. There is no way they'd be stupid enough to not be deadass about this."

    lucas "i don't know man they could be. what if they do what they do in those movies where they like bomb big places."

    menu:
        "No dude we should go":
            jump no_dude_we_should_go
        "Wait it out":
            jump wait_it_out

label no_dude_we_should_go:
    narrator "He looks at you and takes a deep breath. Anger hinting at you behind his eyes."

    lucas "alright whatever. your decision."

    return

label wait_it_out:
    narrator "With a sigh, you think for a second. Together you could be doing so much more, getting somewhere better or at least a head start to something new."

    menu:
        "Ask again":
            jump ask_again
        "Listen and wait":
            jump listen_and_wait

label ask_again:
    mc "\"you positive we should wait it out? you're not curious like at all? bro we haven't heard anything in the past two years. we could be out of this shit.\""

    mc "\"i think we should wait it out. we just don't know. let's sleep on it.\""

    menu:
        "Listen and wait":
            jump listen_and_wait
        "Try again":
            jump try_again

label listen_and_wait:
    narrator "The sun slowly descending in the background, Lucas boarding up the doors and secondary exits. Focused on your tasks, you divide up the rations you both have managed to save. Somewhat low but not like it wouldn't last a couple of days. Between the both of you, there is definitely food for a night or two."

    menu:
        "Talk to Lucas":
            jump talk_to_lucas
        "Sleep off the night":
            jump sleep_off_the_night

label try_again:
    mc "\"come on lucas. This could be our last chance at this thing. We could use this. i know we're not too hot on fuel but we can pick some up on the way easy. You never know. this could be real. I say we do this.\""

    narrator "With baited breath he sighs..."

    lucas "alright you got me. let's just be quick."

    return

label talk_to_lucas:
    narrator "You sit beside where his booth is. He's settled and looking forward, avoiding eye contact with you."

    lucas "\"we're not doing too good on fuel. We stop for gas every day. I don't mean to be all nervous but we can't be making rash decisions all the time. I wanna be on the safe side, not get us into trouble. If we see anyone you think is chill, we can bring them on... but it'll be on you if they fuck us up.\""

    menu:
        "we'll be good":
            jump well_be_good
        "no promises":
            jump no_promises

label sleep_off_the_night:
    lucas "With the windows and doors closed off, Lucas sets up in his chair, he gives you an okay and fully turns off the bus."
    narrator "You lay next to the rations, a wave of dread looming over you as the divets in the seats dig into your side. Is this a good idea?"

    menu:
        "Wake up":
            jump wake_up_after_night

label well_be_good:
    narrator "He shakes his head side to side with his arms already crossed. Leaning back in his chair and placing his cap over his face, a big exhale before a soft snore emits from him."

    menu:
        "check rations":
            jump check_rations
        "sleep":
            jump sleep

label no_promises:
    lucas "\"when is there ever.\""

    narrator "Leaning back in his chair and placing his cap over his face, he settles in for the night. Soft snores emit from him. Now alone with your thoughts, what could you do?"

    menu:
        "sleep":
            jump sleep
        "check rations":
            jump check_rations

label wake_up_after_night:
    narrator "The alarm vibrates as it sits on top of you, the speakers that were taken out and kept for maybe something later on. Lucas is setting up a bag for the day and eating the first half of his can for the day."

    lucas "Thanks for letting me sleep on it. I don't trust a lot but I trust you more than what is going on out there. So lets do this. Van Cortlandt. We can stop along the way for gas and food and maybe we come across other survivors. Just be smart about this."

    menu:
        "Lets get started":
            jump lets_get_started
        "Lets stop for any food we can find":
            jump stop_for_food

label check_rations:
    narrator "In the back, a small bodega crate sits in front of you, tied down to the seat and a makeshift cover made of cut up pallet planks on top accompanied by a lock. Pulling out the key from a hidden compartment in the air vent of the bus, you open it."

    narrator "4 cans. That could either last you 2 days. There's food to spare for now."

    menu:
        "sleep":
            jump sleep

label sleep:
    narrator "Finally resting in your usual spot in the back of the bus by the rations, you lay for a second, the divots in the seats uncomfortable against your back but you've been getting used to it."
    mc "We just have to make it there."

    menu:
        "wake up":
            jump wake_up

label wake_up:
    narrator "The alarm set beside you vibrates, you had taken out the speaker long ago in the beginning. Eyes slightly blurry, you rub them and make your vision clear. You look over to Lucas who is preparing a bag for the day. Eating the first half of his can of the day."

    lucas "So you ready for this? We have a day ahead of us."

    menu:
        "Yeah lets get to it":
            jump yeah_lets_get_to_it
        "Should we check outside before we start?":
            jump check_outside_before_start

label yeah_lets_get_to_it:
    jump lets_get_started

label check_outside_before_start:
    narrator "You consider checking outside before driving off."

    menu:
        "Check outside":
            jump check_outside  # placeholder: not present in Twine snippet
        "Go anyway":
            jump lets_get_started

label lets_get_started:
    narrator "You both prepare and head out to follow the radio tip."

    menu:
        "Go":
            jump go_from_bus
        "Stop and check bag for gear":
            jump check_bag

label stop_for_food:
    lucas "\"Yeah we should. Good thinking. There's a corner store around. Your gas mask any good?\""

    mc "\"I'm all good don't worry about me. Yours good?\""

    lucas "\"I'm good. Got anything you wanna bring?\""

    menu:
        "check bag":
            jump check_bag
        "Go":
            jump go_from_bus

label check_bag:
    narrator "In your bag you have:\n---\nFlashlight\nLighter\nSmall Pocket Knife\nOld apartment keys"

    menu:
        "Grab a machete":
            jump grab_machete
        "Grab a baseball bat":
            jump grab_baseball_bat

label grab_baseball_bat:
    jump go_from_bus

label grab_machete:
    jump go_from_bus

label go_from_bus:
    narrator "Lucas looks at you, an eyebrow raised."

    lucas "Alright then, I'll watch your back."

    narrator "Both of you equipping your masks, Lucas unlocks the door of the bus and takes down the sheet that covers the windows of the door. Light shines through. Stepping down, the noise of the gas mask loud in your ear, you check the surrounding area. Off in the distance you see two corner stores. One 4 blocks away and in direct sunlight, the other is closer and blocked by a building in the shade."

    return

# Some short/empty passages from Twine were present (likely linking anchors).
# We'll include minimal labels as placeholders so jumps won't error if referenced.

label check_it_out:
    # Corresponds to "We have to check it out" passage - content missing from snippet; placeholder.
    narrator "You decide to check it out. (passage content from Twine not fully provided.)"
    return

label think_its_real:
    narrator "You question whether it's real. (passage content not fully provided.)"
    return

label try_again_end:
    narrator "You try again. (placeholder)"
    return

label check_outside:
    narrator "You check the outside area carefully. (placeholder - add details later.)"
    return

# Additional placeholder labels for any empty/unused Twine passages
label wake_up_after:
    narrator "(placeholder)"
    return

label we_out:
    narrator "(placeholder)"
    return

label i_dont_know:
    narrator "(placeholder)"
    return

# End of script

