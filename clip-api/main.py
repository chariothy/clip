from typing import Optional
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import StreamingResponse, HTMLResponse
import os, time, random
from os import path

import redis
REDIS = redis.Redis(connection_pool=redis.ConnectionPool(host='redis', port=6379, db=0))

from utils import at

app = FastAPI()
ENV = os.environ.get('ENV', 'dev')
EXIT = False


def gen_rand():
    id = random.randint(100,999)
    while REDIS.exists(id):
        id = random.randint(100,999)
    return id


@app.post('/')
async def copy(req: Request, f: Optional[UploadFile] = File(None), t: Optional[str] = Form(None)):
    id = gen_rand()
    time_left=at['timeout']
    if t:
        REDIS.set(id, t, time_left)
    elif f:
        _, fullname = path.split(f.filename)
        name, ext = path.splitext(fullname)
        new_name = f'{name}_{id}{ext}' if ext else f'{name}_{id}'
        out_file_path = path.join(at['tmp_dir'], new_name)
        
        with open(out_file_path, 'wb') as out_file:
            while content := f.file.read(1024):  # async read chunk
                out_file.write(content)  # async write chunk
        REDIS.set(id, out_file_path, time_left)
    else:
        id = None
    return id


@app.get('/')
async def usage(req: Request):
    html_content = '''<pre>
# clip
Mini clip board for curl & webpage.

## Put something on it (simply return digital id)

1. Put message
   
    `curl localhost:8000 -F t="Some text"`

2. Put file

    `curl localhost:8000 -F f=@c:/some-file`


## Get something from it ({id} is what we just returned from Put)
1. Get message
   
    `curl localhost:8000/{id}`

2. Get file

    `curl -o file_name.ext localhost:8000/{id}`
</pre>
'''
    return HTMLResponse(content=html_content, status_code=200)


@app.get('/{id}')
async def paste(req: Request, id: int):
    text = REDIS.get(id)
    #print(text)
    if path.exists(text):
        def iterfile():
            with open(text, mode="rb") as file_like:
                yield from file_like
        return StreamingResponse(iterfile(), media_type="application/octet-stream")
    return text


if __name__ == "__main__":
    import uvicorn, os
    print(f'Listening ++++++ ENV={ENV} ++++++')
    uvicorn.run("main:app", host="0.0.0.0", port=at['port'], reload=(ENV != 'prod'))
    EXIT = True