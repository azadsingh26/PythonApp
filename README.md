_**PythonApp**_
---


PythonRainfallApp - Get Rainfall information from Singapore Gov Data API https://api.data.gov.sg/v1/environment/rainfall

The python flask app represents the backend which returns the response in csv format about the locations mentioned in the configuration part..
When running the app locally, the app is accessible under the following URL: http://localhost:8080 or  http://127.0.0.1:8080

---

Getting Started
---
_**Installing Dependencies**_

**Python 3.8.2**

Follow instructions to install the latest version of python for your platform in the python docs

**PIP Dependencies**

>`pip install -r requirements.txt `

This will install all of the required packages we selected within the requirements.txt file.
---
**Key Dependencies**


**Flask**  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

**Requests** module allows you to send HTTP requests using Python.

**Pytest** is a testing framework that allows users to write test codes using Python programming language.

---

Running the server

From within the src directory you can run

>`python3 -m flask run `

you can also give custom parameters to override different ports

>`python3 -m flask run --port=8443
`
---


**BUILDING DOCKER IMAGE**

>`docker build -t <imageName>:<version> . `
  
** RUNNING PYTEST**
  
  >`python3 -m pytest`
  
