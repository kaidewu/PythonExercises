import random
import os

text = open('file.txt')
num_lines = sum(1 for line in text if line.rstrip())
ran_line = random.randint(0, num_lines)


print()
