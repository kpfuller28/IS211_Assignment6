
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15

    return round(kelvins, 2)


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius *(9/5) + 32)

    return round(fahrenheit, 2)

def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)

    return round(celsius)

def convertFahrenheitToKelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * (5/9)

    return round(kelvin, 2)

def convertKelvinToCelsius(kelvin):
    celsius = kelvin - 273.15

    return round(celsius)

def convertKelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin * (9/5) - 459.67)

    return round(fahrenheit)