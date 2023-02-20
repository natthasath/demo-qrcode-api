from fastapi import APIRouter, Depends, Form, UploadFile, Request
from fastapi.responses import JSONResponse, RedirectResponse, StreamingResponse
from app.models.model_room import RoomSchema
from app.services.service_room import RoomService
import cv2

router = APIRouter(
    prefix="/room",
    tags=["ROOM"],
    responses={404: {"message": "Not found"}}
)

@router.get("/headers")
async def read_headers(request: Request):
    user_agent = request.headers.get("User-Agent")
    return user_agent

@router.post("/room_qrcode")
async def room_qrcode(data: RoomSchema = Depends(RoomSchema)):
    return RoomService().room_qrcode(data.room_id)

@router.post("/room_access")
async def room_access(data: RoomSchema = Depends(RoomSchema)):
    return RoomService().room_access(data.room_id)

@router.get("/webcam")
async def read_webcam():
    capture = cv2.VideoCapture(0)
    if not capture.isOpened():
        raise ValueError("Unable to open webcam")

    def generate():
        while True:
            ret, frame = capture.read()
            if not ret:
                break
            frame = cv2.imencode(".jpg", frame)[1].tobytes()
            yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

    return StreamingResponse(generate(), media_type="multipart/x-mixed-replace;boundary=frame")