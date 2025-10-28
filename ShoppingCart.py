prices= []
items=[]
while True:
    item= input("enter your item(press q to quit): ")
    if item.lower()=="q":
        break
    else:
        price= float(input("Enter its price: "))
        items.append(item)
        prices.append(price)
total=sum(prices)
a= "Your shopping cart items:"
print(f"----{a.upper()}----")
for i in items:
    print(i, end= "   " )
    print(f": {prices[items.index(i)]}")
# print("\n")
# for i in prices:
#     print(i, end= " ")
    
print("\n")
print(f"total is {total}")