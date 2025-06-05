p=input("Enter name of baby: ")
for x in reversed(range(1,11)):
    print(x)

print("Welcome To This world",p)


# CONDITIONAL STATEMENTS
light=("Gre")
if (light=="Green"):
     print("Go")
else:
     print("Wait")

Age=25
status="Adult" if Age>=23 else "Minor"
print(status)

# Assign grades to student based on marks...
marks = int(input("Enter You'r Marks: "))
if marks >= 95 and marks < 100:
    grade= "A++"
elif marks >= 90 and marks < 95:
    grade = "A+"
elif marks >= 80 and marks < 90:
    grade = "A"
elif marks >= 70 and marks < 80:
    grade = "B"
elif marks >= 40 and marks < 70:
    grade = "C"
else:
    grade = "F" 

print("You Got ", grade ,"Grade" )

Age= 40
if (Age >= 18):
    if (Age>=80):
        print("You can not drive")
    else:
        print("You can drive")

# Nesting
student=5
if(student >=5):
    if (student<=2):
     print("They can not go")
    else:
     print("They can go")
else:
      print("Come here")

# Practice:
# Write a program to check if number entered by user is odd or even
num= int(input("Enter Number : "))
rem=num%2
if(rem == 0):
    result="Even"
else:
    result="Odd"
print("Number is ",result)

# 2. WAP to check if a number is multiple of 7 or not.
Num2=int(input("Enter Number To Check It is Multiple of Seven Or Not: "))
rem2=Num2%7
if(rem2==0):
  print("The Number You Entered is Multiple of 7")
else:
    print("The Number You Entered is not Multiple of 7")

