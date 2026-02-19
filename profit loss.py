buy  = int(input("Enter buying price:  "))
sell = int(input("Enter selling price:  "))

if sell > buy :
     profit = sell - buy
     print("You made profit of TK", profit)
elif buy == sell :
     print("No profit No loss! !")
else:
     loss = buy - sell
     print("You made a loss of TK:", loss)