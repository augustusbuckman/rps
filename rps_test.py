import os.path
import sys
from unittest import TestCase

from rps import main
from tud_test_base import *

def test_rps():
    try:
        exist = os.path.exists("rps.py")
        assert exist == True
    except:
        sys.exit()

    set_keyboard_input(['Joyce',1,'y',9876,'P'])
    main()
    output = get_display_output()
    assert output==[
        "Welcome to ROCK PAPER SCISSORS. I, Computer, will be your opponent.",
        "--- INITIAL INPUT ---",
        "Please enter your name: ",
        "Thank you!",
        "",
        "--- INITIAL INPUT ---",
        "Please enter the number of rounds to play: ",
        "Thank you!",
        "",
        "--- INITIAL INPUT ---",
        "Please enter y if you want to set the seed: ",
        "Thank you!"
        "",
        "--- INITIAL INPUT ---",
        "Please enter an integer for the seed: ",
        "Thank you!",
        "",
        "--- Round 1 ---",
        "Joyce, enter your choice for this round.",
        "R for Rock, P for Paper, S for Scissors: ",
        "I pick Paper.",
        "We picked the same thing. Round is a draw.",
        "",
        "We played 1 round of ROCK PAPER SCISSORS.",
        "Joyce won 0 rounds.",
        "Well played.",
    ]
