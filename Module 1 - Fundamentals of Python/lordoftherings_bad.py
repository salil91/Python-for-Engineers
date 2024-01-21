class Character:
    def __init__(self, name, weapon, health):
        self.name = name
        self.weapon = weapon
        self.health = health

    # Getter for health
    @property
    def health(self):
        return self._health

    # Setter for health
    @health.setter
    def health(self, health):
        if health > self.max_health:
            raise ValueError(f"Maximum health for {self.race}: {self.max_health}")
        self._health = health

    # Reduce health
    def take_damage(self, damage):
        current_health = self.health - damage
        if current_health <= 0:
            self.health = 0
            print(f"{self.name} has died.")
        else:
            self.health = current_health

    # Increase health
    def get_heal(self, heal_amount):
        current_health = self.health + heal_amount
        if current_health > self.max_health:
            self.health = self.max_health
        else:
            self.health = current_health


class Elf(Character):
    def __init__(self, name, weapon, health):
        self.race = "Elf"
        self.max_health = 80
        super().__init__(name, weapon, health)

    def __str__(self):
        return f"{self.name} is a {self.race} who fights with a {self.weapon}. HP = {self.health} / {self.max_health}"


class Dwarf(Character):
    def __init__(self, name, weapon, health):
        self.race = "Dwarf"
        self.max_health = 150
        super().__init__(name, weapon, health)

    def __str__(self):
        return f"{self.name} is a {self.race} who fights with a {self.weapon}. HP = {self.health} / {self.max_health}"


class Ainur(Character):
    def __init__(self, name, weapon, health, mana):
        self.race = "Ainur"
        self.max_health = 100
        super().__init__(name, weapon, health)
        self.max_mana = 100
        self.mana = mana

    # Getter for mana
    @property
    def mana(self):
        return self._mana

    # Setter for mana
    @mana.setter
    def mana(self, mana):
        if mana > self.max_mana:
            raise ValueError(f"Maximum mana for {self.race}: {self.max_mana}")
        self._mana = mana

    def __str__(self):
        return f"{self.name} is a {self.race} who fights with a {self.weapon}. HP = {self.health} / {self.max_health}. MP = {self.mana} / {self.max_mana}"

    def heal(self, target, heal_amount):
        mana_cost = heal_amount * 2
        if self.mana < mana_cost:
            print(
                f"{self.name} cannot heal for {heal_amount} HP. Insufficient mana. Needs {mana_cost}, has {self.mana}."
            )
        else:
            print(f"{self.name} heals {target.name} for {heal_amount} HP.")
            self.mana = self.mana - mana_cost
            target.get_heal(heal_amount)
