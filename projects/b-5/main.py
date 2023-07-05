import threading
import time

import keyboard

# todo program threads
class Threds:
    class Keyboard(threading.Thread):

        def __init__(self):
            super(Threds.Keyboard,
                  self).__init__()
            self.sig = threading.Event()
            self.data = ""
            self.temp = ""

        def run(self) -> None:
            while self.sig.is_set() is False:
                self.temp = keyboard.read_key()
                if self.temp in ['r', 'p', 's', 'esc']:
                    self.data = self.temp
                    self.temp = ""
                    if self.data == "esc":
                        self.sig.set()
                        break
                else:
                    time.sleep(0.1)
            

    # todo output printing thread
    class Output(threading.Thread):
        pass

    # todo game mechanics thread
    class Mechanics(threading.Thread):
        pass

if __name__ == '__main__':
    pass
