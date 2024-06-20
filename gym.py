import numpy as np
import gymnasium as gym
import random
import time
from IPython.display import clear_output

env = gym.make('FrozenLake-v1', render_mode='ansi')

action_space_size = env.action_space.n
state_space_size = env.observation_space.n

q_table = np.zeros((state_space_size, action_space_size))

num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1
discount_rate = 0.99 # high discount rate means , puurani cheeze bhi abhi tak yaad rahegi, will not forget so easily

exploration_rate = 1    # the upgraded version of epsilon delta , where we start from 1 and slowly decay to 0.01, going from exploration to exploitation
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001

rewards_all_episodes = []

# Q-learning algorithm
for episode in range(num_episodes):
    # initialize new episode params

    for step in range(max_steps_per_episode): 
        # Exploration-exploitation trade-off
        # Take new action
        # Update Q-table
        # Set new state
        # Add new reward        

    # Exploration rate decay   
    # Add current episode reward to total rewards list