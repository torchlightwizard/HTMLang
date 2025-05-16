from openai import OpenAI
from dotenv import load_dotenv as env
import os


class LLMOPENAI():
    def __init__(
            self, 
            model="gpt-4.1-nano-2025-04-14", 
            api_str="OPENAI_API_KEY", 
            prty="{}",
        ):
        
        super().__init__()
        env(".env")
        openai_api_key = os.getenv(api_str)

        self.client = OpenAI(api_key=openai_api_key)
        self.model = model
        self.prty = prty
        self.history = []


    def set_prty(self, prty):
        self.prty = prty
        return self


    def run(self, params):
        prompt = self.prty.format(*params)   
        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )
        ouput = response.output_text

        self.history.append({
            "prty": self.prty,
            "params": params,
            "response": ouput
        })

        return self


    def show_responses(self):
        for conv in self.history:
            print(conv["response"])
            print("--")
        return self
    

    def show_history(self):
        for conv in self.history:
            print(conv["prty"])
            print(conv["params"])
            print(conv["response"])
            print("--")
        return self