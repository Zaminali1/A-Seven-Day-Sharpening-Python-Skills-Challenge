balance = 0
expenses=[]
while True:
    command=input("Deposit/Spend/Report/Quit: ").lower()
    if command == "deposit":
      amount=float(input("Enter Amount To Deposit: "))
      balance+=amount
      print(f"Balance:{balance}")
    elif command == "spend":
        amount=float(input("Amount: "))
        if amount <= balance: 
           balance-=amount
           expenses.append(amount)
           print(f"Spent Balance: {amount}")
        else:
            print("Not Enough Balance")
    elif command == "report":
       print(f"Balance: {balance}")
       print("Expenses:",expenses)
    elif command == "quit":
       break
    else:
       print("Kindly select correct option")