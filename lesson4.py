product = input("Please select the Product: ")
price = float(input("Please enter the Price in $: "))
quantity = int(input("Please enters the qunatity: "))
in_stock = True


if quantity >= 10:
    discount = 20
elif quantity >= 5:
    discount = 10
else:
    discount = 0

subtotal = price * quantity
discount_given = round(subtotal * (discount / 100), 2)
total = subtotal - discount_given

if quantity <= 0:
    print("Invalid quantity!")
else:
    print()
    print("---RECEIPT---")
    print(f"Product: {product}")
    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"In Stock: {in_stock}")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount ({discount:g}%): -${discount_given:.2f}")
    print(f"Total: ${total:.2f}")
    if total > 50:
        print("🎉 You qualify for free delivery!")
