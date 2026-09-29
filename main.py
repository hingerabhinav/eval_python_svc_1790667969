from fastapi import FastAPI

app = FastAPI(title="eval_python_svc_1790667969")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "eval_python_svc_1790667969", "owner": "eval_team_1790667969"}
