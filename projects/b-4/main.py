import os
from dataclasses import dataclass, field




@dataclass
class FlamesData:
    flames_result: str
    name_1: str = None
    name_2: str = None
    letters: list = field(default_factory = list)

    FLAMES = ("FRIENDS", "LOVERS", "AFFECTIONATE", "MARRIAGE", "ENEMIES", "SIBLINGS")

    def result(self):
        if self.can_play() == False:
            return "Please enter two names"

        if self.flames_result:
            return self.flames_result
        else:
            self.flames_result = process_flames(self.letters)
            return self.flames_result

    def can_play(self):
        if self.name_1 and self.name_2:
            if self.letters == []:
                self.letters = process_name(self.name_1,
                                            self.name_2)
            return True
        else:
            return False

    def print(self,msg=None):
        os.system("clear")
        print(f"name 1 : {self.name_1} and {self.name_2} are {self.result()}")
        if msg:
            print(msg)

def get_name():
    while True:
        temp = input("Enter your name: ")
        if temp.isalpha():
            return temp
        else:
            print("Please enter a valid name")

# todo process name : function gets two names and remove duplicated letters from them and return one list
def process_name(name1: str, name2: str) -> list:
    pass

# todo process flames : function gets a list of letters and return the result of flames game
def process_flames(letters: list) -> str:
    pass

# todo main
if __name__ == '__main__':
    pass
