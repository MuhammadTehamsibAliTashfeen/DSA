member = input("Are you a member? (yes/no): ").lower()
product = input("Please select the Product: ")
price = float(input("Please enter the Price in $: "))
quantity = int(input("Please enters the qunatity: "))
stock = 20

member_discount = 5

if quantity >= 10:
    discount = 20
elif quantity >= 5:
    discount = 10
else:
    discount = 0
    
if member == "yes":
    discount += member_discount


subtotal = price * quantity
discount_given = round(subtotal * (discount / 100), 2)
total = subtotal - discount_given

if quantity <= 0:
    print("Invalid quantity!")
elif stock < quantity:
    print(f"Sorry, only {stock} in stock!") 
else:
    print()
    print("---RECEIPT---")
    print(f"Product: {product}")
    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"In Stock: {stock}")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount ({discount:g}%): -${discount_given:.2f}")
    print(f"Total: ${total:.2f}")
    if total > 50 or member == "yes":
        print("🎉 You qualify for free delivery!")
