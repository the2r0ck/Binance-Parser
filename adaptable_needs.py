import subprocess

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello_world():
    return {
        "message": "Hello World"
    }
    

@app.get("/run_cron")
def hello_world():
    result = subprocess.run("cron", shell=True, capture_output=True, text=True)
    return {
        "message": "cron runned",
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
