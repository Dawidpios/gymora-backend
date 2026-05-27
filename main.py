from fastapi import FastAPI
import api.mail.mail as mail_router
from fastapi.middleware.cors import CORSMiddleware
import api.planCreator.planCreator as planCreator

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(mail_router.router)
app.include_router(planCreator.router)

  
