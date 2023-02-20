from decouple import config
from fastapi.responses import JSONResponse, StreamingResponse, RedirectResponse
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO
import qrcode

class RoomService:
    def __init__(self):
        self.config = ''

    def room_qrcode(self, room_id):
        image = qrcode.make(room_id)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def room_access(self, room_id, auth_code):
        return True
        """ # Retrieve the expected authorization code for the room from the database or file
        expected_auth_code = retrieve_auth_code_for_room(room_id)
        
        # Compare the provided code with the expected code
        if auth_code == expected_auth_code:
            return True
        else:
            return False """