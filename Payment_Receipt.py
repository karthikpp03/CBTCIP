from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(transaction_id, date, customer_name, items, total_amount):
    file_name = f"receipt_{transaction_id}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 50, "Payment Receipt")

    
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, f"Transaction ID: {transaction_id}")
    c.drawString(30, height - 100, f"Date: {date}")
    c.drawString(30, height - 120, f"Customer Name: {customer_name}")


    c.drawString(30, height - 150, "Item")
    c.drawString(200, height - 150, "Quantity")
    c.drawString(300, height - 150, "Price")
    c.drawString(400, height - 150, "Total")

   
    y = height - 170
    for item, details in items.items():
        c.drawString(30, y, item)
        c.drawString(200, y, str(details['quantity']))
        c.drawString(300, y, f"${details['price']:.2f}")
        c.drawString(400, y, f"${details['total']:.2f}")
        y -= 20

   
    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, y - 20, "Total Amount:")
    c.drawString(400, y - 20, f"${total_amount:.2f}")

  
    c.setFont("Helvetica", 10)
    c.drawString(30, 30, "Thank you for your purchase!")

    
    c.save()
    print(f"Receipt saved as {file_name}")


transaction_id = "12345"
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
customer_name = "John Doe"
items = {
    "Widget A": {"quantity": 2, "price": 10.00, "total": 20.00},
    "Widget B": {"quantity": 1, "price": 15.00, "total": 15.00},
    "Widget C": {"quantity": 3, "price": 7.50, "total": 22.50}
}
total_amount = 57.50

create_receipt(transaction_id, date, customer_name, items, total_amount)
