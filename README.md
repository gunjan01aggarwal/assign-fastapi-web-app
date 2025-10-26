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


# there are four endpoints:
# 1. Post request:You can upload any image from  this endpoint.
#   http://127.0.0.1:8000/form

# 2. Get request:You can see all images information in the form of a table.
#  http://127.0.0.1:8000/files/html 

# 3. Get request: You can see all images information in a json format.
# http://127.0.0.1:8000/files/

# 4. It shows current upload image information.
# http://127.0.0.1:8000/upload/


