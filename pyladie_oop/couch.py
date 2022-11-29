from clovek import Clovek


class Couch(Clovek):
    def nabití_kouce(self):
        pass

    def sleep(self, hour):
        print(f'{self.name} SPÍ! Je offline, na otázky odpoví, až se probudí :) ')
        if int(hour) < 5:
            self.focus = self.max_focus
        else:
            self.focus += 0.25 * hour
