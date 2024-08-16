print("Welcome to the tip calculator\n")
bill = float(input("what was the total bill?$"))
tip  = int(input("How Much percentation tip woild you like to give?"))
people = int(input("People to split bill?"))

total_bill = bill * (tip / 100)
total_keseluruhan = bill + total_bill
person = round(total_keseluruhan / people, 2)


print(f"Each People Should Pay ${person}")






