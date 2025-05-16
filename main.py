from llms.llmopenai import LLMOPENAI

llm = LLMOPENAI(prty="What is the largest export of {}?")
llm.run(["pakistan"]).show_responses()

llm.set_prty("What is capital of {}?").run(["russia"]).show_responses()
