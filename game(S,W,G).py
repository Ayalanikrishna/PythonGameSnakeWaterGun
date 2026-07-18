import random
"""
1 for Snake
-1 for Water
0 for Gun
"""

computer = random.choice([1, -1, 0])
print("{S - Snake",
      ",W - Water",
      ",G - Gun}")
youstr = input("Enter your choice (S, W, G): ").upper()
youDict = {"S": 1, "W": -1, "G": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]
print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("Draw")
else:
    if (computer == -1 and you == 1) or \
       (computer == 1 and you == 0) or \
       (computer == 0 and you == -1):
        print("You win!")
    else:
        print("You lose")
