from decouple import config
from fastapi.responses import JSONResponse, StreamingResponse, RedirectResponse
from pyzbar.pyzbar import decode
from PIL import Image
from io import BytesIO
import qrcode

class QRcodeService:
    def __init__(self):
        self.url_ios = config('URL_IOS')
        self.url_android = config('URL_ANDROID')
        self.url_windows = config('URL_WINDOWS')

    def config(self, url):
        content = {"message": True}
        response = JSONResponse(content=content)
        response.set_cookie(key='url', value=url)
        return response

    def single_url(self, url):
        image = qrcode.make(url)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def mulitple_url(self, url):
        image = qrcode.make(url)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def email_address(self, email, subject, body):
        data = f"MATMSG:TO:{email};SUB:{subject};BODY:{body};;"
        image = qrcode.make(data)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def mobile_message(self, phone, message):
        data = f"SMSTO:{phone}:{message}"
        image = qrcode.make(data)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def phone(self, phone):
        data = f"tel:{phone}"
        image = qrcode.make(data)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def contact(self, name, email, phone, address):
        data = f"MECARD:N:{name};EMAIL:{email};TEL:{phone};ADR:{address};;"
        image = qrcode.make(data)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def event(self, subject, location, description, start, end):
        data = f"BEGIN:VEVENT\nSUMMARY:{subject}\nLOCATION:{location}\nDESCRIPTION:{description}\nDTSTART:{start}\nDTEND:{end}\nEND:VEVENT"
        image = qrcode.make(data)
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def android_ios(self, url, android, ios):
        image = qrcode.make(url + f'/qrcode/android_ios_redirect?android={android}&ios={ios}')
        buffer = BytesIO()
        image.save(buffer, "PNG")
        buffer.seek(0)
        return StreamingResponse(buffer, media_type="image/png")

    def android_ios_redirect(self, user_agent, android, ios):
        if "Android" in user_agent:
            return RedirectResponse(android)
        elif "iPhone" in user_agent or "iPad" in user_agent:
            return RedirectResponse(ios)
        else:
            return JSONResponse(status_code=200, content={"message": "Sorry, your device is not supported"})

    def qrcode_scan(self, file):
        decocdeQR = decode(Image.open(file))
        uri = decocdeQR[0].data.decode('ascii')
        return uri