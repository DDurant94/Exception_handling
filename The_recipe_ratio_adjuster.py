'''
2. The Recipe Ratio Adjuster
Objective: The aim of this assignment is to create a program that adjusts the quantities of a 
recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.

Use a try block to catch any arithmetic errors that may occur during the calculation.

Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.

Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

'''

# Task one


while True:
  try:
    user_input = float(input("What is the number of serving for the recipe: "))
    user_input2 = float(input("What is the number of servings that you want to make: "))
  except ValueError:
    print("Please enter a number")
  else:
    break


# Task two and three 
  
def recipe_servings_adjustment():
  print("Recipe percentage difference calculator.")
  while True:
    try:
      user_input = float(input("What is the number of serving for the recipe: "))
      user_input2 = float(input("What is the number of servings that you want to make: "))
      if user_input > user_input2:
        serving_total = user_input2 / user_input * 100
        print(f"{serving_total:.2f}%  less than the original serving size of {user_input:.2f} total.")
      elif user_input < user_input2:
        serving_total = ((user_input2 - user_input) / user_input) * 100
        print(f"{serving_total:.2f}% more than the original serving size of {user_input:.2f} total.")
    except ArithmeticError as a:
        print(f"Error: {a} check your equations.")
    except Exception as e:
      print(f"Error: {e}")
    finally:
      print(f"Thank you for converting your recipe with us.\nEnjoy your meal I hope that it is wonderful.")
      break

while True:
  user_input_start = input("Would you like to start? [Y/N] ").upper()
  if user_input_start != "Y":
    break
  else:
    recipe_servings_adjustment()
    