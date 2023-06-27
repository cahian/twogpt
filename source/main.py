from os import getenv
from pprint import pprint

import openai

openai.my_api_key = getenv("OPENAI_API_KEY")
messages = []


def main():
    while True:
        message = input("User: ")
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
            messages=messages
            )
        reply = chat.choices[0].message.content
        print(f"Assistant: {reply}")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()

