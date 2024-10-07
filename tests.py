import conversions as c

def Tests():
  passed = 'PASSED'
  failed = 'FAILED'
  # Celsius, Kelvin, Fahrenheit
  knownValues = [[500, 773.15, 932], [400,673.15, 752], [200, 473.15, 392], [100, 373.15, 212], [0, 273.15, 32]]
  # Celsius Tests
  print('------------------------')
  print('Testing Celsius Conversions')
  for values in knownValues:
    celsius = values[0]
    kelvin = values[1]
    fahrenheit = values[2]
    cToK = c.convertCelsiusToKelvin(celsius)
    cToF = c.convertCelsiusToFahrenheit(celsius)



    if cToK == kelvin:
      cToKBool = passed
    else:
      cToKBool = failed

    if cToF == fahrenheit:
      cToFBool = passed
    else:
      cToFBool = failed

    print('------------------------')
    print(f'Starting Celsius Value: {celsius}')
    print(f'Celsius to Kelvin Test {cToKBool}\nExected Kelvin value: {kelvin}\nActual Kelvin value: {cToK}')
    print(f'Celsius to Fahrenheit Test {cToFBool}\nExected Fahrenheit value: {fahrenheit}\nActual Fahrenheit value: {cToF}')
    print('------------------------')

  # Fahrenheit Tets
  print('------------------------')
  print('Testing Fahrenheit Conversions')
  for values in knownValues:
    celsius = values[0]
    kelvin = values[1]
    fahrenheit = values[2]

    fToC = c.convertFahrenheitToCelsius(fahrenheit)
    fToK = c.convertFahrenheitToKelvin(fahrenheit)

    if fToC == celsius:
      fToCBool = passed
    else:
      fToCBool = failed

    if fToK == kelvin:
      fToKBool = passed
    else:
      fToKBool = failed

    print('------------------------')
    print(f'Starting Fahrenheit Value: {fahrenheit}')
    print(f'Fahrenheit to Kelvin Test {fToKBool}\nExected Kelvin value: {kelvin}\nActual Kelvin value: {fToK}')
    print(f'Fahrenheit to Celsius Test {fToCBool}\nExected Celsius value: {celsius}\nActual Celsius value: {fToC}')
    print('------------------------')

  # Kelvin Tests
  print('------------------------')
  print('Testing Kelvin Conversions')
  for values in knownValues:
    celsius = values[0]
    kelvin = values[1]
    fahrenheit = values[2]

    kToC = c.convertKelvinToCelsius(kelvin)
    kToF = c.convertKelvinToFahrenheit(kelvin)

    if kToC == celsius:
      kToCBool = passed
    else:
      kToCBool = failed

    if kToF == fahrenheit:
      kToFBool = passed
    else:
      kToFBool = failed

    print('------------------------')
    print(f'Starting Kelvin Value: {kelvin}')
    print(f'Kelvin to Celsius Test {kToCBool}\nExected Celsius value: {celsius}\nActual Celsius value: {kToC}')
    print(f'Kelvin to Fahrenheit Test {kToFBool}\nExected Fahrenheit value: {fahrenheit}\nActual Fahrenheit value: {kToF}')
    print('------------------------')



def main():
  Tests()
main()
