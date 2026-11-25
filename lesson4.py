# --- RECEIPT ---
# Product: Coffee
# Price: $4.99
# Quantity: 3
# In stock: True
# Subtotal: $14.97
# Discount (10%): -$1.50
# Total: $13.47

product = input("Please select the Product: ")
price = float(input("Please enter the Price in $: "))
quantity = int(input("Please enters the qunatity: "))
in_stock = True
discount = float(input("Please enter the discount in %: "))

subtotal = price * quantity
discount_given = subtotal * (discount / 100)
total = subtotal - discount_given

print()
print(" --- RECEIPT --- ")
print(f"Product: {product}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"In Stock: {in_stock}")
print(f"Subtotal is {subtotal:.2f}")
print(f"Discount ({discount:g}%): -${discount_given:.2f}")
print(f"Total: ${total:.2f}")

