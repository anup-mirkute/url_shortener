
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from database import InMemoryDB
from utils import encode, decode
app = FastAPI()
db = InMemoryDB()


class URLInput(BaseModel):
    url: str

@app.post("/shorten")
def shorten_url(item: URLInput):
    db_id = db.insert(item.url)
    short_code = encode(db_id)
    
    return {
        "short_code": short_code,
        "short_url": f"http://localhost:8000/{short_code}"
    }

@app.get("/{short_code}")
def redirect_to_original(short_code: str):
    try:
        db_id = decode(short_code)
    except ValueError:
         raise HTTPException(status_code=404, detail="Invalid code format")

    original_url = db.get(db_id)
    
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
        
    return RedirectResponse(original_url)