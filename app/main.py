from fastapi import FastAPI, Depends
from pydantic import BaseModel

from app.utils import read_from_file
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Posts(BaseModel):
    page: int | None = 1


@app.get('/posts')
async def get_posts(params: Posts = Depends()):
    page_filters = {
        1: 'yandex.txt',
        2: 'yandex2.txt',
        3: 'yandex3.txt'
    }
    result = read_from_file(file_name=page_filters[params.page])
    return {'posts': result}
