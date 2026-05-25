def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()
####
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])
