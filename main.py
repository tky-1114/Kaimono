from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.get("/get_name")
def get_name(name: str = Query(...)):
    return {"name": name}

@app.get("/get_profile")
def get_profile(age: int = Query(None), name: str = Query(...)):
    return {"age: ": age, "name: ": name}

@app.get("/get_profile/{name2}/myname")
def get_p(
    name2: str,
    name: str = Query(...),
    age: int | None = Query(None)
):
    return {"name: ": name, "name2: ": name2, "age: ": age}