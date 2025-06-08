while True :
    op=input("Enter + ,-,/,* or q to Quit:")
    if op == "q":
        break
    if op not in['+' ,'-','/','*' ]:
       print("Invalid Operation !")
       continue

    a=float(input("First Number: "))
    b=float(input("Second Number: "))
    if op=='+':
     print(a+b)
    elif op == '-':
      print(a-b)
    elif op == '/':
      print(a/b)
    elif op == '*':
     print(a*b)
    else :
        print("Invalid operation")