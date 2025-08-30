unit = input(" Enter the unit to convert (km/miles)").strip().lower()
if unit == 'km':
    value  = float(input("Enter the distance in kilometers:"))
    result = value * 0.621
    print(f"{value} km in Miles is {result:.2f} miles.")
elif unit == 'miles':
    value  = float(input("Enter the distance in miles:"))
    result = value / 0.621
    print(f"{value} miles in Kilometers is {result:.2f} km.")
