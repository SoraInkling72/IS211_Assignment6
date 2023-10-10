import unittest
class meters(unittest.TestCase):
    #Meters can be any number, but I chose this unit as it's easier to use for smaller units#
    known_values = (29,
                    33,
                    15,
                    8,
                    24)

def test_to_measurments_known_values(self):
    '''to_roman should give known result with known input'''
    for integer, number in self.known_values:
        result = integer
        self.assertEqual(result)

if __name__ == '__main__':
    unittest.main()
