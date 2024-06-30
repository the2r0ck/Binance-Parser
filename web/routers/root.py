from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="")


@router.get("/status")
def system_status(request: Request):
    return templates.TemplateResponse("status.html", {"request": request, "title": "Status"})
