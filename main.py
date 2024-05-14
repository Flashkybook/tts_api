from typing import Union
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from ttsGenerator import Generator
from fastapi.responses import HTMLResponse
app = FastAPI()

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body style="background-color: black; color: white; height: 100vh,width: 100vw; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <h1>TTS generador de audios</h1>
            
            <form style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px;" id="form" action="/tts/" method="get">
           
                <input style="width: 300px; height: 30px; border-radius: 5px;  border: 1px solid white; padding: 5px; text-align: center" type="text" name="expression" value="type your expression here">
                <button type="submit">Submit</button>
            </form>
            <script>
            const form = document.getElementById("form");
            form.addEventListener("submit", (event) => {
                event.preventDefault();
                const formData = new FormData(form);
                const expression = formData.get("expression");
                fetch("/tts/?expression=" + expression).then((response) => {
                    response.blob().then((blob) => {
                        const url = URL.createObjectURL(blob);
                        new Audio(url).play();
                    })
                })
            })
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/")
def read_root():
    return generate_html_response()

# http://localhost:8000/tts/?expression=asdsa
@app.get("/tts/")
def tts_api(expression:str|None = None):
    
    if expression == None:
        return {"error": "no expression word"}
    audio = Generator(expression)
    return FileResponse(audio)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
