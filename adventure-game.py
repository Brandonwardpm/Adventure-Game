import random
import time

def print_pause(message):
    print(message)
    time.sleep(4)

def intro(knowledge, selection):
    print_pause("You're in your living room, "
                "watching the news describe how high inflation has gotten in the U.S.\n")
    print_pause("Everyone knows " + selection + " is to blame. But that doesn't matter now. "
                "The question is, what to do about it?\n")
    print_pause("Suddenly, you get a text message from an unrecognized phone number.\n")
    print_pause("It reads: \"This is your future self.\"")
    print_pause("\"I don't have much time to explain.\"")
    print_pause("\"But the world is about to go through a financial revolution.\"")
    print_pause("\"The legacy system is pending collapse, and there are only two options.\"")
    print_pause("\"Either you can take the orange pill, "
                "or you can take the fiat pill. Which will it be?\"")

def fiat_pill(knowledge, selection):
    if "fiat_knowledge" in knowledge:
        print_pause("You think, \'Wait, this looks familiar.\'")
        print_pause("\'I should probably take the orange pill instead.\'")
    else:
        print_pause("\nYou take the fiat pill.")
        print_pause("You have a vision of the Federal Reserve "
                    "being created in 1913.")
        print_pause("Visions of all the wars which took place "
                    "during the century thereafter.")
        print_pause("Visions of the Great Depression "
                    "and Great Financial Crisis of 2008, and see a bleak future ahead.")
        print_pause("You think, \'That was pretty dark. "
                    "I should probably take the orange pill instead.\'")
        knowledge.append("fiat_knowledge")
    living_room(knowledge, selection)

def orange_pill(knowledge, selection):
    print_pause("\nYou take the orange pill.")
    print_pause("Somewhere, " + selection + " stares off into the distance "
                "because he knows it's too late.")
    print_pause("He can't steal your purchasing power from you "
                "any longer.")
    print_pause("You have successfully made the "
                "decision to become orange-pilled "
                "by educating yourself on the miraculous feat "
                "of engineering known as Bitcoin.")
    while True:
        decision2 = input("\nWould you like to buy your first $20 worth of "
                            "Bitcoin on (1) Coinbase Pro or (2) FTX US?\n")
        if decision2 == "1":
            print_pause("You succesffully purchased $20 worth of "
                        "Bitcoin on Coinbase Pro, paying very little in fees.\n")
            print_pause("Congratulations! This is the first step in securing "
                        "your financial future.\n")
            break
        elif decision2 == "2":
            print_pause("\nYou succesfully purchased $20 worth of "
                        "Bitcoin on FTX US.")
            print_pause("However, you're disappointed because "
                        "they seem to have taken a lot in fees.")
            print_pause("You reason, \'I guess they have to pay for "
                        "all of that marketing somehow. I should probably "
                        "use Coinbase Pro next time instead.\'\n")
            break
        else:
            decision2 = input("\nWould you like to buy your first $20 worth of "
                            "Bitcoin on (1) Coinbase Pro or (2) FTX US?\n")
                        
def living_room(knowledge, selection):
    while True:
        decision1 = input("\nPress 1 to take the orange pill, or press 2 to take the fiat pill.\n")
        if decision1 == "1":
            orange_pill(knowledge, selection)
            break
        elif decision1 == "2":
            fiat_pill(knowledge, selection)
            break
        else:
            decision1 = input("\nPress 1 to take the orange pill, or press 2 to take the fiat pill.")

def time_travel():
    flashback = input("Would you like to go back in time "
                    "and make a different decision? (Y/N)\n").lower()
    if flashback == "y":
        print_pause("\nA bright flash of light followed by a deja vu momemnt . .\n")
        aha_moment()
    elif flashback == "n":
        print_pause("\nYou have decided to live with your decision.")
        print_pause("Will it be the right one?")
        print_pause("Only time will tell . .")
    else:
        time_travel()

def aha_moment():
    knowledge = []
    selection = random.choice(["Putin", "Biden", "Xi Jinping", "Jerome Powell"])
    intro(knowledge, selection)
    living_room(knowledge, selection)
    time_travel()

aha_moment()
