class PyLady:

    def __init__(self, name):
        self.name = name
        self.knowledge = 0  # max je 5
        self.max_knowledge = 5
        self.practice = 0  # max je 5
        self.max_practice = 5
        self.focus = 3  # minimum 0
        self.max_focus = 3
        self.energy = 5  # minimum 0
        self.max_energy = 5
        self.coach_capacity = 3  # min je 0
        self.max_coach_capacity = 3

    def __str__(self):
        return f"PyLady {self.name}. Její practice je {self.graficky_practice()} a knowledge {self.graficky_knowledge()}"

    def graficky_knowledge(self):
        celkem = int(self.max_knowledge)
        pocet = int(self.knowledge)
        return "[{0}{1}]".format("#"*pocet, "_" * (celkem-pocet))

    def graficky_practice(self):
        celkem = int(self.max_practice)
        pocet = int(self.practice)
        return "[{0}{1}]".format("#"*pocet, "_" * (celkem-pocet))

    def study(self, hour):
        # zvyšuje: practice a knowledge podle délky studia
        # snižuje: energy a focus, obojí nesmí být 0
        # při energy <= 0 vypíše hlášku
        # při focus <= 0 vypíše hlášku

        if self.energy > 0 and self.focus > 0:

            hour = int(hour)
            self.energy -= 1 * hour
            if self.energy <= 0:
                self.energy = 0

            self.focus -= 1 * hour
            if self.focus <= 0:
                self.focus = 0

            self.knowledge += 1/20 * hour
            self.practice += 1/10 * hour

    def homework(self):
        # musí být určitá úroveň knowledge a practice
        # nejde dělat pokud nemá energy a focus
        if self.energy > 0 and self.focus > 0:
            if self.knowledge > 0 and self.practice > 0:
                pass

    def take_advice(self):
        # vyčerpá o jednu kapacitu kouče
        # zvýší knowledge o 1
        self.coach_capacity -= 1
        self.knowledge += 1
        if self.coach_capacity <= 0:
            self.coach_capacity = 0
            print('Coach potřebuje načerpat energii')

    def eat(self):
        # zvyšuje energy, připadně focus
        self.energy += 1
        if self.energy >= self.max_energy:
            self.energy = self.max_energy

        self.focus += 0.5
        if self.focus >= self.max_focus:
            self.focus = self.max_focus

    def meditate(self):
        # zvyšuje focus
        self.focus += 0.5
        if self.focus >= self.max_focus:
            self.focus = self.max_focus

    def coffee(self):
        self.energy += 1
        if self.energy >= self.max_energy:
            self.energy = self.max_energy

        self.focus += 0.5
        if self.focus >= self.max_focus:
            self.focus = self.max_focus

    def sleep(self, hour):
        if int(hour) > 7:
            self.focus = self.max_focus
        else:
            self.focus += 0.25 * hour

    def nabití_kouce(self):
        pass

    def control(self):
        if self.energy == 0:
            print(f'{self.name} potřebuje nabrat energii. Najíst se.')
        if self.focus == 0:
            print(f'{self.name} potřebuje dělat chvilku něco jiného než se učit.')
