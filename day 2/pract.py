# # Print Number from 1 to 100


# # y=1
# # while y <=100:
# #     print(y)
# #     y+=1


# # WAP to Print Numbers from 100 to 1

# z=100
# while z >= 1:
#     print(z)
#     z-=1


# # Print the multiplication table of n.

# n=int(input("Enter  Number to Print Table : `"))
# i=1
# while i <=10:
#     print(n*i)
#     i+=1




# i = 1
# while i <= 100:
#     print(i)
#     i+=1 

    
# x=100
# while x >=1:
#     print(x)
#     x-=1



# y=int(input("Enter Number to get table : "))
# z=1
# while z <=10:
#  print(y*z)
#  z+=1





lis=[1,4,9,16,25,36,49,64,81,100]
i = 0
while i<len(lis):
    print(lis[i])
    i+=1


# print elements of list using loop

list=[1,4,9,16,25,36,49,64,81,10]
for val in list:
    print(val)



tup=(1,4,9,16,25,36,49,64,81,10,36)
x=36
idx=0
for el in tup:
    if (el == x):
        print("Found at idx",idx)
    idx+=1
# This concept in programming is called linear programming




# Use for and range loop:

# Print numbers from 1 to 100
for i in range(1,101):
    print(i)


# Print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)



# Print table of number n
l=int(input("Enter number to print a table: "))
for i in range(1,11):
    print(i*l) 