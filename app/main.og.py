from random import randrange
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
#package for defining a schema for 
from pydantic import BaseModel
# import json

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title" : "favorite foods"," content" : "I hate pizza", "id":2 }]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
        return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return ({"data":my_posts})

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post: Post):
    # print(post)
    # print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
# def get_post(id: int, response: Response):
def get_post(id: int):
    print(id)
    post = find_post(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} cannot be found." )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} cannot be found."}
    return {"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    index = find_index_post(id)
    my_posts.pop(index)
    return {"message":'Post was successfully deleted'}

