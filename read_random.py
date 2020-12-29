# Laurie Hall
# PA_7

def read_random(file_path,file_name): 
   util = file_path+"/"+file_name 
   counter = dict() 
   
   #Open file
   f = open(util, "r") 
   
   #Convert to string
   num_str = f.read().strip()

   # Replace all 10's with T so "10" is not read as a 1 and 0 seperately
   # This was per tutor, so I wasnt sure if this is what you were looking for
   num_str = num_str.replace("10","T")

   for num in num_str: 
      counter[num] = counter.get(num, 0) + 1

   #Print result
   for x in sorted(counter.keys()):
      if x=="T": 
         print("The number of 10's is",counter[x])
      else: 
         print("The number of "+x+"'s is",counter[x])

path = input("Enter the path to the file you wish to read: ")
name = input("Enter the file name: ")
read_random(path,name)
