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




Q1.Why you choose your method for creating a unique system filename?

	I choose a method for creating a unique system filename because of avoiding same filename. I don't know other user can be choose same name of file like flowers.png .This anme can be choose by many others users due to its a picture of a flowers. So i choose uuid.uuid4()  which generates a randomly unique 128-bit identifier.Its simple,secure and works for all platforms.

Q3.Any challenges you faced and how you resolved them?
 I faced many challenges while solving this project like:
1.Relative imports causing errors:Using from . import models, database caused ImportError: attempted relative import with no known parent package when running main.py. after that i try import models,database,it works.
2.Datetime not JSON serializable:Object of type datetime is not JSON serializable.I convert datetime into string using isoformat()before returning json.
3.The style.css in the static folder was not applied in HTML:I need to mounted the static folder in fastapi.


