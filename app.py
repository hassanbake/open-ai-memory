from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
# from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

def main():
    load_dotenv()
    
    # Test out api key
    if os.environ.get("OPENAI_API_KEY") is None or os.environ.get("OPENAI_API_KEY")=="":
        print("Please add you OpenAI key to .env")
        exit(1)
    else:
        print("OpenAI API key set.")

    llm = ChatOpenAI()
    # memory = ConversationBufferMemory()
    memory = ConversationEntityMemory(llm=llm)
    conversation = ConversationChain(
        llm=llm, 
        memory=memory,
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        verbose=True
    )


    chat = ChatOpenAI(temperature=0.3)

    print("Hello, I am ChatGPT CLI!")

    while True:
        user_input = input("> ")

        ai_response = conversation.predict(input=user_input)
        print("\nAssistant:\n", ai_response)

if __name__ == "__main__":
    main()