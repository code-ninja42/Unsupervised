from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open("salary_api.pkl", "rb"))

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/predict")
def predict(data: dict):
    exp = float(data["YearsExperience"])
    result = model.predict([[exp]])

    return {
        "YearsExperience": exp,
        "PredictedSalary": float(result[0])
    }
    #py -3.13 -m uvicorn main:app --reload
   # http://127.0.0.1:8000/docs
  # to check post on web
  