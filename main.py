from game_data import data
import random
from art import logo, vs

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
