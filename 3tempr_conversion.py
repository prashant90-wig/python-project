input_unit = input("Enter your input unit (C, F, K): ").upper()
tempr = float(input("Enter your temperature: "))
output_unit = input("Enter your desired output unit (C, F, K): ").upper()

def to_celsius(temp, unit):
    if unit == 'C':
        return temp
    elif unit == 'F':
        return (temp - 32) * 5/9
    elif unit == 'K':
        return temp - 273.15
    else:
        return None

def from_celsius(temp_c, unit):
    if unit == 'C':
        return temp_c
    elif unit == 'F':
        return temp_c * 9/5 + 32
    elif unit == 'K':
        return temp_c + 273.15
    else:
        return None

if input_unit not in ['C', 'F', 'K'] or output_unit not in ['C', 'F', 'K']:
    print("Invalid unit entered.")
else:
    temp_c = to_celsius(tempr, input_unit)
    result = from_celsius(temp_c, output_unit)
    print(f"Your temperature is {result:.2f} in {output_unit}.")

# tempr = float(input("Enter your temperature :"))
# if unit == 'C':
#     result = tempr*1.8 + 32
#     print(f"Your temperature is {result :.2f} in °F.")
# elif unit == 'F':
#     result = (5*tempr-160)/9
#     print(f"Your temperature is {result :.2F} in °C.")
# else:
#     print(f"The unit {unit} is invalid!")