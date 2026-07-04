from agents import Agent

from llm import model
from tools.knowledge_tool import search_knowledge_base


study_agent = Agent(
    name="Study Assistant",
    instructions="""
    You are a helpful study assistant.

    Answer questions only using the provided knowledge base.

    Always use the search_knowledge tool before answering questions
    about the uploaded study materials.

    If the answer is not found in the knowledge base,
    politely say that you don't know.

    Mention the source and page number whenever possible.
    """,
    model=model,
    tools=[search_knowledge_base],
)