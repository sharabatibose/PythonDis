menu= {"tempura":3.50, "cake":5, "tiramisu": 7.5, "pattie": 4}
cart=[]
print("---------MENU---------")
for x,y in menu.items(): #menu.items() giving a tuple of the tuple of key value pairs
  print(f"{x:10}: ${y}")
print("----------------------")
total=0
while True:
    intt= input("enter the food you want to order(q for quit): ").lower()
    if intt=='q':
      break
    if intt in menu:
        cart.append(intt)
        print(f"{intt} added to cart:  ${menu[intt]:.2f}")
    else:
        print("enter valid item")
for x in cart:
      if x in menu:
        total+= float(menu[x])
print(f"Your total is: ${total:.2f}")
