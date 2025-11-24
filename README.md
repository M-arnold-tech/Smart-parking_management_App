# Smart Parking Management System

A full-stack web application for managing parking spaces, reservations, and payments. The system supports two types of users: **Drivers** (who book parking spots) and **Parking Operators** (who manage parking spots).

## 📋 Project Overview

This is a Flask-based REST API backend with a frontend built using HTML, CSS, and JavaScript. The system allows:

- **Drivers** to:

  - Sign up and log in
  - Browse available parking spots
  - Make reservations
  - Process payments
  - View their bookings

- **Parking Operators** to:
  - Sign up and log in
  - Manage parking spots
  - View reservations
  - Monitor their parking operations

## 🏗️ Architecture

### Project Structure

```
Smart-parking_management_App-main/
├── backend/                  # Flask API backend
│   ├── api/                  # API route blueprints
│   │   ├── authentication_api.py
│   │   ├── parking_api.py
│   │   ├── reservation_api.py
│   │   └── payment_api.py
│   ├── process/              # Business logic
│   │   ├── authentication.py
│   │   ├── parkingSpots.py
│   │   ├── reservations.py
│   │   └── payment.py
│   ├── app.py                # Main Flask application
│   ├── config.py             # Configuration
│   ├── database.py           # Database connection
│   ├── requirements.txt      # Python dependencies
│   ├── render.yaml           # Render deployment config
│   └── smart_space.sql       # Database schema
│
├── frontend/                 # Frontend (GitHub Pages)
│   ├── assets/
│   │   ├── css/              # Stylesheets
│   │   ├── js/               # JavaScript files
│   │   │   └── config.js     # API configuration
│   │   └── images/           # Image assets
│   ├── pages/                # HTML pages
│   │   ├── landing_page.html
│   │   ├── sign_up.html
│   │   ├── find_parking.html
│   │   ├── booking_page.html
│   │   ├── payment_page.html
│   │   ├── User_dashboard.html
│   │   └── ...
│   └── index.html            # GitHub Pages entry point
│
├── DEPLOYMENT.md             # Deployment guide
├── DATABASE_SETUP.md         # Local database setup
└── README.md                 # This file
```

### Deployment Architecture

- **Database**: Aiven (MySQL) - Cloud-hosted MySQL database
- **Backend**: Render - Flask API deployed as web service
- **Frontend**: GitHub Pages - Static site hosting

## 🚀 Quick Start (Local Development)

### Prerequisites

1. **Python 3.7+** installed
2. **MySQL Server** installed and running
3. **pip** (Python package manager)

### Installation Steps

#### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

#### 2. Set Up MySQL Database

See [DATABASE_SETUP.md](DATABASE_SETUP.md) for detailed instructions.

Quick setup:

```bash
# Create database
mysql -u root -p -e "CREATE DATABASE smart_spaces;"

# Import schema
mysql -u root -p smart_spaces < backend/smart_space.sql
```

#### 3. Configure Environment Variables

Create `backend/.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=smart_spaces
DB_PORT=3306
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
```

#### 4. Start the Flask Server

```bash
cd backend
python app.py
```

The server will start on `http://localhost:5000`

#### 5. Open Frontend

Open `frontend/pages/landing_page.html` in your browser, or use a local server:

```bash
cd frontend
python -m http.server 8000
# Then visit http://localhost:8000
```

## 🌐 Deployment

For production deployment to Aiven, Render, and GitHub Pages, see **[DEPLOYMENT.md](DEPLOYMENT.md)** for complete step-by-step instructions.

### Quick Deployment Summary

1. **Database (Aiven)**:

   - Create MySQL service on Aiven
   - Import `backend/smart_space.sql`
   - Get connection credentials

2. **Backend (Render)**:

   - Connect GitHub repository
   - Create web service
   - Set environment variables (Aiven credentials)
   - Deploy

3. **Frontend (GitHub Pages)**:
   - Update `frontend/assets/js/config.js` with Render backend URL
   - Enable GitHub Pages in repository settings
   - Deploy

## 📁 Key Files

### Backend

- `backend/app.py` - Main Flask application
- `backend/config.py` - Configuration management
- `backend/database.py` - Database connection handler
- `backend/api/*.py` - API endpoints
- `backend/process/*.py` - Business logic

### Frontend

- `frontend/assets/js/config.js` - **IMPORTANT**: API URL configuration
- `frontend/pages/*.html` - Application pages
- `frontend/index.html` - GitHub Pages entry point

## 🔧 Configuration

### Backend API URL

Update `frontend/assets/js/config.js`:

```javascript
const API_BASE_URL = isLocalhost
  ? "http://127.0.0.1:5000" // Local
  : "https://your-backend.onrender.com"; // Production
```

### Database Connection

Configure in `backend/config.py` or via environment variables:

- `DB_HOST` - Database host
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password
- `DB_NAME` - Database name
- `DB_PORT` - Database port (default: 3306)

## 📝 API Endpoints

### Authentication

- `POST /auth/driver/signup` - Register driver
- `POST /auth/driver/login` - Driver login
- `POST /auth/operator/signup` - Register operator
- `POST /auth/operator/login` - Operator login

### Parking

- `GET /parking/spots` - Get all parking spots
- `GET /parking/spots/<id>` - Get specific spot
- `POST /parking/spots` - Create parking spot (operator)

### Reservations

- `POST /reservation/book` - Create reservation
- `GET /reservation/driver/<id>` - Get driver reservations
- `PUT /reservation/<id>/cancel` - Cancel reservation

### Payments

- `POST /payment/initiate` - Initiate payment
- `PUT /payment/confirm` - Confirm payment

## 🐛 Troubleshooting

### Local Development

**Database Connection Issues**:

- Ensure MySQL is running
- Verify credentials in `.env` file
- Check database exists: `mysql -u root -p -e "SHOW DATABASES;"`

**Port Already in Use**:

- Change port in `backend/app.py`: `app.run(port=5001)`

**Module Not Found**:

- Install dependencies: `pip install -r backend/requirements.txt`
- Check Python environment

### Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) troubleshooting section for deployment-specific issues.

## 📚 Documentation

- [DEPLOYMENT.md](DEPLOYMENT.md) - Complete deployment guide
- [DATABASE_SETUP.md](DATABASE_SETUP.md) - Local database setup

## 🎯 Next Steps

1. Set up local development environment
2. Test all features locally
3. Deploy to production (see DEPLOYMENT.md)
4. Configure custom domain (optional)
5. Set up monitoring and backups

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

**Note**: Remember to update `frontend/assets/js/config.js` with your production backend URL after deploying to Render!
