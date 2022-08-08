from game_data import data
import random
from art import logo, vs

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

