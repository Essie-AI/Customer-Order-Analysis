
# Customer Order Analysis

orders = [{'customer': 'Alice', 'product': 'Laptop', 'category': 'Electronics', 'price': 1200}, {'customer': 'Bob', 'product': 'T-Shirt', 'category': 'Clothing', 'price': 25}, {'customer': 'Alice', 'product': 'Coffee Maker', 'category': 'Home Essentials', 'price': 80}, {'customer': 'Diana', 'product': 'Blender', 'category': 'Home Essentials', 'price': 150}, {'customer': 'Charlie', 'product': 'Laptop', 'category': 'Electronics', 'price': 1200}, {'customer': 'Bob', 'product': 'Jeans', 'category': 'Clothing', 'price': 60}, {'customer': 'Charlie', 'product': 'Headphones', 'category': 'Electronics', 'price': 100}]

# Step 1: Total spend per customer
customer_totals = {'Alice': 1280, 'Bob': 85, 'Diana': 150, 'Charlie': 1300}
print("Total Spend per Customer:")
for customer, total in customer_totals.items():
    print(f"{customer}: ${total}")

# Step 2: Most Popular Products
product_counts = {'Laptop': 2, 'T-Shirt': 1, 'Coffee Maker': 1, 'Blender': 1, 'Jeans': 1, 'Headphones': 1}
print("\nProduct Purchase Frequency:")
for product, count in product_counts.items():
    print(f"{product}: {count} purchases")

# Step 3: Sales by Category
category_totals = {'Electronics': 2500, 'Clothing': 85, 'Home Essentials': 230}
print("\nTotal Sales by Category:")
for category, total in category_totals.items():
    print(f"{category}: ${total}")
