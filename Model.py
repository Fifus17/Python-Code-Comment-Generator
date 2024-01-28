from openai import OpenAI
from key import OPENAI_API_KEY

class Model():
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def ask(self, code):
        question = self.generate_question(code)
        stream = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
        )

        answer = ""

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                # print(chunk.choices[0].delta.content, end="")
                answer += chunk.choices[0].delta.content

        answer = answer.split("\n")
        return answer

    def generate_question(self, code):
        base = "insert me a comment above every line of code explaining what it does:\n"
        return base + code