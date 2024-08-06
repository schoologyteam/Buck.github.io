import random
class Shotgun:
    RED = "Live Round"
    BLUE = "Blank Round"

    def __init__(self, is_barrel_there=True):
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

    def shoot(self, target):
        if self.clip:
            bullet = self.clip.pop(0)
            
            if bullet == Shotgun.RED:
                print("It was a live round")
                if self.is_barrel_there:
                    target.lives -= 1
                else:
                    target.lives -= 2
            if bullet == Shotgun.BLUE:
                print("It was a blank round.")
            self.is_barrel_there = True
            