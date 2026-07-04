from agents import function_tool

from rag.retriever import Retriever

retriever = Retriever()


@function_tool
def search_knowledge_base(query: str) -> str:
    """
    Search the knowledge base for information related to the user's question.
    """
    return retriever.retrieve(query)