product_name = "Laptop"
price = 85000
quantity_sold = 7
stock =  25
discount = 10
tax = 18
minimum_stock = 10

# 1. total sales

total_sales_before_discount = price*quantity_sold
print(total_sales_before_discount)

# 2.discount amount

discount_amount =   discount/100*price
print(discount_amount)

# 3.price after discount

price_after_discount = price-discount_amount
print(price_after_discount)

# 4.tax amount

tax_amount = tax/100*price
print(tax_amount)

# 5. final invoice amount
final_invoice_amount = price_after_discount + tax_amount
print(final_invoice_amount)

# 6. reamaining stock

remaining_stock =stock - quantity_sold
print(remaining_stock)






# product_name = "Laptop"
# price = 85000
# quantity_sold = 7
# stock =  25
# discount = 10
# tax = 18
# minimum_stock = 10


### Part 2 — Comparison Operators

# Use comparison operators to determine:
#
# 1. Whether the remaining stock is below the minimum stock level.
# 2. Whether the product price is greater than 50,000.
# 3. Whether the quantity sold is greater than or equal to 5.
# 4. Whether the final invoice amount is equal to a specified target amount.
# 5. Whether the remaining stock is not equal to zero.
#
print(remaining_stock<minimum_stock)

print(price>50000)

print(quantity_sold>=5)

print(final_invoice_amount==850000)

print(remaining_stock!=0)

### Part 3 — Logical Operators

# Create conditions using `and`, `or`, and `not`.
#
# For example:
#
# * If the product price is above 50,000 **and** quantity sold is at least 5, display:
#   `"High-value product with strong sales"`
#
# * If stock is below the minimum level **or** stock is zero, display:
#   `"Inventory Reorder Required"`
#
# * Use `not` to check whether the product is **not** out of stock.





















































stock = 25

### Part 4 — Assignment Operators
# Perform the following operations using assignment operators:
#
# ```python
# stock -= 7
# stock += 10
# stock *= 2
# stock //= 2
# ```
#
# Display the value of `stock` after each operation.

# x = 5
#
# x += 3
#
# print(x)

stock -= 7
print(stock)


stock += 10
print(stock)


stock *= 2
print(stock)

stock //= 2
print(stock)





### Part 5 — Membership Operators

products = ["Laptop", "Mobile", "Tablet", "Monitor", "Keyboard"]
#
#
# Use `in` and `not in` to check:
#
# 1. Whether `"Laptop"` exists in the product list.
# 2. Whether `"Printer"` exists in the product list.
# 3. Whether `"Mobile"` is not in the product list.


print("Laptop" in products)

print("Printer" in products)

print("Mobile" not in products)





### Part 6 — Identity Operators

# Create:

# ```python
company = "TechStore"
branch = company
# # ```
#
# Use `is` and `is not` to determine whether both variables refer to the same object.
#
# > **Note:** Do not use `is` for normal value comparison. Explain briefly why `==` and `is` are different.


print(company is branch)

print(company is not branch)




