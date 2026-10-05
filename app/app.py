from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import Post, create_db_and_tables, get_async_session
from app.schemas import PostCreate, PostResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


text_posts = {
    1: {"title": "New post", "content": "Cool test post"},
    2: {"title": "Hello World", "content": "My first test post!"},
    3: {"title": "FastAPI Tips", "content": "Use Pydantic models for validation."},
    4: {"title": "Python Tricks", "content": "List comprehensions are awesome."},
    5: {"title": "Morning Update", "content": "Coffee first, code later."},
    6: {"title": "Weekend Plans", "content": "Hiking and then building APIs."},
    7: {"title": "Test Post 7", "content": "Lorem ipsum dolor sit amet."},
    8: {"title": "Random Thoughts", "content": "Why is the sky blue? Anyway, testing."},
    9: {"title": "Dev Diary", "content": "Day 12: still debugging."},
    10: {"title": "Final Test", "content": "This is the last cool test post."},
}


@app.get("/posts")
def get_all_posts(limit: int | None = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    return text_posts[id]


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {
        "title": post.title,
        "content": post.content,
    }
    text_posts[max(text_posts.keys()) + 1] = new_post
    return PostResponse(title=post.title, content=post.content)
