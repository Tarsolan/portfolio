# Intro to Python - Challenge Week 1
# Author - Alex Ridgeley
# Date - October 4th, 2021
# Objective - Challenge myself, so I will try to create a short game

# Constants

# Input
player_name = input("Enter a first name for your character: ").title()

# Processing

# Output
print()
print(f"THE TRIAL OF GREED")
input(f"The vast majority of text will be advanced by pressing the 'ENTER' key.\n"
      f"Press ENTER to continue, {player_name}. ")
print("Good! Let's begin.")
input()
input("It’s a beautiful, sunny day. You’re walking in the woods with your friends, Degren and Auron,\n"
      "when you stumble across something… odd.")
print()
input("It’s a small path, leading off the main trail. You're sure it wasn't there before.")
input("“That’s a little odd.” Degren says, matter of factly. “I’m pretty curious about what’s down there.”")
print()
input("Auron chimes in, saying: “Are you sure, my friend?“\n"
      "“All sorts of danger could be waiting for us off the path, and we’ve got places to be.”")
print()
input("Hmm...")
input(f"They both look to you, clearly seeking the tie-breaking vote.\n"
      f"“What do you think, {player_name}?” Degren says. “Should we check it out?”")
while True:
    story_begin_question = input("You pause for a moment and consider the question.\n"
                                 "You do have places to be, but you're just so curious.\n"
                                 "\n"
                                 "Will you check it out? (Y/N) ").upper()
    if story_begin_question == "N":
        input("You shake your head. You’ve all got business waiting for you in town, and it’d be best to move on.\n"
              "“Well, alright.” Degren sighs, a little disappointed. “Let’s keep going to town, then.”")
        input("You enjoy a pleasant walk into town in the company of your friends, and all is well.\n"
              "Sometimes, when you let your mind wander, you can’t help but wonder what might’ve been down that path…")
        print()
        input("END OF GAME")
        quit()
    elif story_begin_question == "Y":
        break
    else:
        print("Invalid Choice. Please enter either 'Y' or 'N'")
        print()
print()
input("You nod, and motion to the others to head down the path.\n"
      "“Alright, alright.” Auron says, with a slight smile on his face. “Let’s check it out.”")
print()
input("You move down the path, one at a time. The forest darkens slightly as the trees covering\n"
      "the sky become increasingly dense. You press on.")
print()
input("After about an hour, you come to a small clearing at the base of a hill.\n"
      "Built into the side of this hill, there is a set of stairs. \n"
      "You spy what appears to be some kind of entrance at the end of the stairs… a cave, perhaps?\n"
      "It’s hard to tell without getting closer.")
print()
input("Degren speaks with his usual tone of confidence, “Well, we’ve come this far.\n"
      "Might as well see if anyone’s home.” He begins to head up the steps, followed by you and Auron.")

# PART 1 - THE DOOR
door_check = False
keyhole_check = False
doorknob_check = False
print()
input("The three of you come to a door at the top of the stairs. It looked simple at first,\n"
      "but upon inspection, it is surprisingly intricate. There are engravings in the center,\n"
      "and some kind of glowing rune hovers over the doorknob.")
print()
input("Degren attempts to open the door, but the moment his hand touches the rune, he recoils in shock. \n"
      "“Ouch! That hurt!” He exclaims. “It seems like whoever is here doesn’t want us coming in that easily.”")
print()
input("“I don’t like this.” Auron says. “This place gives me some bad vibes – whoever made\n"
      "this place is probably bad news.” His face turns to a scowl. \n"
      "“Still, it might be best if we get inside and make sure nothing bad is happening.”")
print()
input(f"Degren nods. “Anyone with the power to lock a door magically like this could be trouble.” \n"
      f"He looks to you. “{player_name}, you seem like a smart cookie. How about you take point on this mission?”")
print()
input("You sigh. But, you are the newbie. Might as well take this opportunity to prove yourself.")
print()
input("You step forward, taking a closer look at the door. There are a few areas that strike you as interesting.")
input("First, the engraving in the center of the door.")
input("Second, there seems to be some kind of keyhole right above the doorknob.")
input("Third, the rune on the door knob itself.")
print()
while True:
    if door_check is True and doorknob_check is True and keyhole_check is True:
        print("Hmm... there seems to be something else. Another engraving on the frame\n"
              "of the door itself?")
        print()
        examine_door_question = input("Which will you look at? (1, 2, 3, 4)\n"
                                      "1. Engravings\n"
                                      "2. Keyhole\n"
                                      "3. Door Knob\n"
                                      "4. Door Frame\n"
                                      "")
    else:
        examine_door_question = input("Which will you look at? (1, 2, 3)\n"
                                      "1. Engravings\n"
                                      "2. Keyhole\n"
                                      "3. Door Knob\n"
                                      "")
    if examine_door_question == "1":
        door_check = True
        print()
        print("You take a closer look at the engraving on the center of the door. It’s definitely \n"
              "a language you understand, but it’s faded. It seems to say… “speak the answer here, \n"
              "and you shall be granted entry.” How odd.")
        print()
        examine_door_detail = input("What will you do?\n"
                                    "1. Speak an answer.\n"
                                    "2. Go back.\n"
                                    "")
        if examine_door_detail == "2":
            input("You step away from the door. Perhaps you'll come back to it in a moment.")
            print()
            continue
        if examine_door_detail == "1":
            door_answer = input("Alright. This is it. Let's do this.\n"
                                "Enter your answer to the question: ").lower()
            if door_answer == "a coin" or door_answer == "coin" or door_answer == "coins":
                break
            else:
                print()
                input("You wait for a while after speaking the words, but nothing happens.\n"
                      "Slightly disappointed, you back away.")
                continue
    elif examine_door_question == "2":
        keyhole_check = True
        while True:
            input("You take a closer look at the key hole. It almost looks ordinary,\n"
                  "but it's not shaped to receive any kind of key you've ever \n"
                  "seen before.")
            print()
            input("There's not much more you can do here. Better focus on the \n"
                  "rest of the door.")
            print()
            break
    elif examine_door_question == "3":
        doorknob_check = True
        input("The rune glows a faint gold, and holds the shape of a seven-pointed star.\n"
              "Going in for a closer look, it almost reminds you of a type of\n"
              "ancient currency you’ve read about before.")
        print()
        rune_examine_question = input("What will you do?\n"
                                      "1. Touch the rune\n"
                                      "2. Back away\n"
                                      "")
        if rune_examine_question == "1":
            input("You feel a shock take hold of your body. It hurts, and your mind is filled with\n"
                  "a very brief flash of a strong desire for wealth.")
            print()
            input("You pull away instinctively. Degren laughs and says \n"
                  "“Now, you just saw me do that a moment ago. Did you think it was\n"
                  "going to be any different for you, newbie?”")
            print()
            input("You feel a little silly, and back away from the rune.")
            print()
            continue
        if rune_examine_question == "2":
            input("Remembering what happened to Degren when he tried to touch the rune,\n"
                  "you decide it might be best to just turn away for now, and look at something\n"
                  "else.")
            continue
    elif examine_door_question == "4" and door_check is True and doorknob_check is True and keyhole_check is True:
        input("The engraving on the frame of the door is far less degraded. \n"
              "You can make out nearly the entire script.")
        print()
        input("It reads “What has a head and a tail, but no body?”")
        input("... really? A simple riddle? That's it?")
        print()
        input("Auron speaks up “Well, I guess that explains how to get in. \n"
              "We just solve the riddle and speak the answer, right?”")
        print()
        input("You nod. Let’s see what happens.")
        print()
        continue
    else:
        input("Invalid selection. Please try again.")
        print()
        continue
input("You hear a hissing sound, followed by a distinct 'click'. The place where the keyhole was is now filled\n"
      "with a strange, gold liquid.")
print()
input("Moments pass, and then the door moves open.")
input(f"“Well, {player_name}, I guess we're in. Let's see if anyone's home.“ Auron says. You head in.")
print()
input("The three of you move into the structure. The inside is much more... lavish\n"
      "than you had first expected.")
print()
input("It is very large, and very bright, with a lot of gold-inlaid banners\n"
      "draped from the walls. You appear to be in a kind of great hall.")
print()
input("“My word…” Degren says. “I had no idea a place like this could exist \n"
      "so close to town without anyone knowing about it. I doubt that \n"
      "simple riddle could have kept everyone out.”")
print()
input("“Definitely not. I think it’s more likely that we saw this place \n"
      "because whoever lives here wanted us to come here.” Auron says in response.\n"
      "“Maybe they're showing off to us.“")
print()
input("As you move through the great hall, a large table catches your eye. \n"
      "The table seems to hold a large device of some sort, with a piece of \n"
      "paper and some writing utensils laid out in front.")
print()
input("A wire comes out of the device. You follow it with your eyes, and see \n"
      "that it connects to the door at the other end of the great hall.")
print()
input("You point this out to Degren. “If I were a betting man - which, I am -” he says, \n"
      "“that’s a device that can unlock the door up ahead.”")
print()
input("Auron agrees. “You two check out that device. I’ll head over\n"
      "to the door and see what’s up.”")
input("He walks ahead, towards the door.")
print()
input("Coming closer to the device, you can see that it’s a large box. \n"
      "It has a small opening on the top labeled “INPUT” and a small \n"
      "opening on the bottom labeled “OUTPUT”. Each is about big enough to hold a piece of paper.")
print()
input("The paper on the table seems to be filled with… numbers. \n"
      "You recognize this. This is math.")
print()
input("You roll your eyes. It can’t be.")
print()
input("Degren notices your despair, and comments. “… it looks like we have to solve the math problems on the paper,\n"
      "then feed our answers into this device. That might unlock the door? Disgusting.”")
print()
input("Each of you sigh. But you’ve come this far, so you might as well take\n"
      "a look at what horrors await on the page.")
print()

# PART II - THE MATH
question_1_print = "INCORRECT"
question_2_print = "INCORRECT"
question_3_print = "INCORRECT"
question_4_print = "INCORRECT"
question_5_print = "INCORRECT"
question_6_print = "INCORRECT"
question_7_print = "INCORRECT"
question_8_print = "INCORRECT"
question_9_print = "INCORRECT"
question_10_print = "INCORRECT"
question_1_answer = "Not Yet Attempted"
question_2_answer = "Not Yet Attempted"
question_3_answer = "Not Yet Attempted"
question_4_answer = "Not Yet Attempted"
question_5_answer = "Not Yet Attempted"
question_6_answer = "Not Yet Attempted"
question_7_answer = "Not Yet Attempted"
question_8_answer = "Not Yet Attempted"
question_9_answer = "Not Yet Attempted"
question_10_answer = "Not Yet Attempted"
while True:
    question_select = input("\n"
                            "... Okay, FINE. Which question?\n"
                            "0.  You're done. Place the paper in the machine.\n"
                            f"1.  Question 1  ({question_1_answer})\n"
                            f"2.  Question 2  ({question_2_answer})\n"
                            f"3.  Question 3  ({question_3_answer})\n"
                            f"4.  Question 4  ({question_4_answer})\n"
                            f"5.  Question 5  ({question_5_answer})\n"
                            f"6.  Question 6  ({question_6_answer})\n"
                            f"7.  Question 7  ({question_7_answer})\n"
                            f"8.  Question 8  ({question_8_answer})\n"
                            f"9.  Question 9  ({question_9_answer})\n"
                            f"10. Question 10 ({question_10_answer})\n")
    if question_select == "1":
        print("Question 1: 15*2/3+15*2/10-15*2/6")
        question_1_answer = float(input("Answer: "))
        if question_1_answer == 8:
            question_1_print = "CORRECT"
        continue
    elif question_select == "2":
        print("Question 2: 4*10/(3+5)^2*2-15/3")
        question_2_answer = float(input("Answer: "))
        if question_2_answer == -3.75:
            question_2_print = "CORRECT"
        continue
    elif question_select == "3":
        print("Question 3: (5*5-25/5)+12-4+5+(9-3*2)^2")
        question_3_answer = float(input("Answer: "))
        if question_3_answer == 42:
            question_3_print = "CORRECT"
        continue
    elif question_select == "4":
        print("Question 4: (10*4-6+7-8/2+3*3+(4+5-6/3)+1)/2")
        question_4_answer = float(input("Answer: "))
        if question_4_answer == 27:
            question_4_print = "CORRECT"
        continue
    elif question_select == "5":
        print("Question 5: ((3+4-6/2+2)+((9/3+6*5)/11))*((4+5-6)+(18-3*4))/9")
        question_5_answer = float(input("Answer: "))
        if question_5_answer == 9:
            question_5_print = "CORRECT"
        continue
    elif question_select == "6":
        print("Question 6: Tom divided $360 among his six children for them to use for \n"
              "            holiday gifts. His daughter Kate added $20 to her portion, then used \n"
              "            the money to buy 16 gifts that each cost the same amount. \n"
              "            What was the price of each of Kate’s gifts?")
        question_6_answer = float(input("Answer: "))
        if question_6_answer == 5:
            question_6_print = "CORRECT"
        continue
    elif question_select == "7":
        print("Question 7: 331 students went on a field trip. Six carts were \n"
              "            filled, and 7 students traveled on foot. \n"
              "            How many students were in each cart?")
        question_7_answer = float(input("Answer: "))
        if question_7_answer == 54:
            question_7_print = "CORRECT"
        continue
    elif question_select == "8":
        print("Question 8: Jill bought items costing $3.45, $1.99, $6.59, and \n"
              "            $12.98. She used a coupon worth $2.50. If Jill had $50.00 when \n"
              "            she went into the store, how much did she have when she left?")
        question_8_answer = float(input("Answer: "))
        if question_8_answer == 27.49:
            question_8_print = "CORRECT"
        continue
    elif question_select == "9":
        print("Question 9: Anne earned $3 an hour baby-sitting, and \n"
              "            $4 an hour working in the garden. Last week she did \n"
              "            baby-sitting for 5 hours and garden work for 3 hours. \n"
              "            How much more money does she need to buy a game that costs $35?")
        question_9_answer = float(input("Answer: "))
        if question_9_answer == 8:
            question_9_print = "CORRECT"
        continue
    elif question_select == "10":
        print("Question 10: The Cooking Club made some pies to sell at \n"
              "             a basketball game to raise money for the new math books. \n"
              "             The cafeteria contributed four pies to the sale. Each pie \n"
              "             was then cut into five pieces and sold. There was a total \n"
              "             of 60 pieces to sell. How many pies did the club make?")
        question_10_answer = float(input("Answer: "))
        if question_10_answer == 8:
            question_10_print = "CORRECT"
        continue
    if question_select == "0":
        input("You motion for Auron to keep an eye on the door, as you insert the piece of\n"
              "paper into the slot labelled 'INPUT'.")
        print()
        input("The device makes a quiet humming noise and it takes the paper in on one end and \n"
              "returns it out the other.")
        input("From across the room, you hear Auron say “There's something showing up on the door over\n"
              "here. It looks like a list of questions, and each one is labeled. I'll read it out.“")
        print()
        input("You hear Auron call out the answer for each question, one by one. The door reads:\n"
              f"Question 1:  {question_1_print}\n"
              f"Question 2:  {question_2_print}\n"
              f"Question 3:  {question_3_print}\n"
              f"Question 4:  {question_4_print}\n"
              f"Question 5:  {question_5_print}\n"
              f"Question 6:  {question_6_print}\n"
              f"Question 7:  {question_7_print}\n"
              f"Question 8:  {question_8_print}\n"
              f"Question 9:  {question_9_print}\n"
              f"Question 10: {question_10_print}\n"
              f"")
        if question_1_print == "CORRECT" and question_2_print == "CORRECT" and question_3_print == "CORRECT" and question_4_print == "CORRECT" and question_5_print == "CORRECT" and question_6_print == "CORRECT" and question_7_print == "CORRECT" and question_8_print == "CORRECT" and question_9_print == "CORRECT" and question_10_print == "CORRECT":
            break
        else:
            input("Auron calls out: “It looks like we messed something up. Better try some of those again.“")
            print()
            continue
    else:
        print()
        input("Invalid selection. Please try again.")
print()
input("The door hums loudly. Auron takes a step back, just before it\n"
      "pulls itself completely open, from one side to the other.")
print()
input(f"“Well, it looks like it worked. Nice job, {player_name}.“ Degren says. Let's\n"
      "see what's next.")
print()
input("The door opens loudly, and as you and Degren make your way back \n"
      "over to Auron, you can see that he is standing perfectly still.")
print()
input("Whatever he sees on the other side of the door, he really doesn’t want to take his eyes off it.")
input("When you get to the door, you understand why.")
print()
input("You’re facing a room filled to the brim with treasure. Piles upon \n"
      "piles of gold coins, gems, precious minerals – you name it. ")
print()
input("You each wander inside. Degren immediately springs into action, \n"
      "his greed getting the better of him. He rushes in and begins to shovel \n"
      "the coins into his pack.")
print()
input("“Wait, Degren, this could be a tr-“ Auron tries to say, but it’s too late. \n"
      "Before he can finish his sentence, a quiet rumble briefly shakes the room, \n"
      "and the door worked so hard to open slams shut.")
print()
input("“Great. We’re trapped.” Auron says with a sigh. Degren doesn’t seem to care – he’s still collecting gold.")
input(f"“{player_name}, can you help me look for a way out?”")
print()
input("You nod. Better get to it – you don’t know what else might be waiting for you.")
print()
input("Apart from Degren, this room falls eerily quiet. You look around, \n"
      "taking in all of the treasure that lies before you. It could easily \n"
      "fund your businesses for years to come, but that doesn’t do you any \n"
      "good if you can’t get it out of this place.")
print()
input("“Who built this place?” you hear Auron wondering to himself. “What danger lurks here?”")
print()
input("After looking around for a while, it doesn’t seem that there are \n"
      "any other entrances or exits, apart from the one you came through. ")
print()
input("At that thought, your eyes wander over to examine the door. \n"
      "It’s sealed shut, but there are some more engravings on this side.")
input("More instructions, perhaps? You move in to get a closer look.")
print()
input("You read the engraving aloud: “You have done well to make it to my vault. \n"
      "However, before I will let you leave, you must pass one final test.”")
print()
input("Auron perks up, and heads over. “What is this test?”")
print()
input("You continue. “I hope you are aware of the colors of the rainbow, for \n"
      "you must find six gems or items within my treasure hoard that match them, \n"
      "and then insert them into the slots you will see below – starting from the \n"
      "left, with red. I have done you the favor of adding the final color - purple - for you.”")
print()
input("While reading, you look down and do, indeed, see six empty sockets. \n"
      "The socket on the far right is already filled with a deep purple gem.")
print()
input("You continue. “However, be aware that three incorrect attempts \n"
      "will lock the door forever – and this place will become your tomb.”")
print()
input("Auron’s face falls flat. “Great.” He says, as you see worry take hold. \n"
      "“Degren, time to snap out of it. We’ve got some gem hunting to do.”")
print()

# PART III - THE ESCAPE
input("The three of you spend a while hunting down six items that you feel\n"
      "like match the colors of the rainbow. You come out of it with the following:\n"
      "- a Ruby\n"
      "- a Sapphire\n"
      "- an Emerald\n"
      "- an Amethyst\n"
      "- a hard piece of Amber\n"
      "- a Citrine")
print()
input("“Alright…” Auron says. “Now, to put these into their respective slots \n"
      "in the right order, starting with the first color of the rainbow.”")
print()
input("You nod, gems in hand. Time to do this.")
print()
input(f"“We’re in your hands, {player_name}.” Degren says, still collecting money. \n"
      "“Hey, Auron, come over here and carry some of this for me.”")
input("… he’s in his own world.")
incorrect_attempt_counter = 0
while True:
    # attempts_remaining = 3 - incorrect_attempt_counter
    def game_over():
        if incorrect_attempt_counter == 3:
            input("As the gem falls to the floor, the door lights up. The same rune that was on the front door\n"
                  "appears again, much larger and brighter.")
            print()
            input("You hear a voice coming from the rune. “So, it would seem you don't know your colors after\n"
                  "all. A shame.“")
            print()
            input("“Well, a shame for you at least. I get the pleasure of adding you to my vault now. Enjoy\n"
                  "eternity, my treasure. Maybe I'll feed you from time to time, if you're lucky,")
            print()
            input("You briefly feel a panic set in, before the entire room falls into total darkness and silence.\n"
                  "Will this truly be your life from now on?")
            print()
            input("You spend your remaining days talking with Degren and Auron, before their voices\n"
                  "fall silent, one by one.")
            input("You begin to think that, maybe, you should have just kept walking.")
            print()
            print()
            input("GAME OVER")
            quit()
    while True:
        if incorrect_attempt_counter == 3:
            game_over()
        gem_1 = input(f"ATTEMPTS REMAINING: {3 - incorrect_attempt_counter}\n"
                      "Which gem will you place in the right-most slot?\n"
                      "1. Ruby\n"
                      "2. Sapphire\n"
                      "3. Emerald\n"
                      "4. Amethyst\n"
                      "5. Amber\n"
                      "6. Citrine\n"
                      "")
        if gem_1 == "1":
            input("You hear a soft 'click' as the gem neatly slots into place.\n"
                  "It begins to glow faintly. Seems like it worked.")
            print()
            break
        elif gem_1 == "2" or gem_1 == "3" or gem_1 == "4" or gem_1 == "5" or gem_1 == "6":
            input("As you try to insert the gem, you feel a sharp recoil. It feels\n"
                  "like you're briefly filled with a deep sense of greed, but it quickly fades.")
            print()
            input("The gem is knocked out of the slot and falls onto the floor. That\n"
                  "must have been the wrong answer.")
            print()
            incorrect_attempt_counter += 1
            continue
        else:
            input("Invalid selection. Please input a number between 1 and 6.")
            print()
            continue
    while True:
        if incorrect_attempt_counter == 3:
            game_over()
        gem_2 = input(f"ATTEMPTS REMAINING: {3 - incorrect_attempt_counter}\n"
                      "Which gem will you place next to the color red?\n"
                      "1. Sapphire\n"
                      "2. Emerald\n"
                      "3. Amethyst\n"
                      "4. Amber\n"
                      "5. Citrine\n"
                      "")
        if gem_2 == "4":
            input("You hear a soft 'click' as the Amber stone neatly slots into place.\n"
                  "It begins to glow a little brighter. Seems like it worked.")
            print()
            break
        elif gem_2 == "1" or gem_2 == "2" or gem_2 == "3" or gem_2 == "5":
            input("As you try to insert the gem, you feel a sharp recoil. It feels\n"
                  "like you're briefly filled with a deep sense of greed, but it quickly fades.")
            print()
            input("The gem is knocked out of the slot and falls onto the floor. That\n"
                  "must have been the wrong answer.")
            print()
            incorrect_attempt_counter += 1
            continue
        else:
            input("Invalid selection. Please input a number between 1 and 5.")
            print()
            continue
    while True:
        if incorrect_attempt_counter == 3:
            game_over()
        gem_3 = input(f"ATTEMPTS REMAINING: {3 - incorrect_attempt_counter}\n"
                      "Which gem will you place next to the color orange?\n"
                      "1. Sapphire\n"
                      "2. Emerald\n"
                      "3. Amethyst\n"
                      "4. Citrine\n"
                      "")
        if gem_3 == "4":
            input("You hear a soft 'click' as the Citrine neatly slots into place.\n"
                  "It begins to glow a little brightly. Seems like it worked.")
            print()
            break
        elif gem_3 == "1" or gem_3 == "2" or gem_3 == "3":
            input("As you try to insert the gem, you feel a sharp recoil. It feels\n"
                  "like you're briefly filled with a deep sense of greed, but it quickly fades.")
            print()
            input("The gem is knocked out of the slot and falls onto the floor. That\n"
                  "must have been the wrong answer.")
            print()
            incorrect_attempt_counter += 1
            continue
        else:
            input("Invalid selection. Please input a number between 1 and 4.")
            print()
            continue
    while True:
        if incorrect_attempt_counter == 3:
            game_over()
        gem_4 = input(f"ATTEMPTS REMAINING: {3 - incorrect_attempt_counter}\n"
                      "Which gem will you place next to the color yellow?\n"
                      "1. Sapphire\n"
                      "2. Emerald\n"
                      "3. Amethyst\n"
                      "")
        if gem_4 == "2":
            input("You hear a soft 'click' as the gem neatly slots into place.\n"
                  "It begins to glow quite brightly. Seems like it worked.")
            input("At this point, the light from the rainbow on the door is beginning to reflect off all the\n"
                  "treasure in the room.")
            print()
            break
        elif gem_4 == "1" or gem_4 == "3":
            input("As you try to insert the gem, you feel a sharp recoil. It feels\n"
                  "like you're briefly filled with a deep sense of greed, but it quickly fades.")
            print()
            input("The gem is knocked out of the slot and falls onto the floor. That\n"
                  "must have been the wrong answer.")
            print()
            incorrect_attempt_counter += 1
            continue
        else:
            input("Invalid selection. Please input a number between 1 and 3.")
            print()
            continue
    while True:
        if incorrect_attempt_counter == 3:
            game_over()
        gem_5 = input(f"ATTEMPTS REMAINING: {3 - incorrect_attempt_counter}\n"
                      "Which gem will you place next to the color green?\n"
                      "1. Sapphire\n"
                      "2. Amethyst\n"
                      "")
        if gem_5 == "1":
            input("You hear a soft 'click' as the Sapphire neatly slots into place.\n"
                  "It begins to shine. Seems like it worked.")
            print()
            break
        elif gem_5 == "2":
            input("As you try to insert the gem, you feel a sharp recoil. It feels\n"
                  "like you're briefly filled with a deep sense of greed, but it quickly fades.")
            print()
            input("The gem is knocked out of the slot and falls onto the floor. That\n"
                  "must have been the wrong answer.")
            print()
            incorrect_attempt_counter += 1
            continue
        else:
            input("Invalid selection. Please input a number between 1 and 2.")
            print()
            continue
    while True:
        if incorrect_attempt_counter == 3:
            game_over()
        gem_6 = input(f"ATTEMPTS REMAINING: {3 - incorrect_attempt_counter}\n"
                      "Which gem will you place next to the color blue?\n"
                      "1. Amethyst\n"
                      "")
        if gem_6 == "1":
            input("You hear a soft 'click' as the final gem neatly slots into place.\n"
                  "It begins to glow faintly. Seems like it worked.")
            print()
            break
        else:
            input("Invalid selection. Please input number 1. Finish this.")
            print()
            continue
    print()
    input("As the final gem slots in, the rainbow on the door before you explodes in a bright array of colors.\n"
          "It's quite beautiful.")
    print()
    input("As it shines, you hear a voice. “I congratulate you on solving my final puzzle for you. While I\n"
          "would have enjoyed adding you all to my collection, I will settle for\n"
          "finally getting to have some guests.“")
    print()
    input("The voice laughs. It's unsettling.")
    print()
    input("“You may take as much treasure from this vault as you can carry. Return, and I will seal\n"
          "you inside forever. Until next time, adventurers.")
    print()
    input("When the voice stops talking, the light fades. The doors slide open once again, and you\n"
          "feel a breeze upon your skin. Freedom.")
    break
print()
input(f"“Okay.“ Auron says, clearly relieved. “Thanks for the save there, {player_name}! I owe you\n"
      f"a drink.")
print()
input("Degren finally perks up. “Well, my bag and pockets are stuffed. Shall we get the hell out\n"
      "of here? After you both fill up as well, of course.")
print()
input("You and Auron look at each other. He shrugs, and begins to load up his inventory.\n"
      "You wonder if you should do the same.")
print()

while True:
    gold_take = input("Will you take any treasure? (Y/N)\n"
                      " ").upper()
    if gold_take == "Y":
        print()
        input("You earned this reward, and it'd be rude to refuse it.\n"
              "You fill your pouches and pockets with whatever valuables\n"
              "you can find - it will help your business, after all.")
        print()
        input("With full pockets, the three of you leave the hillside home.\n"
              "You make it back to the road, and head towards town.")
        print()
        input("END OF GAME")
        quit()
    elif gold_take == "n":
        print()
        input("No. This place was bad enough - you don't want to take any part\n"
              "of it with you. Even if you did have to do math to get here.\n"
              "You shudder.")
        input("Math. Gross.")
        print()
        input("With empty pockets, you leave the hillside home. Your companions\n"
              "follow close behind, pockets very full.You make it back to the \n"
              "road, and head towards town.")
        input("“Drinks are on me.“ says Degren, as you walk into the setting sun.")
        print()
        input("END OF GAME")
        quit()
    else:
        print()
        input("Invalid selection. Please enter either Y or N.")
        print()
        continue
