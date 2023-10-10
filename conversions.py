import unittest
class celsius(unittest.TestCase):
    #Celsius temperatures can be any number, but I chose numbers that are bearable for an environment#
    known_values = (29,
                    33,
                    15,
                    8,
                    24)

def test_to_temperature_known_values(self):
    for integer, number in self.known_values:
        result = integer
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = (celsius + 273.15)
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = ((celsius*9/5)+32)
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    celsius = ((fahrenheit-32)*(5/9))
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    kelvins = ((fahrenheit+459.67)*(5/9))
    return kelvins

def convertKelvinsToCelsius(kelvins):
    celsius = (kelvins-273.15)
    return celsius

def convertKelvinsToFahrenheit(kelvins):
    fahrenheit = ((kelvins*(9/5)-459.67))
    return fahrenheit