def tempConv(num,unit):
    if unit == 'F' or unit == 'f':
        temp = ((float(num) - 32) * (5 / 9))
        converted_temp = str(round(temp, 1)) + "°C"
        return converted_temp
    elif unit == 'C' or unit == 'c':
        temp = ((float(num) * (9/5) + 32))
        converted_temp = str(round(temp, 1)) + "°F"
        return converted_temp
    else:
        error = 'Something went wrong with your request. Valid entries are either "C" for Celcius, or "F" for Fahrenheit.'
        return error

tempInput = input("Enter a temperature: ")
unitInput = input("Is this Fahrenheit or Celsius? Enter F for Fahrenheit or C for Celsius: ")

print(tempConv(tempInput,unitInput))