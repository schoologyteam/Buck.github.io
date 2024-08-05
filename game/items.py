class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, player, dealer):
        # This method will be overridden by specific item effects
        pass


class HandSaw(Item):
    def __init__(self):
        super().__init__(
            name="Hand saw",
            description="Saw the shotgun in half to deal double damage for one turn. "
                        "If successful, the dealer will lose two lives instead of one with a single shotgun bullet.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to deal double damage
        pass


class MagnifyingGlass(Item):
    def __init__(self):
        super().__init__(
            name="Magnifying glass",
            description="Checks the current round in the chamber before you choose to shoot the dealer or yourself.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to check the current round in the chamber
        pass


class CigarettePack(Item):
    def __init__(self):
        super().__init__(
            name="Cigarette pack",
            description="Regain a life.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to regain a life
        pass


class Handcuffs(Item):
    def __init__(self):
        super().__init__(
            name="Handcuffs",
            description="Check the current round in the chamber before you choose to shoot the dealer or yourself.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to check the current round in the chamber
        pass


class Beer(Item):
    def __init__(self):
        super().__init__(
            name="Beer",
            description="Rack the shotgun to remove the bullet from the chamber, regardless of whether it’s a blank or live.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to rack the shotgun and remove the bullet
        pass


class Pills(Item):
    def __init__(self):
        super().__init__(
            name="Pills",
            description="Take it inside the bathroom at the beginning of the game to enter Double or Nothing mode.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to enter Double or Nothing mode
        pass


class Adrenaline(Item):
    def __init__(self):
        super().__init__(
            name="Adrenaline",
            description="Steal an item from the Dealer and use it immediately.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to steal an item from the dealer and use it
        pass


class Inverter(Item):
    def __init__(self):
        super().__init__(
            name="Inverter",
            description="Switches the shell in the chamber to the opposite effect. If it’s a blank it will become a live round, while a live round will swap to a blank.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to switch the shell in the chamber to the opposite effect
        pass


class ExpiredMedicine(Item):
    def __init__(self):
        super().__init__(
            name="Expired Medicine",
            description="40 percent chance to regain two charges (lives). You lose a charge if you fail.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to regain two charges or lose a charge
        pass


class BurnerPhone(Item):
    def __init__(self):
        super().__init__(
            name="Burner Phone",
            description="Receive a call, identifying a random shell in the sequence as a live or blank round.",
            effect=self.use
        )

    def use(self, player, dealer):
        # Logic to identify a random shell in the sequence
        pass

# Example usage:
# hand_saw = HandSaw()
# magnifying_glass = MagnifyingGlass()
# cigarette_pack = CigarettePack()
# handcuffs = Handcuffs()
# beer = Beer()
# pills = Pills()
# adrenaline = Adrenaline()
# inverter = Inverter()
# expired_medicine = ExpiredMedicine()
# burner_phone = BurnerPhone()

# items = [hand_saw, magnifying_glass, cigarette_pack, handcuffs, beer, pills, adrenaline, inverter, expired_medicine, burner_phone]
