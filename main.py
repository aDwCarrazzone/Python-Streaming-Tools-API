import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from trovo_get_profile_image import get_trovo_profile_image_url as trovo_get_profile_image
from trovo_get_profile_followers import get_trovo_profile_followers_quantity as trovo_get_profile_followers
from twitch_get_profile_image import get_twitch_profile_image_url as tgpi

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Allow Access-Control-Allow-Origin from other domains
@app.middleware("http")
async def add_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

# when user a username in the url, get the profile image url
@app.get("/api/trovo/get/image/{username}")
async def get_trovo_profile_image_url(username: str):
    profile_image_url = await trovo_get_profile_image(username)
    return(profile_image_url)

@app.get("/api/twitch/get/image/{username}")
async def get_twitch_profile_image_url(username: str):
    profile_image_url = await tgpi(username)
    return(profile_image_url)

# @app.get("/api/trovo/get/followers/{username}")
# async def get_trovo_followers(username: str):
#     profile_followers = await trovo_get_profile_followers(username)
#     return(profile_followers)

if __name__ == '__main__':
    uvicorn.run(app, port=80, host='127.0.0.1')