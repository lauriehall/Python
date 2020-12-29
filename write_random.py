# Laurie Hall
# PA_7

import random

def fill_random(file_path,file_name):

  util = file_path+"/"+file_name

  file = open(util,"w")

  for _ in range(10000):
    number = random.randint(1,10)
   
    file.write(str(number))
    file.write("\t")

  file.close()

  print("The 10,000 random numbers have been written to the file successfully")

file_path = input("Enter the path to the file you wish to create: ")
file_name = input("Enter the file name: ")

fill_random(file_path,file_name)