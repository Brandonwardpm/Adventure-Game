import random
import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro(knowledge, selection):
    print_pause("You're in your living room, "
                "watching the news describe how high inflation has gotten in the U.S.\n")
    print_pause("Everyone knows " + selection + " is to blame. But that doesn't matter now. "
                "The question is, what to do about it?\n")
    print_pause("Suddenly you get a text message from an unrecognized phone number.\n")
    print_pause("It reads: \"This is your future self.\"\n")
    print_pause("\"I don't have much time to explain.\"\n")
    print_pause("\"But your world is about to go through a financial revolution.\"\n")
    print_pause("\"Your legacy system is pending collapse, and there are only two options.\"\n")
    print_pause("\"You can either take the orange pill "
                "or you can take the fiat pill. Which will it be?\"\n")

def fiatPill(knowledge, selection):
    if "fiat_knowledge" in knowledge:
        print_pause("You think, \'Wait, this looks familiar.\'\n")
        print_pause("\'I should probably take the orange pill instead.\'\n")
    else:
        print_pause("You take the fiat pill.\n")
        print_pause("You have a vision of the Federal Reserve "
                    "being created in 1913.\n")
        print_pause("Visions of all the wars which took place "
                    "during the century thereafter.\n")
        print_pause("Visions of the Great Depression "
                    "and Great Financial Crisis of 2008, and see a bleak future ahead.\n")
        print_pause("You think, \'That was pretty dark. "
                    "I should probably take the orange pill instead.\'\n")
        knowledge.append("fiat_knowledge")
    living_room(knowledge, selection)

