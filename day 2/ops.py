# variables -> lowercase
# constant -> All CAPS
# use underscore => first_name
# _variable => in classes

# arithmetic operators -> +, -, *, /, //, %, **
# Ex: E-commerce order calculation
unit_price = 99.99
quantity = 7
discount_pct = 15
tax_rate = 0.085
shipping_rate = 5.99

# calculations
subtotal = unit_price * quantity
discount_amt = subtotal * (discount_pct/100)
discounted_price = subtotal - discount_amt
tax_amt = discounted_price * tax_rate
total = discounted_price + tax_amt + shipping_rate

full_boxes = quantity // 3
leftover_items = quantity % 3

print('Subtotal: Rs.', subtotal)
print(f'Discount (15%): Rs.{discount_amt:.2f}')
print(f'After Discount: Rs.{discounted_price:.2f}')
print(f'Tax (8.5%): Rs.{tax_amt:.2f}')
print(f'Shipping: Rs.{shipping_rate:.2f}')
print(f'TOTAL: Rs.{total:.2f}')
print(f'Full Boxes: {full_boxes}, LeftOver items: {leftover_items}')