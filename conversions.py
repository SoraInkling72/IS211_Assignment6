import unittest
class celsius(unittest.TestCase):
    #Celsius temperatures can be any number, but I chose numbers that are bearable for an environment#
    known_values = (29,
                    33,
                    15,
                    8,
                    24)

def test_to_temperature_known_values(self):
    '''to_roman should give known result with known input'''
    for integer, numeral in self.known_values:
        result = roman1.to_roman(integer)
        self.assertEqual(numeral, result)

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
