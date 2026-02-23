# # Input we need to from the users
# total flat rent
# total fridge rent
# total food order and snacking
# electricity units spends
# charge per unit
# person living in flat


# outputs
# total amount you've to pay is

rent=int(input("Enter your flat rent :"))
fridge_rent=int(input("Enter your fridge rent :"))
food=int(input("Enter the amount of food ordered :"))
electricity_spend=int(input("Enter the total electricity_spend :"))
charge_per_unit=float(input("Enter the charge per unit :"))
person=int(input("Enter the number od person living in flat :"))

total_bill=electricity_spend*charge_per_unit

result=(rent+food+fridge_rent+total_bill) /person

print("Each person will pay",result)