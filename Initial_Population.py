import log from log
import grab_screen from Grag_Screen
import outputs
import numpy as np
import random
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from statistics import median, mean
from collections import Counter

LR = 1e-3
goal_steps = 500
score_requirement = "Win"
initial_games = 100

def some_random_games_first():
    GameCount = 0
    while True:
        if GameCount <= 5:
            action = rand.randrange()

            observation = 
            reward = ["Score", "Kills", "Win"]
            done = "done"
            info = 

            if done = "done":
                GameCount += 1
