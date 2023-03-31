from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import json

def generate_html_response():
    htmlContent = """   
    <hmtl lang="en">
        <head>
            <title>Test</title>
        </head>

        <body>
            <style>

                .body {
                    background-color: black;
                }

            </style>

            <script>

            </script>

            <form>
                <label for="toSqaure">Square a Number</label>
                <input type="int" id="toSqaure" name="toSqaure">
            </form>

        </body>

    </hmtl>
    """
    return HTMLResponse(content=htmlContent, status_code=200)

app = FastAPI()

@app.get("/items/", response_class=HTMLResponse)
async def read_items():

    return generate_html_response()