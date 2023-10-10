import unittest
class Celsius(unittest.TestCase):               ①
    celsius = (42,
               32,
               15,
               4,
               25)

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = (celsius + 273.15)
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = ((celsius*9/5)+32)
    return fahrenheit
