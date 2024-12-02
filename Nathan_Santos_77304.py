
age = int(input("Please enter your age: "))
price = int(input("Please enter the price of the product: "))
final_price = (price * 0.90) 
additional = (final_price - 10)


if age < 18 and final_price < 100:
    print (f"The final price is {final_price}")
    
elif age < 18 and final_price > 100:
    print (f"The final price is {additional}")    
    
else:
    print ("The final price is ", price, "\nYou have earned: No discounts or promotions.")
next_customer = input ("Do you want to enter details for another customer? (yes/no)")
if next_customer == "no":
    print ("Thank you!")
while next_customer != "no":
    
    age = int(input("Please enter your age: "))
    price = int(input("Please enter the price of the product: "))
    final_price = (price * 0.90) 
    additional = (final_price - 10)

    if age < 18 and final_price < 100:
        print (f"The final price is {final_price}")
        
    elif age < 18 and final_price > 100:
        print (f"The final price is {additional}")
        
    else:
        print ("The final price is ", price, "\nYou have earned: No discounts or promotions.")
    next_customer = input ("Do you want to enter details for another customer? (yes/no) ")



