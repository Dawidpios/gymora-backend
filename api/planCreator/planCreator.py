from fastapi import APIRouter
from .connect import connect
from pydantic import BaseModel


class BasicInfo(BaseModel):
    goal: str
    experience: str
    days: int


class PlanDetails(BaseModel):
    weeklyStructure: str
    trainingApproach: str


class PlanBody(BaseModel):
    basicInfo: BasicInfo
    exercises: list[str]
    planDetails: PlanDetails
  

router = APIRouter()

@router.post("/plan-creator")
async def create_plan(body: PlanBody): 
    query = f"""
    Create a personalized workout plan based on the following information:
    Goal: {body.basicInfo.goal}
    Experience: {body.basicInfo.experience}
    Training Days per Week: {body.basicInfo.days}
    Preferred Exercises: {', '.join(body.exercises)}
    Weekly Structure: {body.planDetails.weeklyStructure}
    Training Approach: {body.planDetails.trainingApproach}
    """
    res = connect(query)
    return res.model_dump()