def celsius_to_fahrenheit(celcius):
    return (celcius * 9/5)+32
def celsius_to_kelvin(celcius):
    return celcius+273.15
def fahrenheit_to_celcius(fah):
    return (fah-32) * 5/9
def fahrenheit_to_kelvin(fah):
    return (fah-32) * 5/9 +273.15
def kelvin_to_celcius(kelvin):
    return kelvin-273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin-273.15) * 9/5 +32

def main():
    print("enter 1 to convert from celsius to fahrenheit: ")
    print("enter 2 to convert from celsius to kelvin: ")
    print("enter 3 to convert from fahrenheit to celcius: ")
    print("enter 4 to convert from fahrenheit to kelvin: ")
    print("enter 5 to convert from kelvin to celcius: ")
    print("enter 6 to convert from kelvin to fahrenheit: ")
    
    inp=int(input("enter your choice: "))
    
    if inp==1:
        celcius=float(input("enter temp in celcius: "))
        print("temperature in fahrenheit is: ",celsius_to_fahrenheit(inp))
    if inp==2:
        celcius=float(input("enter temp in celcius: "))
        print("temperature in kelvin is: ",celsius_to_kelvin(inp))
    if inp==3:
        fahrenheit=float(input("enter temp in fahrenheit: "))
        print("temperature in celcius is: ",fahrenheit_to_celcius(inp))
    if inp==4:
        fahrenheit=float(input("enter temp in fahrenheit: "))
        print("temperature in kelvin is: ",fahrenheit_to_kelvin(inp))
    if inp==5:
        kelvin=float(input("enter temp in kelvin: "))
        print("temperature in celcius is: ",kelvin_to_celcius(inp))
    if inp==6:
        kelvin=float(input("enter temp in kelvin: "))
        print("temperature in fahrenheit is: ",kelvin_to_fahrenheit(inp))
    
main()
        