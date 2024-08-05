import random

class Shotgun:
    RED = "Live Round"
    BLUE = "Blank Round"

    def __init__(self, ammo, is_barrel_there=True):
        self.ammo = ammo
        self.clip = []
        self.is_barrel_there = is_barrel_there

    def load_bullets(self, stage):
        self.clip = []
        if stage == 1:
            self.clip = [Shotgun.RED, Shotgun.RED, Shotgun.BLUE, Shotgun.BLUE]
        elif stage == 2:
            self.clip = [Shotgun.RED, Shotgun.RED, Shotgun.RED, Shotgun.RED, Shotgun.BLUE, Shotgun.BLUE, Shotgun.BLUE]
            random.shuffle(self.clip)
            self.clip = self.clip[:6]
        elif stage == 3:
            self.clip = [Shotgun.RED, Shotgun.RED, Shotgun.RED, Shotgun.RED, Shotgun.BLUE, Shotgun.BLUE, Shotgun.BLUE, Shotgun.BLUE]
            random.shuffle(self.clip)
            self.clip = self.clip[:8]
        random.shuffle(self.clip)

    def current_bullet(self):
        if self.clip:
            return self.clip[0]
        return None

    def random_bullet(self):
        if self.clip:
            return random.choice(self.clip)
        return None

    def change_barrel(self):
        self.is_barrel_there = not self.is_barrel_there
        # Turn back to true after one use
        if not self.is_barrel_there:
            self.is_barrel_there = True

    def __str__(self):
        return (f"Ammo: {self.ammo}\n"
                f"Clip: {self.clip}\n"
                f"Is Barrel There: {self.is_barrel_there}\n"
                f"Current Bullet: {self.current_bullet()}")

# Example usage:
# shotgun = Shotgun(ammo=10)
# shotgun.load_bullets(stage=2)
# print(shotgun)
# print("Current Bullet:", shotgun.current_bullet())
# print("Random Bullet:", shotgun.random_bullet())
# shotgun.change_barrel()
# print("Barrel Changed:", shotgun.is_barrel_there)
