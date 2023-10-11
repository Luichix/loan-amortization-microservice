from fastapi import FastAPI
from app.routers import amortizations, financial_statements
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(amortizations.router)
app.include_router(financial_statements.router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
