# Muhammad Talal Siddiqui — Flask Portfolio

A responsive personal portfolio built with Python and Flask, based on the supplied resume.

## Run locally

### Windows PowerShell

```powershell
cd talal_flask_portfolio
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

If PowerShell blocks activation, you can run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## Resume

The supplied resume is copied into `resume/Talal_Siddiqui_Resume_Updated.pdf`.

## Deployment

This project is suitable for Flask hosts such as Render. Use:

Build command:
`pip install -r requirements.txt`

Start command:
`gunicorn app:app`

For local development, `python app.py` is sufficient.

## Certification

The portfolio includes the supplied Microsoft Certified Professional certificate.
Achievement date: February 24, 2013.
