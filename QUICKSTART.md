# Quick Start Guide - Park Smart

## Getting Started in 3 Steps

### 1. Install Dependencies
```bash
npm install
```

### 2. Start Development Server
```bash
npm start
```
The app will automatically open at `http://localhost:3000`

### 3. Test the App

#### Sign In as Regular User
- Email: `user@example.com`
- Password: `password123`
- You'll be redirected to the Find Parking page

#### Sign In as Admin
- Email: `admin@example.com`
- Password: `password123`
- You'll be redirected to the Admin Dashboard

## Page Navigation

### User Flow
```
Sign In → Find Parking → My Booking → Active Booking
```

### Admin Flow
```
Sign In (with admin email) → Admin Dashboard
```

## Available Pages

| Page | Route | Description |
|------|-------|-------------|
| Sign In | `/` | Authentication page |
| Find Parking | `/find-parking` | Browse and search parking spaces |
| My Booking | `/my-booking` | Book a parking space |
| Active Booking | `/active-booking` | Manage current bookings |
| Admin Dashboard | `/admin-dashboard` | Admin statistics and management |

## Features to Try

### Find Parking Page
- Search for parking locations
- View available parking spaces with ratings
- See pricing and availability
- Click "Book Now" to proceed

### My Booking Page
- Select parking duration (0-1hr to 12hr)
- Choose vehicle type (Sedan, Normal, SUV & Truck)
- Review booking summary
- Select payment method

### Active Booking Page
- View current parking session details
- Renew parking session
- Confirm arrival
- Cancel booking
- Browse available spots

### Admin Dashboard
- View revenue statistics
- Monitor active bookings
- Check system performance
- Manage parking lists
- View usage statistics

## Building for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

## Troubleshooting

### Port 3000 Already in Use
If port 3000 is already in use, you can specify a different port:
```bash
PORT=3001 npm start
```

### Dependencies Issues
Clear node_modules and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

## Project Structure

```
src/
├── components/
│   ├── Header.js          # Top navigation
│   └── Footer.js          # Bottom footer
├── pages/
│   ├── SignIn.js          # Login page
│   ├── FindParking.js     # Browse parking
│   ├── MyBooking.js       # Booking page
│   ├── ActiveBooking.js   # Active sessions
│   └── AdminDashboard.js  # Admin panel
├── App.js                 # Main routing
├── index.js               # Entry point
└── index.css              # Global styles
```

## Next Steps

- Integrate with backend API
- Add real map functionality (Google Maps, Mapbox)
- Connect payment gateway (Stripe, PayPal)
- Implement user profiles
- Add booking history
- Set up notifications system

## Support

For issues or questions, refer to the main README.md file for detailed documentation.
