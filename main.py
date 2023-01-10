from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_rating
#from app.model.model import __version__ as model_version


from fastapi.middleware.cors import CORSMiddleware









app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextIn(BaseModel):
    text: str



@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict")
def predict(payload: TextIn):
    prediction_rating = predict_rating(payload.text)
    return {"prediction": prediction_rating}