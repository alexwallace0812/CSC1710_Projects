gallon = 19.75
cover = 200
height = float(input("Enter the height of the wall (in feet):"))
width = float(input("Enter the width of the wall (in feet):"))
gallons = ((height*width)/cover)
cost = gallon*gallons
print(f"You will need {gallons:.2f} of paint and it will cost {cost:.2f} dollars")

