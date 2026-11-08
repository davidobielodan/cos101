#PSEUDO CODE
#START
    #READ temperature in Celsius
    #CALCULATE Fahrenheit AS (Celsius × 9 / 5) + 32
    #DISPLAY temperature in Fahrenheit
#STOP

celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius:.2f} degrees Celsius = "
f"{fahrenheit:.2f} degrees Fahrenheit")
