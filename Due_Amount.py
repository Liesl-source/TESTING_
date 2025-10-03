def calculate_due_amount(total_bill_amount, amount_paid):
 
  due_amount = total_bill_amount - amount_paid
  return due_amount

 # Get total bill amount from the user
total_bill_amount = float(input("Enter the total bill amount: "))

    # Get amount paid by the customer
amount_paid = float(input("Enter the amount paid by the customer: "))

remaining_due = calculate_due_amount(total_bill_amount, amount_paid)
  # Display the result
if remaining_due > 0:
      print(f"Customer still owes: ${remaining_due}")
elif remaining_due < 0:
      print(f"Change to be returned to the customer: ${abs(remaining_due)}")
else:
      print("The bill has been fully paid.")

 