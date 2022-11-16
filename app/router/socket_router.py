from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.logger import logger

from fastapi import APIRouter
from ..db.database import SessionLocal, engine

from ..utils.auth_utils import get_current_user,AuthProvider, get_db


router = APIRouter(
    prefix="/socket"
)


@router.websocket("/connect")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()
    await websocket.send_text(f"Welcome client:{websocket.client}")
    while True:
        data = await websocket.receive_text()
        print(f"message receices: {data} from {websocket.client}")
        await websocket.send_text(f"Message text was: {data}")
    
