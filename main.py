print("welcome to the tip calculator")
food_amt = float(input("How much was your food? "))

tip_amt = food_amt * 0.18

tax_amt = food_amt * 0.07

total_cost = food_amt + tip_amt + tax_amt

print(
    f"Your food costs:  ${round(food_amt, 2)},\nyour tip is ${round(tip_amt, 2)} \ntax is ${round(tax_amt, 2)}")
print("---------------------------")
print(f"Your total cost is: ${round(total_cost, 2)}")
