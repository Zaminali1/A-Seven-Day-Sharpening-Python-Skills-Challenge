# loops in python
# looploops are used to execute a block of code repeatedly until a certain condition is met.
# there are two types of loops in python
# 1. for loop
# 2. while loop


#while loop
# while loop is used to execute a block of code repeatedly until a certain condition is met.



while True :
    print("Hello")



x=5
while x >= 1:
    print(x)
    x -= 1

     

    #  break and continue keywords in python

    # break is used to terminate loop when encountered 
#eg
l=8
while l<=15:
    print(l)
    if(l==11):
        break
    l+=1

    # like here when it encountered 11 it comes out of loop



y = 1
while y <= 8:
    if y == 5:
        y += 1
        continue
    print(y)
    y += 1

y = 1
while y <= 8:
    if y == 5:
        y += 1
        continue
    print(y)
    y += 1


#  for loop
# for loop is used for sequence iteration
# eg

#  using for loop to print elements of a list


list=[8,9,6,3,0]
for num in list:
 print(num)


o = 3
while o <= 8:
    if (o%2 == 0):
         o += 1
         continue 
    print(o)
    o+=1   


n = "hello"
for char in n:
     if (char=='z' ):
          print("l found")
          break
     print(char)
else:
     print("The End")