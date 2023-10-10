import unittest
class Celsius(unittest.TestCase):
    #Celsius temperatures can be any number, but I chose numbers that are bearable for an environment#
    celsius = (29,
               33,
               15,
               8,
               24)

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = (celsius + 273.15)
    return kelvins

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = ((celsius*9/5)+32)
    return fahrenheit
