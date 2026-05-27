from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from .prompt import prompt as LLM_PROMPT
from .models import WorkoutPlan


load_dotenv(override=True)

def connect(query: str) -> WorkoutPlan:
    openAI = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    prompt = ChatPromptTemplate.from_messages([
        ("system", LLM_PROMPT),
        ("human", "{query}")
    ])

    structured_llm = openAI.with_structured_output(WorkoutPlan)
    chain = prompt | structured_llm
    result: WorkoutPlan = chain.invoke({"query": query})

    return result


