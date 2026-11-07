from fastapi import FastAPI

klu = FastAPI(title="AI-Tutor", 
              description="An AI-Tutor Pbl project.",
                version="1.0.0")


@klu.get("/")
def home():
    return {"message": "Welcome to the AI-Tutor project!"}

@klu.get("/demo")
def demo():
    return {"message": "KL university."}

@klu.get("/ask question")
def ask_question():
    return {"message": "What is  LLM?","ANSWER":"LLM stands for Large Language Model. It is a type of artificial intelligence model that is trained on vast amounts of text data to understand and generate human-like language. LLMs can perform various natural language processing tasks, such as text generation, translation, summarization, and question-answering."}
