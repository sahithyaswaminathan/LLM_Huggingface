#Text completion LLM using gpt-2 hosted by huggingface
from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

#everything defined in env file is exposed in this environment
load_dotenv()
#temperature is set high so LLM becomes creative
hub_llm = HuggingFaceHub(
    repo_id="gpt2",
    model_kwargs={'temperature': 0.6, 'max_length': 100})
#Pass the prompt to LLM for which it provides the output
prompt = PromptTemplate(
    input_variables= ["occasion"],
    template= "I had a really great time at the {occassion}! Lets celebrate and be happy"
)
hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
print(hub_chain.run("Diwali")) #fed to question
print(hub_chain.run("New year"))
print(hub_chain.run("Christmas"))