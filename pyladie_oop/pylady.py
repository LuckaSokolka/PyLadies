from clovek import Clovek


class PyLady(Clovek):
    def __init__(self, name):
        self.knowledge = 0  # max je 5
        self.max_knowledge = 5
        self.practice = 0  # max je 5
        self.max_practice = 5
        self.coach_capacity = 3  # min je 0
        self.min_coach_capacity = 0
        # self.couch = input('Vyber couche')
        super().__init__(name)

    def __str__(self):
        return f"PyLady {self.name}. Její practice je {self.graficky_practice()} a knowledge {self.graficky_knowledge()}"

    def graficky_knowledge(self):
        celkem = round(self.max_knowledge)
        pocet = round(self.knowledge)
        return "[{0}{1}]".format("#" * pocet, "_" * (celkem - pocet))

    def graficky_practice(self):
        celkem = round(self.max_practice)
        pocet = round(self.practice)
        return "[{0}{1}]".format("#" * pocet, "_" * (celkem - pocet))

    def study(self, hour):
        # zvyšuje: practice a knowledge podle délky studia
        # snižuje: energy a focus, obojí nesmí být 0
        # při energy <= 0 vypíše hlášku
        # při focus <= 0 vypíše hlášku

        hour = int(hour)
        if self.energy < hour:
            print(f'{self.name} měla energii jen na {hour - self.energy} hod. Potřebuje se posilnit.')
        if self.focus < hour:
            print(f'{self.name} se zvládla soustředit jen {hour - self.focus} hod. Je čas si odpočinout.')
        for i in range(hour):
            if self.energy >= 1 and self.focus >= 1 and self.knowledge < 5 and self.practice < 5:
                self.energy -= 1
                self.focus -= 1
                self.knowledge += 1/20
                self.practice += 1/10
            self.max_control()

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

    def max_control(self):
        if self.knowledge >= self.max_knowledge:
            self.knowledge = self.max_knowledge
        if self.practice >= self.max_practice:
            self.practice = self.max_practice
        # if self.coach_capacity >= self.max_coach_capacity:
            # self.coach_capacity = self.max_coach_capacity
        super().max_control()

    def sleep(self, hour):
        print(f'{self.name} ve snu přemýšlí, jak se bude řešit HW.')
        if int(hour) >= 5:
            self.focus = self.max_focus
        else:
            self.focus += 0.25 * hour
