# Author: Tahmid Efaz
# Date: 7/21/2017

from stack import Stack

number = input("Enter the 1st term of the look and say sequence:  ")
nterms = int(input("Number of terms you want to generate? : "))

repeat_stack = Stack()
next_number = number
sequence_list = []
n = ""
  
for j in range(nterms):
  for i in range(len(next_number)):
    if(repeat_stack.size()==0):
      repeat_stack.push(next_number[i])
    else:
      if(repeat_stack.top()==next_number[i]):
        repeat_stack.push(next_number[i])
      else:
        n += str(repeat_stack.size())+ str(repeat_stack.top())
        repeat_stack.clean()
        repeat_stack.push(next_number[i])
    if(i==len(next_number)-1):
      n += str(repeat_stack.size())+ str(repeat_stack.top())
      repeat_stack.clean()
    
  sequence_list.append(n)
  next_number = n
  n=""

# print("The sequence is as follows: ")
# print(number)
for i in range(len(sequence_list)):
   print(sequence_list[i])
print("finished")
