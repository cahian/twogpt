import sys
from enum import Enum
from os import getenv
from pprint import pprint

import openai
from colorama import Fore, Back, Style

from .config import config

openai.my_api_key = getenv("OPENAI_API_KEY")
INDENT = '   '


def optinput(prompt, test, cast):
    while True:
        try:
            string = input(prompt)
            if test(cast(string)):
                return cast(string)
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass


def separate():
    print("")


class TwoMessages:
    def __init__(self, sysmsg1, sysmsg2):
        self._msgs = []
        self._add("system", sysmsg1)
        self._mode = 1
        self._sysmsg1 = sysmsg1
        self._sysmsg2 = sysmsg2

    def get(self):
        return self._msgs

    def get_mode(self):
        return self._mode

    def add_user(self, content):
        self._add("user", content)

    def add_assistant(self, content):
        self._add("assistant", content)

    def swap_roles(self):
        msgs_iter = iter(self._msgs)
        new_msgs = []

        sysmsg = next(msgs_iter)
        self._mode = 2 if self._mode == 1 else 1
        match sysmsg["content"]:
            case self._sysmsg1:
                sysmsg["content"] = self._sysmsg2
            case self._sysmsg2:
                sysmsg["content"] = self._sysmsg1
        new_msgs.append(sysmsg)

        for msg in msgs_iter:
            match msg["role"]:
                case "user":
                    msg["role"] = "assistant"
                case "assistant":
                    msg["role"] = "user"
            new_msgs.append(msg)

    def _add(self, role, content):
        self._msgs.append({"role": role, "content": content})


def main():
    print("Do you want a predefined prompt or a custom one?")
    option = optinput("Enter 1 for predefined and 2 for custom: ",
            lambda n: n in [1, 2], int)
    separate()

    match option:
        case 1:
            iniprompts = config["initial_prompts"]
            inilength = len(iniprompts)
            for index, iniprompt in enumerate(iniprompts):
                print(f"Predefined prompt {index + 1}:")
                print(f"{INDENT}{Fore.BLUE}ChatGPT1{Fore.RESET}: {iniprompt['ChatGPT1']}")
                print(f"{INDENT}{Fore.RED}ChatGPT2{Fore.RESET}: {iniprompt['ChatGPT2']}")
            separate()

            print("Which predefined initial prompt do you want?")
            option2 = optinput(f"Enter a predefined prompt number from 1 to {inilength}: ",
                    lambda n: n >= 1 and n <= inilength, int)

            iniprompts = iniprompts[option2 - 1]
            iniprompt1 = iniprompts["ChatGPT1"]
            iniprompt2 = iniprompts["ChatGPT2"]
        case 2:
            iniprompt1 = input("Enter {Fore.BLUE}ChatGPT1{Fore.RESET}initial prompt: ")
            iniprompt2 = input("Enter {Fore.RED}ChatGPT2{Fore.RESET}initial prompt: ")
    separate()

    twomsgs = TwoMessages(iniprompt1, iniprompt2)
    while True:
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=twomsgs.get(),
            temperature=0.8
        )
        reply = chat.choices[0].message.content
        print(f"{Fore.BLUE if twomsgs.get_mode() == 1 else Fore.RED}ChatGPT{twomsgs.get_mode()}{Fore.RESET}: {reply}")
        twomsgs.add_assistant(reply)
        twomsgs.swap_roles()
        input("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit()

