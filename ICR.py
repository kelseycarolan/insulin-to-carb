print("Let's calculate your insulin-to-carb ratio")
print("Ready?")
total_daily_insulin_dose = raw_input('What is your total amount of insulin taken in one day, including long-acting, short-acting, or rapid- acting insulin? ')
body_weight = raw_input('What is your weight in pounds? ')
grams_carb_covered_per_1_unit_insulin = 500 / int(total_daily_insulin_dose)
print("The number of grams of carbohydrate covered by 1 unit of your rapid-acting insulin without taking into account your body weight is " + str(grams_carb_covered_per_1_unit_insulin))
grams_carb_covered_per_1_unit_insulin2 = 2.8*int(body_weight) / int(total_daily_insulin_dose)
print("The number of grams covered of carbohydrate by 1 unit of your rapid-acting insulin taking into account your weight is " + str(grams_carb_covered_per_1_unit_insulin2))

print("Now let's calculate your insulin sensitivity factor ")
sensitivity_factor = 1700 / int(total_daily_insulin_dose)
print("Your estimated insulin sensitivity factor is " + str(sensitivity_factor) + " mg/dl ")
print("In other words, it is estimated that 1 unit of your rapid-acting insulin will lower your blood sugar by " + str(sensitivity_factor) + " mg/dl ")

print("Insulin-to-carbohydrate ratios can be used to calculate a rapid acting insulin dose to cover a rise in blood sugar from a meal. Let's try calculating a dose ")
total_carbohydrate = raw_input("How many grams of carbohydrate will eat at this meal? ")
units_of_insulin_to_give = float(total_carbohydrate) / grams_carb_covered_per_1_unit_insulin2
print("The amount of insulin to give to cover the rise in blood sugar for this meal is " + str(units_of_insulin_to_give) + "units ")

print("If blood sugar is higher than 130 mg/dL before a meal, an insulin sensitivity or correction factor will allow you to calculate the amount of insulin needed to correct high blood sugar ")
target_blood_sugar = raw_input("What is your target blood sugar? ")


import csv

with open('/users/kcarolan/desktop/raw_data', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow([total_daily_insulin_dose, body_weight, grams_carb_covered_per_1_unit_insulin, grams_carb_covered_per_1_unit_insulin2, sensitivity_factor, total_carbohydrate, units_of_insulin_to_give, target_blood_sugar])