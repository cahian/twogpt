import sys
from enum import Enum
from os import getenv
from pprint import pprint

import openai

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
    def __init__(sysmsg1, sysmsg2):
        self._msgs = []
        self._add("system", sysmsg1)
        self._sysmsg1 = sysmsg1
        self._sysmsg2 = sysmsg2

    def add_user(content):
        self._add("user", content)

    def add_assistant(content):
        self._add("assistant", content)

    def swap_roles():
        msgs_iter = iter(self._msgs)
        new_msgs = []

        sysmsg = next(msgs_iter)
        match sysmsg:
            case self._sysmsg1:
                sysmsg = self._sysmsg2
            case self._sysmsg2:
                sysmsg = self._sysmsg1
        new_msgs.append(sysmsg)

        for msg in msgs_iter:
            match msg["role"]:
                case "user":
                    msg["role"] = "assistant"
                case "assistant":
                    msg["role"] = "user"
            new_msgs.append(msg)

    def _add(role, content):
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
                print(f"{INDENT}ChatGPT1: {iniprompt['ChatGPT1']}")
                print(f"{INDENT}ChatGPT2: {iniprompt['ChatGPT2']}")
            separate()

            print("Which predefined initial prompt do you want?")
            option2 = optinput(f"Enter a predefined prompt number from 1 to {inilength}: ",
                    lambda n: n >= 1 and n <= inilength, int)

            iniprompts = iniprompts[option2 - 1]
            iniprompt1 = iniprompts["ChatGPT1"]
            iniprompt2 = iniprompts["ChatGPT2"]
        case 2:
            iniprompt1 = input("Enter ChatGPT1 initial prompt: ")
            iniprompt2 = input("Enter ChatGPT2 initial prompt: ")


    # while True:
    # while True:
    #     message = input("User: ")
    #     if message:
    #         messages.append(
    #             {"role": "user", "content": message},
    #         )
    #         chat = openai.ChatCompletion.create(
    #             model="gpt-3.5-turbo",
    #             messages=messages
    #         )
    #     reply = chat.choices[0].message.content
    #     print(f"Assistant: {reply}")
    #     messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()

