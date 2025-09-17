from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")
@app.get("/")
async def root():
return {"message": "🏠 Montpellier Immo AI", "status": "running"}
@app.get("/interface")
async def serve_frontend():
return FileResponse("frontend/index.html")
class ContentRequest(BaseModel):
platform: str
@app.post("/generate-content")
async def generate_content(request: ContentRequest):
if request.platform == "linkedin":
return {"post": "Découvrez les opportunités immobilières à Montpellier ! #Montpellier #Immobilier #PortMarianne"}
elif request.platform == "instagram":
return {"post": "🏡 Montpellier, la ville où investir ! #ImmobilierMontpellier #Antigone #Investissement"}
else:
raise HTTPException(status_code=400, detail="Platform must be 'linkedin' or 'instagram'")
