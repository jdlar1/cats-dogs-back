from pydantic import BaseModel

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from ai import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # replace with your frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Response(BaseModel):
    prediction: str

@app.post("/predict")
async def predict_endpoint(upload: UploadFile = File(...)):
    print(upload.filename)
    file = await upload.read()
    
    prediction = predict(file)
    print(f"Prediction: {prediction}")
    
    animal = "error"
    
    if prediction < 0.0001:
        animal = "cat"
    elif prediction > 0.9999:
        animal = "dog"
    
    return Response(prediction=animal)
    