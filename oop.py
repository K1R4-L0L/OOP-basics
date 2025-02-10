import random

class Character:
    #class attricbutes
    hair_colors = ["Blonde", "Brown", "Black", "Red"]
    sizes = ["Tiny", "Medium", "Large"]
    special_powers = ["Flying","Invisibility", "Super Strength", "Mind reading"]
    height = ["Short", "average", "tall"]
    skin_color ["white", "yellow", "brown", "orange", "black"]

    #Constructor
    def__init__(sel):
        self.generate_character()

    def generate_character():
        self.hair_color = random.choice(Character.hair_colors)
        self.size = random.choice(Character.sizes)
        self.power = random.choice(Character.special_powers)
        self.height = random.choice(Character.height)
        self.color = random.choice(Character.skin_color)
        self.description = (
            f"Your character has {self.hair_color}hair, "
            f" is {self.size} in size, {self.color}, {self.height}, and has the power of {self.power}"
        )

def__str__(self):
    return self.description

char1 = Character()
char2 = Character()
print(char1)
print(char2)