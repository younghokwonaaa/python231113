import openpyxl
from openpyxl import Workbook
import random

# Create a new workbook and select the active sheet
workbook = Workbook()
sheet = workbook.active

# Add headers to the sheet
headers = ["Product ID", "Product Name", "Price", "Quantity"]
sheet.append(headers)

# Generate 100 sample electronic product sales data
for _ in range(100):
    product_id = random.randint(1000, 9999)
    product_name = f"Product_{product_id}"
    price = round(random.uniform(10.0, 1000.0), 2)
    quantity = random.randint(1, 10)

    # Append data to the sheet
    sheet.append([product_id, product_name, price, quantity])

# Save the workbook to a file
workbook.save("sales.xlsx")
