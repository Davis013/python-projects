def getTemp(type):
    type = input("Please Enter Temperature Type: ").upper()
    temp = float(input("Please Enter Temperature: "))
    if type == "C":
        tempC = 5/9 * (temp - 32)
        return tempC
    elif type == "F":
        tempF = (temp * 1.8) + 32
        return tempF
    else:
        return "Invalid Temperature Type"


print("Temperature in Celsius: ", getTemp('C'))
print("Temperature in Fahrenheit: ", getTemp('F'))
