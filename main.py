import random
import keyboard
import os

start_deck = list("""---------------------
                  |    |    |    |    |
                  ---------------------
                  |    |    |    |    |
                  ---------------------
                  |    |    |    |    | 
                  ---------------------
                  |    |    |    |    | 
                  ---------------------""")
deck = start_deck
nums = [[0 for _ in range (4)] for _ in range (4)]

def list_rot90(data, times=1):
    if times==0:
        return data
    rot_data = []
    for t in range (times):
        m = len(data)
        n = len(data[0])
        rev_data = data[::-1]
        rot_data = [[rev_data[j][i] for j in range (m)]
                    for i in range (n)]
        data = rot_data
    return rot_data

def write_nums():
    global deck
    deck = start_deck[:]
    for row in range (4):
        for col in range (4):
            if nums[row][col]:
                for i in range(len(str(nums[row][col]))):
                    deck[22 + (row * (22 * 2)) + 1 + col * 5 + i] = str(nums[row][col])[i]