Here's a complete `README.md` file with all content in one document:

```markdown
# Domain Info Lookup API 🌐

A FastAPI-based web service to retrieve domain registration details and subdomain information.

## Features

- 📅 **Domain Age Calculation**: Get creation date and age in days/years
- 🌐 **Subdomain Enumeration**: Discover known subdomains for a domain
- ⚡ **Fast & Simple**: RESTful API with JSON responses
- 📦 **Lightweight**: Minimal dependencies
- 🚀 **Production-ready**: Deployed on Render

```

## Usage

### Installation

1. Clone the repository:
```bash
git clone https://github.com/theshakawat/domain-info-lookup-python.git
cd domain-info-lookup-python
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

### API Endpoints

**GET** `/docs/`

Example request:
```bash
http://127.0.0.1:8000
```

Sample response:
```json
{
  "domain": "google.com",
  "creation_date": "1997-09-15",
  "age_days": 10041,
  "age_years": 28,
  "subdomains": [
    "*.apis.corp.google.com",
    "*.appengine.google.com",
    "*.auth.corp.google.com"
  ]
}
```

## Deployment

Live demo available at:  
[https://domain-info-mckw.onrender.com/](https://domain-info-mckw.onrender.com/)

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- python-whois
- Requests



---

**Note**: Replace `your-repo` in the clone URL with your actual GitHub repository name.  
For production use, consider adding rate limiting and authentication mechanisms.
```

This single-file documentation includes all key elements for developers to:
1. Understand the project's purpose
2. Set up the development environment
3. Test the API endpoints
4. Deploy the application
5. Extend or modify the codebase

The structure follows standard open-source project documentation conventions while maintaining readability and completeness.