import os
from dataclasses import dataclass, field

@dataclass
class FlamesData:
    flames_result: str = None
    name_1: str = None
    name_2: str = None
    _letters: list = field(default_factory = list)
    _msg = ""

    FLAMES = ("FRIENDS", "LOVERS", "AFFECTIONATE", "MARRIAGE", "ENEMIES", "SIBLINGS")

    def result(self):
        if self.can_play() == False:
            return "Please enter two names"

        if self.flames_result:
            return self.flames_result
        else:
            self.flames_result = process_flames(self._letters)
            return self.flames_result

    def can_play(self):
        if self.name_1 and self.name_2:
            if self._letters == []:
                self._letters = process_name(self.name_1,
                                             self.name_2)
            return True
        else:
            return False

    @property
    def letters(self):
        self.can_play()
        return self._letters

    def print(self, msg = None):
        os.system("cls")
        print(f"name 1 : {self.name_1} and {self.name_2} are {self.result()}")
        if msg:
            print(msg)
        if self._msg != "":
            print(self._msg)
            self._msg = ""

def get_name(dataframe = None) -> str:
    while True:
        if dataframe:
            dataframe.print()
        temp = input("Enter your name: ")

        if temp.isalpha():
            return temp
        else:
            if dataframe:
                dataframe._msg = "Please enter a valid name"
            else:
                print("Please enter a valid name")

def process_name(name1: str, name2: str) -> list:
    temp_name_1 = sorted(list(name1.lower().replace(" ",
                                                    "")))
    temp_name_2 = sorted(list(name2.lower().replace(" ",
                                                    "")))
    result = set([x for x in temp_name_1 + temp_name_2])
    result = {x: 0 for x in result}
    for char in temp_name_1:
        result[char] += 1
    for char in temp_name_2:
        result[char] -= 1
    res = []
    for key, value in result.items():
        if value != 0:
            for i in range(abs(value)):
                res.append(key)
    return res

def process_flames(letters: list) -> str:
    temp = list(FlamesData.FLAMES)
    while len(temp) > 1:
        index = len(letters) % len(temp)
        temp = temp[index:] + temp[:index]
        temp.pop()
    return temp[0]

if __name__ == '__main__':
    x = FlamesData()
    x.name_1 = get_name(x)
    x.name_2 = get_name(x)
    x.print()
