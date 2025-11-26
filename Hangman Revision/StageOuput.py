# A simple subroutine that outputs a user-friendly representation of the stage of the game based on the input
Stages = [
    
"You have not messed up yet and shouldn't be seeing this"
    
            ,'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def StageOut(num):
    print("You have "+str((len(Stages)-(num+1)))+" chances left!")
    if num == 0:
        return 
    else:
        return Stages[num]


if __name__ == "__main__":
   print(StageOut(int(input("Input a stage to test"))))
