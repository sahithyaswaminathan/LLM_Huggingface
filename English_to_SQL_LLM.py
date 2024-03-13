#Text completion LLM using gpt-2 hosted by huggingface
from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate

#everything defined in env file is exposed in this environment
load_dotenv()
#English to SQL llm
hub_llm = HuggingFaceHub(repo_id="mrm8488/t5-base-finetuned-wikiSQL")
#Pass the prompt to LLM for which it provides the output
#hub_chain = LLMChain("what is the percentage split of trees in the rainforest")
#Instead of hardcoding we can create a prompt template
prompt = PromptTemplate(
    input_variables= ["question"],
    template= "Translate English to SQL: {question}"
)
hub_chain = LLMChain(prompt=prompt, llm=hub_llm, verbose=True)
print(hub_chain.run("what is average age of people in New York?")) #fed to question