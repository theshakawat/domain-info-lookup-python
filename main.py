from fastapi import FastAPI, HTTPException, Request
from datetime import datetime
import whois
import requests

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allow all origin, or specify your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
async def render_homepage(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/website-age/")
def get_website_age(domain: str):
    try:
        # fetch domain information using the whois package
        # fetch domain information using the whois package
        domain_info = whois.whois(domain)
        if domain_info.creation_date:
            creation_date = domain_info.creation_date
            if isinstance(creation_date, list):
                creation_date = creation_date[0]

                # calculate the age
                current_time = datetime.now()
                age_in_days = (current_time - creation_date).days
                age_in_years = age_in_days / 364.25

                return {
                    "domain": domain,
                    "creation_date": creation_date.strftime("%Y-%m-%d"),
                    "age_in_days": age_in_days,
                    "age_in_years": round(age_in_years)
                }
        else:
            raise HTTPException(status_code=404,detail="creation date not found!!")
    except Exception as e:
        return HTTPException(status_code=500,detail=str(e))

@app.get("/find-subdomains/{domain}")
def find_subdomain(domain: str):
    url = f"https://crt.sh/?q={domain}&output=json"
    response = requests.get(url)

    # check if the response is successful
    if response.status_code == 200:
        data = response.json()
        subdomains = set()  # use a set to avoid duplicate
        for i in data:
            name_value = i.get('name_value')
            if name_value:
                # split the subdomain names on newline characters and add to set
                subdomains.update(name_value.split('\n'))

        return {"domain": domain, "subdomains": sorted(subdomains)}
    else:
        return {"error": f"Error fetching subdomain for {domain}, status code: {response.status_code}"}