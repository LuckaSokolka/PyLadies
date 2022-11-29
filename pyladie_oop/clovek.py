class Clovek:
    def __init__(self, name) -> None:

        self.name = name
        self.focus = 3  # minimum 0
        self.max_focus = 3
        self.energy = 5  # minimum 0
        self.max_energy = 5

    def eat(self):
        # zvyšuje energy, připadně focus
        if self.energy >= 5 and self.focus >= 3:
            print(f"{self.name} je najezená.")
        else:
            self.energy += 1
            self.focus += 0.5
            self.max_control()

    def meditate(self):
        # zvyšuje focus
        self.focus += 0.5
        self.max_control()

    def coffee(self):
        self.focus += 0.25
        self.energy += 0.25
        self.max_control()

    def sleep(self, hour):
        print(f'{self.name} se zdá moc hezký sen.')
        if int(hour) > 7:
            self.focus = self.max_focus
        else:
            self.focus += 0.25 * hour

    def control(self):
        if self.energy <= 0:
            print(f'{self.name} potřebuje nabrat energii. Najíst se.')
        if self.focus <= 0:
            print(f'{self.name} potřebuje dělat chvilku něco jiného.')

    def max_control(self):
        if self.energy >= self.max_energy:
            self.energy = self.max_energy
        if self.focus >= self.max_focus:
            self.focus = self.max_focus
