import dataclasses
import multiprocessing
import random
from dataclasses import dataclass
import os
import threading
import time
from tabulate import tabulate

import keyboard

def cs_hook(args):
    print(args)
    print("exiting program")

threading.excepthook = cs_hook

class Header:

    # key: str = ""
    # total_rounds: int = 0
    # current_round: int = 0
    # win_count: int = 0
    # loss_count: int = 0
    def __init__(self, total_rounds):
        self.key = ""
        self.total_rounds = total_rounds
        self.current_round = 1
        self.win_count = 0
        self.loss_count = 0
        self.draw_count = 0
        self.data_rounds = []
        self.temp = ""
    def __str__(self):
        if len(self.data_rounds) > 0:
            data = " \n ".join([f"u : {x[0]} , pc : {x[1]} status : {x[2]}" for x in self.data_rounds])
            self.temp += "\n"+data
            self.data_rounds = []
        if self.key == "":
            return self.temp+"\n"+f"Round {self.current_round} of {self.total_rounds} | Wins: {self.win_count} Losses: {self.loss_count} Draw: {self.draw_count}"
        else:
            return self.temp+"\n"+f"Round {self.current_round} of {self.total_rounds} | Wins: {self.win_count} Losses: {self.loss_count} | Draw: {self.draw_count} | key pressed : {self.key}"

class Threads:
    single = None

    def __new__(cls, *args, **kwargs):
        if cls.single is None:
            cls.single = super(Threads,
                               cls).__new__(cls)
        return cls.single

    def __init__(self, total_round):
        self.header = Header(total_rounds = total_round)
        self.event = threading.Event()
        self.output = Output(header = self.header,
                             event = self.event)

class Output(threading.Thread):

    def __init__(self, header, event):
        super().__init__()
        self.header = header
        self.event = event
        self.temp = ""
        self.msg = ""

    def run(self) -> None:
        while True:
            if self.temp != str(self.header) + "\n" + self.msg:
                self.temp = str(self.header) + "\n" + self.msg
                os.system("cls")
                print(self.temp)
            if self.event.is_set() == True:
                break
            time.sleep(0.1)

def get_round():
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? "))
            if rounds > 0:
                return rounds
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a number.")

def start_game(rounds):
    game = Threads(rounds)
    game.output.start()
    try:
        while game.header.current_round <= game.header.total_rounds:
            game.output.msg = "Press any key to start the round."
            # press any key to start the round
            keyboard.read_key()
            game.output.msg = "Round started."
            for i in range(3):
                game.output.msg = f"Round started. Round will start in {3 - i} seconds."
                time.sleep(1)
            game.output.msg = "Round started. Round will start in 0 seconds."
            computer = random.choice(["r", "p", "s"])
            game.output.msg +="\nPress r for rock, p for paper, s for scissors."
            while True:
                key = keyboard.read_key()
                if key in ["r", "p", "s"]:
                    break
            cond = ""
            game.output.msg = f"Round started. Round will start in 0 seconds. You pressed {key}."
            print(f"Computer pressed {computer}.")
            if key == computer:
                game.header.draw_count += 1
                cond = "draw"
                game.output.msg = f"Round started. Round will start in 0 seconds. You pressed {key}. Computer pressed {computer}. Draw!"
            elif key == "r" and computer == "s":
                game.header.win_count += 1
                cond = "win"
                game.output.msg = f"Round started. Round will start in 0 seconds. You pressed {key}. Computer pressed {computer}. You win!"
            elif key == "p" and computer == "r":
                game.header.win_count += 1
                cond = "win"
                game.output.msg = f"Round started. Round will start in 0 seconds. You pressed {key}. Computer pressed {computer}. You win!"
            elif key == "s" and computer == "p":
                game.header.win_count += 1
                cond = "win"
                game.output.msg = f"Round started. Round will start in 0 seconds. You pressed {key}. Computer pressed {computer}. You win!"
            else:
                game.header.loss_count += 1
                cond = "loss"
                game.output.msg = f"Round started. Round will start in 0 seconds. You pressed {key}. Computer pressed {computer}. You lose!"
            game.header.data_rounds.append([key, computer, cond])
            time.sleep(1)
            game.output.msg = ""
            if game.header.current_round +1 <= game.header.total_rounds:
                game.header.current_round+= 1
            else:
                break



    except KeyboardInterrupt:
        pass


    game.event.set()
    game.output.join()
    Win_rate = game.header.win_count / game.header.total_rounds * 100
    Loss_rate = game.header.loss_count / game.header.total_rounds * 100
    Draw_rate = game.header.draw_count / game.header.total_rounds * 100
    Total_rounds = game.header.total_rounds
    Total_wins = game.header.win_count
    Total_losses = game.header.loss_count
    Total_draws = game.header.draw_count
    print(tabulate([["Total Rounds", Total_rounds], ["Total Wins", Total_wins], ["Total Losses", Total_losses], ["Total Draws", Total_draws], ["Win Rate", Win_rate], ["Loss Rate", Loss_rate], ["Draw Rate", Draw_rate]],
                   headers = ["Stats", "Values"]))
    if game.header.win_count > game.header.loss_count:
        print("You win!")
    elif game.header.win_count < game.header.loss_count:
        print("You lose!")
    else:
        print("Draw!")
    print("Game Over")

if __name__ == '__main__':
    os.system("cls")
    r = get_round()
    time.sleep(0.1)
    start_game(r)
