from fastapi import FastAPI
from pydantic import BaseModel

# 1) Create the app
app = FastAPI()

# 2) Define what the input looks like
class InputData(BaseModel):
    text: str  # change this to whatever your real input is

# 3) Your existing function (toy example)
def Copy of volleyball_trajectory_tracker(text: str) -> str:
    # 🚧 Replace this with your real logic / model call
    result = text[::-1]
    return result

# 4) Create an endpoint
@app.post("/predict")
def predict(data: InputData):
    output = Copy of volleyball_trajectory_tracker(data.text)
    return {"result": output}

