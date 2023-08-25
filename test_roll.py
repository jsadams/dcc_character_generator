import unittest
import roll

class TestRoll(unittest.TestCase):

    def test_3d6(self):

        s="3d6"
        [n_dice,n_sides]=roll.roll_string_to_n_dice_and_n_sides(s)



        n_dice_expected=3
        n_sides_expected=6
        
        self.assertEqual(n_dice, n_dice_expected, f"failed n_dice on {s}")
        self.assertEqual(n_sides, n_sides_expected, f"failed n_sides on {s}")
        
    def test_d6(self):

        s="d6"
        [n_dice,n_sides]=roll.roll_string_to_n_dice_and_n_sides(s)



        n_dice_expected=1
        n_sides_expected=6
        
        self.assertEqual(n_dice, n_dice_expected, f"failed n_dice on {s}")
        self.assertEqual(n_sides, n_sides_expected, f"failed n_sides on {s}")

    def test_6(self):

        s="6"
        [n_dice,n_sides]=roll.roll_string_to_n_dice_and_n_sides(s)



        n_dice_expected=1
        n_sides_expected=6
        
        self.assertEqual(n_dice, n_dice_expected, f"failed n_dice on {s}")
        self.assertEqual(n_sides, n_sides_expected, f"failed n_sides on {s}")



if __name__ == '__main__':
    unittest.main()
