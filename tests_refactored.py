import conversions_refactored as c

def main():
  # Celsius, Kelvin, Fahrenheit

  # Yards, Meters, Miles
  distanceValues = [17600, 16093.4, 10]

  units = [('Celsius', 500), ('Fahrenheit', 932), ('Kelvin', 773.15), ('Yards', 17600), ('Meters', 16093.4), ('Miles', 10)]

  for fromTemp in units:
    print('-------------')
    print(f'Testing {fromTemp[0]} Conversions')
    print('-------------')
    for toTemp in units:
      converted = c.convert(fromTemp[0], toTemp[0], fromTemp[1])
      if isinstance(converted, float):
        passed = 'PASSED' if converted == toTemp[1] else 'FAILED'
        print(f'{fromTemp[0]} to {toTemp[0]} test: {passed}')
        print(f'Starting {fromTemp[0]} value: {fromTemp[1]}')
        print(f'Expected {toTemp[0]} value: {toTemp[1]}')
        print(f'Actual {toTemp[0]}  value: {converted}')
        print('-------------')
      else:
        print(f'Conversion Error: {converted}')
        print('-------------')


main()
