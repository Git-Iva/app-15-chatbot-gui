import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, user_input, model="gpt-3.5-turbo"):
        messages = [{"role": "user", "content": user_input}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=1000,
            temperature=0.7
            )
        return response.choices[0].message["content"]


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me a joke about planets")
    print(response)

