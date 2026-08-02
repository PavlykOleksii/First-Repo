import random
import pathlib

current_dir = pathlib.Path(__file__).parent
# print(current_dir)

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "No jokes available."
