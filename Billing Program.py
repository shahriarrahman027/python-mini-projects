#taking input from user
item_name=input("Enter the name of your item: ")
price= int(input("Enter the price: "))
quantity= int(input("Enter quantity: "))

#claculating total price
total_price=price*quantity

#printing total price
print(f"Total Bill for {item_name} = {total_price}")
