# -*- coding: UTF-8 -*-
import thread
import time


def sing():
    for i in range(0, 9):
        print("I'm singing\n")


def playGuitar():
    for i in range(0, 9):
        print("I'm playing guitar\n")


thread.start_new_thread(sing, ())
thread.start_new_thread(playGuitar, ())

raw_input("press continue")
