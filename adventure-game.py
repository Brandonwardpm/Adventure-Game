import random
import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro(object, selection):
    print_pause("You're in your living room, "
                "watching the news describe how high inflation has gotten in the U.S.\n")
    print_pause("Everyone knows " + selection + " is to blame. But that doesn't matter now. "
                "The question is, what to do about it?\n")
    print_pause("Suddenly you get a text message from an unrecognized phone number.\n")
    print_pause("It reads: \"This is your future self.\"\n")
    print_pause("\"I don't have much time to explain.\"\n")
    print_pause("\"But your world is going through a financial revolution.\"\n")
    print_pause("\"Your legacy system is pending collapse, and there is only one way out\"\n")
    print_pause("\"You can either take the orange pill "
                "or reply \'STOP\' to this message and forget this ever happened.")

