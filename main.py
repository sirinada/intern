from fastapi import FastAPI

app = FastAPI()

@app.get('/bmi')
def main(w:int, h:int):
    
    h = (h/100)**2
    bmi = w/h
    return {'bmi':bmi}

