from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from languages import svg_languages

origins = [
    "http://www.ramshankar.codes",
    "https://www.ramshankar.codes",
    "http://iconsapi.ramshankar.codes",
    "https://iconsapi.ramshankar.codes",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

description = """DevHaven Icon API lets you download for icons in the SVG format."""

tags_metadata = [
    {
        "name": "svg",
        "description": "Logo in svg format. You get the svg for the icon you want or all of them.",
    },
    {
        "name": "img",
        "description": "Logo in PNG format.**To be developed**",
    },
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="DevHaven Icons API",
    description=description,
    version="0.0.1",
    contact={
        "name": "DevHaven",
        "url": "https://www.ramshankar.codes/",
        "email": "ramshankar.codes@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 

@app.get('/')
def root():
    return {"instructions": [
        {'svg':'you can get svgs from /svg/{language}'},
        {'image_in_developement':'you can get images from /img/{language}'},
    ]}
    
@app.get('/svg', tags=["svg"])
def svg_all():
    svg = [f"<svg viewBox='0 0 128 128' width='120px' height='120px stroke='none'>{svgs}</svg>" for svgs in svg_languages.values()]
    return ({'icons':svg_languages})

@app.get("/svg/{lang}", tags=["svg"])
def svg_single(lang:str, width:Optional[int] = 128, height:Optional[int] = 128, stroke:Optional[str]='none'):
    
    language = str.lower(lang)
    
    if language in svg_languages:
        return f'''<svg width='{width}px' height='{height}px stroke='none'> {svg_languages[language]}</svg>'''
    else:
        return f'''{language} is not available. You can request a new SVG here: https://github.com/BlankRiser/DevHavenIcons'''

    
# @app.get('/img', tags=["img"])
# def img_all():
#     img = [f"<img src='<svg viewBox='0 0 128 128' width='120px' height='120px stroke='none'>{svgs}</svg>'>" for svgs in svg_languages.values()]
#     return ({'icons':img})

# @app.get("/img/{lang}",tags=["img"], response_class=HTMLResponse)
# def img_single(lang:str, width:Optional[int] = 128, height:Optional[int] = 128, stroke:Optional[str]='none'):
    
#     language = str.lower(lang)
#     print('functions prints')
    
#     if language in svg_languages:
#         # svgOutput = '''< width='{width}px' height='{height}px stroke='none' >{svg_languages[language]}</svg>'''
#         return f'''<svg width='{width}px' height='{height}px stroke='none'> {svg_languages[language]}</svg>'''
#     else:
#         return f'''<p>{language} is not available. You can request a new SVG here: <Github link> </p>'''
    