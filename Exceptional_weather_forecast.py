'''
1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling by 
creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly error message if the user 
enters something that can't be converted to a number.

Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.

Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is 
displayed regardless of whether an exception was caught or not.
'''


# Task one
'''
def fahrenheit_temp():
  while True:
    try:
      user_input = float(input("Enter the temperature in Fahrenheit: "))
      return f"{user_input} was recorded for save keeping."  
    except ValueError:
      print("Please enter in a number.")

while True:
  continue_input = input("Would your like to continue? [Y/N] ").upper()
  if continue_input != "Y":
    break
  else:
    result = fahrenheit_temp()
    print(result)

# Task two
    
def temperature_conversion():
  try:
    user_input = float(input("Enter the temperature that your would like to convert to Celsius: "))
    conversion = (user_input - 32) * 5/9
    return f"{user_input} degrees Fahrenheit was converted to {conversion:.2f} degrees Celsius."
    
  except ValueError:
    print("Please Enter a number!")
  except ZeroDivisionError as zd:
    print(f"{zd} Error: Cant divide by zero.")
  except OverflowError as of:
    print(f"{of} Error: Too many numbers to handle. ")



while True:
  continue_input = input("Would your like to continue? [Y/N] ").upper()
  if continue_input != "Y":
    break
  else:
    result = temperature_conversion()
    print(result)
'''

# Task Three


def temperature_conversion():
        try:
          user_input = float(input("Enter the temperature that your would like to convert to Celsius: "))
          conversion = (user_input - 32) * 5/9
        except ValueError:
          print("Please Enter a number!")
        except ZeroDivisionError as zd:
          print(f"{zd} Error: Cant divide by zero.")
        except OverflowError as of:
          print(f"{of} Error: Too many numbers to handle. ")
        else:
          print(f"{user_input} degrees Fahrenheit was converted to {conversion:.2f} degrees Celsius.")
        finally:
           print("Thank you for using our weather app!") 

while True:
  continue_input = input("Would your like to continue? [Y/N] ").upper()
  if continue_input != "Y":
    break
  else:
    temperature_conversion()