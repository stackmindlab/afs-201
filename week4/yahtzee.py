import random

class die():
    def __init__(self):
        pass
        
    def roll(self):
        return random.randint(1, 6)

    def getCurrentFaceValue(self):
        return self.roll()

    def showDieFace(self):
        print(self.getCurrentFaceValue())
    
def add_icon(num):
    match num:
        case 1:
            return f"⚀ ({num})"
        case 2:
            return f"⚁ ({num})"
        case 3:
            return f"⚂ ({num})"
        case 4:
            return f"⚃ ({num})"
        case 5:
            return f"⚄ ({num})"
        case 6:
            return f"⚅ ({num})"
    


def check_for_yahtzee(array):
    if(array[0] == array[1] == array[2] == array[3] == array[4]):
        return True


def roll_five():
    start_game = die()
    yahtzee_digits = [ start_game.getCurrentFaceValue() for x in range(5)]
    transformed_list = list(map(add_icon, yahtzee_digits))
    print(" ".join(transformed_list))
    if(check_for_yahtzee(yahtzee_digits)):
        print("YAHTZEE")
    






roll_five()
        

