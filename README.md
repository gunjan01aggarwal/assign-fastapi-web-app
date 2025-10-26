"# assign-fastapi-web-app" 

# Make a fastapi folder.
 mkdir fastapi
# Create a virtual environment inside fastapi folder.
 python3 -m venv .env

# Install requirements
pip install fastapi uvicorn jinja2 sqlalchemy

# project structure
fastapi_webapp/
│
├── main.py
├── models.py
├── database.py
├── templates/
│   ├── record.html
│   ├── upload.html
├── static/
│   ├──css/style.css
    ├──uploads
└── .env/

# clone this repository:
https://github.com/gunjan01aggarwal/assign-fastapi-web-app.git



