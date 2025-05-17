from openai import OpenAI
from dotenv import load_dotenv as env
import os


class gloa():
    """
        gloa stands for gen llm open ai
    """

    def __init__(
            self, 
            api_str="OPENAI_API_KEY", 
            model="gpt-4.1-nano-2025-04-14", 
            task=None,
            name=None,
            temperature=0.9
        ):
        
        super().__init__()
        env(".env")
        openai_api_key = os.getenv(api_str)

        self.client = OpenAI(api_key=openai_api_key)
        self.model = model
        self.task = task
        self.data = None
        self.name = name
        self.temperature = temperature


    def set(self, task):
        # print(f"LOG: {self.name} openai set.")
        self.task = task
        return self


    def run(self, params):
        # print(f"LOG: {self.name} openai run.")
        prompt = self.task.format(*params)   
        response = self.client.responses.create(
            model=self.model,
            temperature=self.temperature,
            input=prompt
        )
        output = response.output_text
        self.data = output
        return self


    def get(self):
        # print(f"LOG: {self.name} openai get.")
        output = self.data
        return output