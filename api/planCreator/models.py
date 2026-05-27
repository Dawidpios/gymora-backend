from pydantic import BaseModel, Field


class Exercise(BaseModel):
    name: str = Field(description="Name of the exercise")
    sets: int = Field(description="Number of sets")
    reps: str = Field(description="Rep range, e.g. '8-12' or '30 seconds'")
    tempo: str = Field(default="", description="Tempo notation, e.g. '2-0-2'")
    rest: str = Field(description="Rest time between sets, e.g. '60-90 sec'")
    technical_cues: str = Field(description="Key technique tips for this exercise")


class WorkoutPlan(BaseModel):
    assessment: str = Field(description="Brief assessment of the user's profile and goals")
    weekly_training_split: str = Field(description="Name and description of the chosen training split")
    exercises: list[Exercise] = Field(description="List of exercises in the plan")
    progression_strategy: str = Field(description="How to progress week over week")
    rest_times: str = Field(description="General rest time guidelines")
    weekly_progression_recommendations: str = Field(description="Specific weekly progression targets")
    warm_up_routine: list[str] = Field(description="List of warm-up steps")
    cooldown_stretching: list[str] = Field(description="List of cooldown and stretching steps")
    why_these_exercises: str = Field(description="Explanation of why these exercises were selected")
    alternative_exercises: str = Field(description="Suggested alternatives for exercises in the plan")
    motivation: str = Field(description="Motivational closing message from the trainer")