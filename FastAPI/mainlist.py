from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

import requests

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone: str

templates = Jinja2Templates(directory="templates")

## ------------------------------------------------------------------------------------
## Models
## ------------------------------------------------------------------------------------

class City(BaseModel):
    name: str
    timezone: str

class CityModify(BaseModel):
    id: int
    name: str
    timezone: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/cities', response_class=HTMLResponse)
def get_cities(request: Request):
    context = {}

    rsCity = []

    cnt = 0
    for city in db:
        str = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        #print(str)
        r = requests.get(str)
        cur_time = r.json()['datetime']

        cnt += 1

        rsCity.append({'id': cnt, 'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time})

    #print(rsCity)

    context['request'] = request
    context['rsCity'] = rsCity

    return templates.TemplateResponse("city_list.html", context)


@app.get('/cities/{city_id}', response_class=HTMLResponse)
def get_city(request: Request, city_id: int):
    city = db[city_id-1]
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
    cur_time = r.json()['datetime']

    # return {'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}
    context = {'request':request, 'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}
    return templates.TemplateResponse("city_detail.html", context)


@app.post('/cities')
def create_city(city: City):

    db.append(city.dict())

    return db[-1]


@app.put('/cities')
def modify_city(city: CityModify):

    db[city.id-1] = { 'name': city.name, 'timezone': city.timezone }

    return db[city.id-1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)

    return {'result_msg':'Deleted...'}




