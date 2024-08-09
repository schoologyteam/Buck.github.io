from game.dealer import Dealer
dealer = Dealer()

# Test initial state
assert dealer.lives == 0, "Initial lives should be 0"
assert dealer.dealer_items == [], "Initial items should be an empty list"
assert dealer.last_bullet is None, "Initial last_bullet should be None"
assert not dealer.handcuffed, "Initial handcuffed state should be False"

# Test assign_life_to_dealer
dealer.assign_life_to_dealer(1)
assert dealer.lives == 2, "Lives should be 2 after round 1"
dealer.assign_life_to_dealer(2)
assert dealer.lives == 4, "Lives should be 4 after round 2"
dealer.assign_life_to_dealer(3)
assert dealer.lives == 6, "Lives should be 6 after round 3"

# Test assign_items_to_dealer
dealer.assign_items_to_dealer(1)
assert len(dealer.dealer_items) == 0, "No items should be added in round 1"
dealer.assign_items_to_dealer(2)
assert len(dealer.dealer_items) == 2, "2 items should be added in round 2"
dealer.assign_items_to_dealer(3)
assert len(dealer.dealer_items) == 6, "4 more items should be added in round 3"
dealer.assign_items_to_dealer(3)
assert len(dealer.dealer_items) == 8, "Total items should be capped at 8"

# Test clear_items
dealer.clear_items()
assert dealer.dealer_items == [], "Items should be cleared"

# Test remove_item
dealer.assign_items_to_dealer(3)
item_to_remove = dealer.dealer_items[0]
dealer.remove_item(item_to_remove)
assert item_to_remove not in dealer.dealer_items, "Item should be removed from dealer items"

# Test dealer_has_life
assert dealer.dealer_has_life() == True, "Dealer should have life"

# Test last_known_bullet
assert dealer.last_known_bullet() is None, "Last known bullet should be None initially"

# Test is_item_present
assert dealer.is_item_present(dealer.dealer_items[0]) == True, "Item should be present in dealer items"
assert dealer.is_item_present("NonExistentItem") == False, "Non-existent item should not be present"

# If all assertions pass:
print("All test cases passed!")