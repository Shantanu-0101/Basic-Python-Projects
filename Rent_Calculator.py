#rent Calculator

rent = int(input("enter the rent amount = "))
food = int(input("enter the amount of food ordered ="))
electricity_spend = int(input("enter the amount of electricity spend = "))
charge_per_unit = int(input("enter the charges per unit =  "))
persons = int(input("enter the number of persons in the room = "))

total_bill = electricity_spend *charge_per_unit

output = (rent + food + total_bill) // persons

print("each person will pay= ", output)