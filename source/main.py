from os import getenv
from pprint import pprint

import openai


openai.my_api_key = getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)


def main():
    pprint(completion)


if __name__ == "__main__":
    main()
