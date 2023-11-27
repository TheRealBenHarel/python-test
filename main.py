import numpy as np
import test

my_list = [1, 2, "3"]

my_tuple = (2, 2, 4)

my_list[0] = 8

dict = {"sagi" : "or", 
        "yaron" : "drukh", 
        "ben" : "harel"}

for item in my_list:
    print(item, type(item))
    
if (my_list[0] == 8):
    print("hello")


def addition(x, y):
    return x + y

print(addition(2, 3))

print(len(my_list))