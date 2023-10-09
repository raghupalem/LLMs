
#from langchain.document_loaders import DirectoryLoader

import os
#os.environ["OPENAI_API_KEY"] ="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"


from langchain.llms import OpenAI

#Using OpenAI -chatGPT 3.5
llm = OpenAI(temperature=0.9)  

prompt = "what would be a good company name be for a company that makes colorful socks?"

#print(llm(prompt))
result = llm.generate([prompt]*5)

for c_name in result.generations:
  print(c_name[0].text)