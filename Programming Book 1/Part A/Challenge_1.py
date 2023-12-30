# from decimal import Decimal

# price = Decimal(input("Enter the total price "))
# numDiners = Decimal(input("Enter the total number of diners "))

# payment = price/numDiners
# result = Decimal(payment.quantize(Decimal('.01')))
# print("the total price per diner is £" + str(result))

# Ask for the total price of the bill, then ask how many diners there are. ​​​​​​​Divide the total bill by the number of diners and show how much each person must pay.

price = float(input("Enter the total price: "))
num_diners = int(input("Enter the total number of diners: "))

payment = round(price / num_diners, 2)

print(f"Each person has to pay £{payment} for the £{price:.2f} bill")
