import uuid
import os
from datetime import datetime
from fastapi import FastAPI, UploadFile, File, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import models, database 
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse


app = FastAPI()

#Mounted static files where i have styling of web page.
app.mount("/static", StaticFiles(directory="static"), name="static")




# Setup templates
templates = Jinja2Templates(directory="templates")

# Create database tables (once)
models.Base.metadata.create_all(bind=database.engine)

# Directory to save uploads
UPLOAD_DIR = "static/uploads"


# Database dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET: show HTML upload form
@app.get("/form", response_class=HTMLResponse)
def show_upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


# POST: upload file and save record
@app.post("/upload/")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Extract file extension (.jpg, .pdf, etc.)
    file_ext = os.path.splitext(file.filename)[1]

    # Generate system filename using UUID
    system_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, system_filename)

    # Save uploaded file locally
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Get file size in bytes
    filesize = os.path.getsize(file_path)

    # Current time (received/uploaded)
    uploaded_at = datetime.now()

    # Create DB record
    document = models.Image(
        original_filename=file.filename,
        system_filename=system_filename,
        file_size_bytes=filesize,
        uploaded_at=uploaded_at
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "File uploaded successfully!",
        "original_filename": file.filename,
        "system_filename": system_filename,
        "file_size_bytes": filesize,
        "uploaded_at": uploaded_at
    }

#GET: fetches all records from database images table and retuirn in a json format.
@app.get("/files/")
def get_all_files(db: Session = Depends(get_db)):
    # Query all records
    files = db.query(models.Image).all()

    # Convert SQLAlchemy objects to list of dictionaries
    result = []
    for f in files:
        result.append({
            "id": f.id,
            "original_filename": f.original_filename,
            "system_filename": f.system_filename,
            "file_size_bytes": f.file_size_bytes,
            "uploaded_at": f.uploaded_at.isoformat() 
        })

    return JSONResponse(content=result)

# GET: It shows a table where all information related to the images.
@app.get("/files/html", response_class=HTMLResponse)
def get_files_html(request: Request, db: Session = Depends(get_db)):
    files = db.query(models.Image).all()
    return templates.TemplateResponse("record.html", {"request": request, "files": files})
