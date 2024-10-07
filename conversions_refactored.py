conversions = {
  'celsiusTokelvin': lambda c : c + 273.15,
  'celsiusTofahrenheit': lambda c : c * (9/5) + 32,
  'fahrenheitTocelsius': lambda f : (f - 32) * (5/9),
  'fahrenheitTokelvin': lambda f : (f + 459.67) * (5/9),
  'kelvinTocelsius': lambda k : k - 273.15,
  'kelvinTofahrenheit': lambda k : k * (9/5) - 459.67,
  'milesToyards': lambda m : m * 1760,
  'milesTometers': lambda m : m * 1609.34,
  'metersTomiles': lambda m : m / 1609.34,
  'metersToyards': lambda m : m * 1.09361,
  'yardsTomiles': lambda y : y / 1760,
  'yardsTometers': lambda y : y / 1.09361
}

class ConversionNotPossible(Exception):
  pass

def convert(fromUnit, toUnit, value):
  if (fromUnit.lower() == toUnit.lower()):
    return float(value)

  conversion = fromUnit.lower() + 'To' + toUnit.lower()

  if conversion in conversions:
    return round(float(conversions[conversion](value)),2)
  else:
    return ConversionNotPossible(f'Cannot convert from {fromUnit} to {toUnit}')
