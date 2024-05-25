unit = input("is this temperature in Celsius, Fahrenheit or Kelvin(C/F/K) : ")
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((9 * temp / 5) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
    temp = round((temp + 273.15), 1)
    print(f"The temperature in Kelvin is: {temp}K")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
    temp = round((temp-32)*5/9 + 273.15, 1)
    print(f"The temperature in Kelvin is: {temp}K")
elif unit == "K":
    temp = round((temp - 273.15), 1)
    print(f"The temperature in Celsius is: {temp}°C")
    temp = round((temp - 273.15)*9/5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")

else:
    print(f"{unit} is an invalid unit of measurement")
