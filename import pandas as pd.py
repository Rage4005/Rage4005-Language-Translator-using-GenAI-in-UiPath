import pandas as pd # type: ignore

# Ask how many products were purchased
num_items = int(input("Enter the number of products purchased: "))

# Collect product details
products = []
for i in range(1, num_items + 1):
    product_name = input(f"Enter the name of product {i}: ")
    products.append({"Item Number": i, "Product Name": product_name})

# Create a DataFrame for the product table
df = pd.DataFrame(products)

# Display the product table
print("\nPurchased Products Table:")
print(df)

# Save to Excel
excel_filename = "Purchased_Products.xlsx"
df.to_excel(excel_filename, index=False)

print(f"\nData successfully stored in '{excel_filename}'")
