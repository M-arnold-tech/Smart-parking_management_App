# Smart-parking_management_App (Backend)

Lightweight Flask backend for the Smart Spaces parking project. Provides authentication, parking spot management, reservations and payments backed by MySQL.

## Quick status
- Intended for local development. CORS is enabled.
- Known: some SQL/logic issues were identified and a minimal safe-pass was applied (env config, some SQL fixes). See "Notes" below.

## Prerequisites
- Python 3.8+
- MySQL Server (local or remote)
- Recommended: create and use a virtual environment

## Setup (Windows / PowerShell)
1. Create & activate a venv
	```powershell
	python -m venv .venv
	.venv\Scripts\Activate.ps1   # or use activate.bat if PowerShell blocks scripts
	```
2. Install dependencies
	```powershell
	pip install --upgrade pip
	pip install -r requirements.txt
	```
3. Configure environment
	- Copy the example: `Copy-Item .env.example .env`
	- Edit `.env` and set `DB_PASSWORD` and `DB_NAME` (for example `smart_spaces`).
	- The app loads `.env` via `python-dotenv` (already used in `config.py`).

4. Create the database and import schema
	```powershell
	# create DB (if needed) and import schema file
	mysql -u <user> -p -e "CREATE DATABASE IF NOT EXISTS smart_spaces;"
	mysql -u <user> -p smart_spaces < smart_space.sql
	```

## Run
```powershell
python app.py
```
Visit `http://127.0.0.1:5000/` to confirm the server is running.

## Main API endpoints (summary)
- `POST /auth/driver/signup` — driver registration (JSON body: username, email, phone_number, vehicle_plate, password)
- `POST /auth/driver/login` — driver login (username, password)
- `POST /auth/operator/signup` — operator registration
- `POST /parking/add` — operator adds parking spot (operator_id, location, price_per_hour, total_spots)
- `GET /parking/available` — list available parking spots
- `POST /reservation/book` — create reservation (driver_id, spot_id, start_time, end_time, total_price)
- `PUT /reservation/cancel` — cancel reservation (res_id)
- `PUT /reservation/checkout` — checkout (res_id)
- `POST /payment/initiate` — initiate payment (res_id, amount, payment_method)
- `PUT /payment/confirm` — confirm payment (payment_id, success)

See the `api/` and `process/` modules for full payloads and behavior.

