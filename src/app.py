from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class PostSchema(BaseModel):
    title: str
    description: str

#Dummy seed data
posts = {
    1: {
        "title": "Rise of Punjabi Music in India",
        "description": "Exploring how regional beats transcended borders to become a global pop culture phenomenon, dominating charts from Bollywood to Billboard.",
        "author": "Aryan Kohli"
    },
    2: {
        "title": "The UPI Revolution",
        "description": "How a simple QR code transformed the Indian economy, enabling seamless digital transactions for everyone from high-end retailers to street vendors."
    },
    3: {
        "title": "Boom of D2C Brands",
        "description": "An analysis of how homegrown startups are bypassing traditional middlemen to build direct, authentic relationships with the modern consumer."
    },
    4: {
        "title": "The Shift to Sustainable Fashion",
        "description": "Why Gen Z and Millennials are ditching fast fashion in favor of thrift finds, handlooms, and ethical manufacturing practices."
    },
    5: {
        "title": "Explosion of Regional OTT Content",
        "description": "How streaming platforms broke the language barrier, bringing Malayalam thrillers and Bengali dramas to a Pan-Indian audience."
    },
    6: {
        "title": "Electric Vehicle Adoption",
        "description": "Assessing the rapid transition from fuel to battery power in the two-wheeler market and the infrastructure challenges ahead."
    },
    7: {
        "title": "The Specialty Coffee Culture",
        "description": "Moving beyond instant coffee: How artisanal roasters and distinct café aesthetics are redefining social spaces in metro cities."
    },
    8: {
        "title": "Growth of Women's Cricket",
        "description": "Tracing the commercial and cultural rise of women's cricket, fueled by new leagues and iconic performances on the world stage."
    },
    9: {
        "title": "The Gig Economy & Remote Work",
        "description": "How the post-pandemic world normalized freelancing and work-from-home setups, changing the traditional 9-to-5 mindset."
    },
    10: {
        "title": "Destigmatizing Mental Health",
        "description": "A look at the growing awareness around mental well-being and how therapy is becoming an open conversation in urban households."
    }
}

@app.get("/")
def read_root():
    return {"msg": "Server is running"}

@app.get("/posts", response_model=Dict[int, PostSchema])
def get_all_posts():
    return posts

@app.get("/post/{post_id}", response_model=PostSchema)
def get_post(post_id: int):
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Invalid Post Id")
    return posts[post_id]

@app.post("/add", status_code=status.HTTP_201_CREATED)
def add_post(post: PostSchema):
    post_id = max(posts.keys()) + 1 if posts else 1
    posts[post_id] = post.dict()
    return {"msg": "Post added successfully"}
