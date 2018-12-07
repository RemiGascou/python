import time

class loadbar(object):
    """docstring for loadbar."""
    def __init__(self, length):
        super(loadbar, self).__init__()
        self.length = length
        self.bar = "[>" + " "*(self.length) + "]"

    def updatebar(self, current):
        if current >= 1 : current = 1
        elif current < 0: current = 0
        a = int((self.length * 10) * current)
        endedcells = (a // 10)
        self.bar = "[" + "="*(endedcells) + ">" + " "*((self.length) - endedcells) + "]"

    def show(self, current, text=""):
        self.updatebar(current)
        print("\r" + text + self.bar, end="")


if __name__ == '__main__':
    l = loadbar(25)

    max = 17
    for k in range(max+1):
        adv = k/max
        l.show(adv, "Currently at " + str(int(adv*100)).rjust(3, " ") + "% : ")
        time.sleep (125.0 / 1000.0);
