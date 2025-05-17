from model.gen.llm._openai import gloa
import time

llm1 = gloa(name="model 1")
llm2 = gloa(name="model 2")

a = llm1.set("Ask something you want from another llm model.{}").run([""]).get()
time.sleep(1)
b = llm2.set("Ask something you want from another llm model who has said: {}").run([a]).get()
time.sleep(1)

for i in range(10):
    a = llm1.set("Model 2 has asked: {}").run([b]).get()
    print("Model 1: ", a)
    print("---")
    time.sleep(1)
    b = llm2.set("Model 1 has asked: {}").run([a]).get()
    print("Model 2: ", b)
    print("---")
    time.sleep(1)