balance=0
transactions=[]
while True:
  print("\n---Expense-Tracker---")
  print("1.Add income")
  print("2.Add Expense")
  print("3.Show Balance")
  print("4.Show Transactions")
  print("5.Exit")
  choice=input("Enter choice:")
  if choice=="1":
    amount=float(input("Enter income amount:"))
    balance+=amount
    transactions.append(("Income",amoount))
    print("Income added!")
  elif choice=="2":
    amount=float(input("Enter expense amount:"))
    balance-=amount
    transactions.append(("Expense",amount))
    print("Expense added!")
  elif choice=="3":
    print("Current Balance: ",balance)
  elif choice=="4":
    if not transactions:
      print("No transactions yet.")
    else:
      for t in transactions:
        print(t[0], "-Rs",t[1])
  elif choice=="5":
    print("Goodbye!")
    break
  else:
    print("Invalid choice!")
