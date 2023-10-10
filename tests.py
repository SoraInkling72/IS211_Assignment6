import unittest
class meters(unittest.TestCase):
    #Meters can be any number, but I chose this unit as it's easier to use for smaller units#
    known_values = (345,
                    12866,
                    18,
                    577,
                    248752879)

def test_to_measurments_known_values(self):
    for integer, number in self.known_values:
        result = integer
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()

def convertMetersToYards(meters):
    yards = (meters/0.9144)
    return yards

def convertMetersToMiles(meters):
    miles = (meters/1609.344)
    return miles

def convertYardsToMeters(yards):
    meters = (yards*0.9144)
    return meters

def convertYardsToMiles(yards):
    miles = (yards/1760)
    return miles

def convertMilesToYards(miles):
    yards = (miles*1760)
    return yards

def convertMilesToMeters(miles):
    meters = (miles*1609.344)
    return meters