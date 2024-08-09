# Let's write the test cases to thoroughly check the functionality of the Dealer class

import unittest
from game.dealer import Dealer

class TestDealer(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer()

    def test_initial_state(self):
        self.assertEqual(self.dealer.lives, 0)
        self.assertEqual(self.dealer.dealer_items, [])
        self.assertIsNone(self.dealer.last_bullet)
        self.assertFalse(self.dealer.handcuffed)
    
    def test_assign_life_to_dealer(self):
        # Test round 1
        self.dealer.assign_life_to_dealer(1)
        self.assertEqual(self.dealer.lives, 2)
        
        # Test round 2
        self.dealer.assign_life_to_dealer(2)
        self.assertEqual(self.dealer.lives, 4)
        
        # Test round 3
        self.dealer.assign_life_to_dealer(3)
        self.assertEqual(self.dealer.lives, 6)
    
    def test_assign_items_to_dealer_round_1(self):
        # No items should be added in round 1
        self.dealer.assign_items_to_dealer(1)
        self.assertEqual(len(self.dealer.dealer_items), 0)
    
    def test_assign_items_to_dealer_round_2(self):
        # 2 items should be added in round 2
        self.dealer.assign_items_to_dealer(2)
        self.assertEqual(len(self.dealer.dealer_items), 2)
    
    def test_assign_items_to_dealer_round_3(self):
        # 4 items should be added in round 3
        self.dealer.assign_items_to_dealer(3)
        self.assertEqual(len(self.dealer.dealer_items), 4)
    
    def test_assign_items_to_dealer_max_items(self):
        # Adding more items should not exceed 8 items in total
        self.dealer.assign_items_to_dealer(3)
        self.dealer.assign_items_to_dealer(3)  # Repeating to check if it prevents exceeding
        self.assertEqual(len(self.dealer.dealer_items), 8)
    
    def test_clear_items(self):
        # Clearing items should remove all items from dealer's inventory
        self.dealer.assign_items_to_dealer(3)
        self.dealer.clear_items()
        self.assertEqual(self.dealer.dealer_items, [])
    
    def test_remove_item(self):
        # Test removing an item from the dealer's inventory
        self.dealer.assign_items_to_dealer(3)
        item_to_remove = self.dealer.dealer_items[0]
        self.dealer.remove_item(item_to_remove)
        self.assertNotIn(item_to_remove, self.dealer.dealer_items)
    
    def test_dealer_has_life(self):
        # Test if dealer has life
        self.dealer.assign_life_to_dealer(1)
        self.assertTrue(self.dealer.dealer_has_life())
    
    def test_show_lives(self):
        # Test showing lives
        self.dealer.assign_life_to_dealer(1)
        self.assertEqual(self.dealer.lives, 2)
    
    def test_last_known_bullet(self):
        # Test last known bullet is initially None
        self.assertIsNone(self.dealer.last_known_bullet())
    
    def test_show_all_items(self):
        # Test showing all items
        self.dealer.assign_items_to_dealer(2)
        self.assertEqual(len(self.dealer.dealer_items), 2)
    
    def test_is_item_present(self):
        # Test checking if an item is present
        self.dealer.assign_items_to_dealer(3)
        item = self.dealer.dealer_items[0]
        self.assertTrue(self.dealer.is_item_present(item))
        self.assertFalse(self.dealer.is_item_present("NonExistentItem"))

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
