from fastapi import APIRouter, Depends, Form, UploadFile, Request
from fastapi.responses import JSONResponse, RedirectResponse
from app.models.model_qrcode import ConfigSchema, SingleUrlSchema, MultipleUrlSchema, EmailAddressSchema, MobileMessageSchema, PhoneSchema, ContactSchema, EventSchema, AndroidIosUrlSchema, RedirectSchema
from app.services.service_qrcode import QRcodeService

router = APIRouter(
    prefix="/qrcode",
    tags=["QRCODE"],
    responses={404: {"message": "Not found"}}
)

@router.post("/config_ngrok")
async def config(data: ConfigSchema = Depends(ConfigSchema)):
    return QRcodeService().config(data.ngrok_url)

@router.post("/single_url")
async def single_url(data: SingleUrlSchema = Depends(SingleUrlSchema)):
    return QRcodeService().single_url(data.url)

@router.post("/mulitple_url")
async def mulitple_url(data: MultipleUrlSchema = Depends(MultipleUrlSchema)):
    url = data.url[0].split(',')
    return QRcodeService().mulitple_url(url)

@router.post("/email_address")
async def email_address(data: EmailAddressSchema = Depends(EmailAddressSchema)):
    return QRcodeService().email_address(data.email, data.subject, data.body)

@router.post("/mobile_message")
async def mobile_message(data: MobileMessageSchema = Depends(MobileMessageSchema)):
    return QRcodeService().mobile_message(data.phone, data.message)

@router.post("/phone")
async def phone(data: PhoneSchema = Depends(PhoneSchema)):
    return QRcodeService().phone(data.phone)

@router.post("/contact")
async def contact(data: ContactSchema = Depends(ContactSchema)):
    return QRcodeService().contact(data.name, data.email, data.phone, data.address)

@router.post("/event")
async def event(data: EventSchema = Depends(EventSchema)):
    return QRcodeService().event(data.subject, data.location, data.description, data.start, data.end)

@router.post("/android_ios")
async def android_ios(request: Request, data: AndroidIosUrlSchema = Depends(AndroidIosUrlSchema)):
    url = request.cookies.get("url")
    return QRcodeService().android_ios(url, data.android, data.ios)

@router.get("/android_ios_redirect")
async def android_ios_redirect(request: Request, data: AndroidIosUrlSchema = Depends(AndroidIosUrlSchema)):
    user_agent = request.headers.get("User-Agent")
    return QRcodeService().android_ios_redirect(user_agent, data.android, data.ios)

@router.get("/redirect")
async def redirect_endpoint(data: RedirectSchema = Depends(RedirectSchema)):
    return RedirectResponse(data.url)

@router.get("/checkos")
async def checkos(request: Request):
    user_agent = request.headers.get("User-Agent")
    return user_agent

@router.get("/checkos_redirect")
async def checkos_redirect(request: Request):
    user_agent = request.headers.get("User-Agent")
    if "Android" in user_agent:
        return RedirectResponse("https://play.google.com/store/apps/")
    elif "iPhone" in user_agent or "iPad" in user_agent:
        return RedirectResponse("https://apps.apple.com/")
    elif "Windows" in user_agent:
        return RedirectResponse("https://www.microsoft.com/en-us/store/apps/windows/")
    else:
        return {"message": "Sorry, your device is not supported"}

@router.post("/scan")
async def qrcode_scan(file: UploadFile):
    return QRcodeService().qrcode_scan(file.file)