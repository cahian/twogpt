from enum import Enum
from os import getenv
from pprint import pprint

import openai

from .config import config

openai.my_api_key = getenv("OPENAI_API_KEY")


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
    print(config)
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

