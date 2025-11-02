# Park Smart - Smart Parking Management App

A modern, responsive web application for smart parking management built with React, Tailwind CSS, and React Router.

## Features

### User Pages
- **Sign In Page**: Authentication with email/phone and password, social login options (Apple, Email)
- **Find Parking**: Browse available parking spaces with real-time availability, ratings, and pricing
- **My Booking**: Reserve parking spaces with duration selection, vehicle type selection, and payment processing
- **Active Booking**: Manage active parking sessions with renewal, arrival confirmation, and cancellation options

### Admin Dashboard
- **Revenue Tracking**: Monitor monthly revenue generation
- **Booking Management**: View active bookings and available spots
- **System Performance**: Track system health, error rates, and usage statistics
- **Parking Management**: Manage parking lists and real-time data

## Tech Stack

- **Frontend Framework**: React 18.2.0
- **Routing**: React Router DOM 6.20.0
- **Styling**: Tailwind CSS 3.3.0
- **Icons**: Lucide React 0.294.0
- **HTTP Client**: Axios 1.6.0
- **Build Tool**: React Scripts 5.0.1

## Project Structure

```
src/
├── components/
│   ├── Header.js          # Navigation header with logo and user menu
│   └── Footer.js          # Footer with links
├── pages/
│   ├── SignIn.js          # Authentication page
│   ├── FindParking.js     # Browse parking spaces
│   ├── MyBooking.js       # Booking and payment page
│   ├── ActiveBooking.js   # Active booking management
│   └── AdminDashboard.js  # Admin statistics and management
├── App.js                 # Main app with routing
├── index.js               # React entry point
└── index.css              # Global styles with Tailwind
```

## Installation

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Setup Steps

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Start the development server**
   ```bash
   npm start
   ```
   The app will open at `http://localhost:3000`

3. **Build for production**
   ```bash
   npm run build
   ```

## Usage

### Navigation Flow

1. **Sign In**: Start at the login page
   - Use any email/phone and password to sign in as a regular user
   - Use an email containing "admin" to sign in as an admin
   - Social login buttons are available for Apple and Email

2. **Find Parking**: Browse available parking spaces
   - Search by location
   - View parking options with ratings and pricing
   - Click "Book Now" to proceed to booking

3. **My Booking**: Complete your parking reservation
   - Select parking duration
   - Choose vehicle type
   - Review booking summary
   - Select payment method and complete payment

4. **Active Booking**: Manage your current parking session
   - View session start and end times
   - Renew, confirm arrival, or cancel booking
   - Browse available spots for future bookings

5. **Admin Dashboard**: Monitor system performance (Admin only)
   - View revenue and booking statistics
   - Check system performance metrics
   - Manage parking lists

## Key Components

### Header Component
- Logo and branding
- Navigation links (Find parking, My booking, Active booking)
- User menu with notifications and sign out

### Footer Component
- Quick links (About Us, Contact Us, Terms of Service, Work with us)

### Pages Features

**SignIn.js**
- Email/phone and password input
- Social authentication buttons
- Sign up link
- Responsive design for mobile and desktop

**FindParking.js**
- Location search with map view
- Parking space cards with:
  - Images and names
  - Pricing information
  - Star ratings
  - Availability status
  - Book Now buttons

**MyBooking.js**
- Duration selection (0-1hr, 1-2hr, 2-3hr, 3-6hr, 12hr)
- Vehicle type selection (Sedan, Normal cars, SUV & Truck)
- Booking summary with cost breakdown
- Payment method selection
- Payment processing

**ActiveBooking.js**
- Session start and end time display
- Action buttons (Renew, Arrived, Cancel)
- Available spots grid
- Quick booking options

**AdminDashboard.js**
- Revenue statistics
- Active bookings counter
- Available spots tracker
- Today's activity log
- System performance metrics
- Error tracking
- Parking lists management
- Usage statistics

## Styling

The app uses Tailwind CSS for styling with a purple color scheme:
- Primary Color: Purple (#9333ea)
- Secondary Colors: Gray, Green, Red, Blue

All components are responsive and work on mobile, tablet, and desktop devices.

## Authentication Flow

The app includes a simple authentication system:
- Users are redirected to Sign In if not authenticated
- Admin users (email containing "admin") are redirected to Admin Dashboard
- Regular users are redirected to Find Parking
- Sign out functionality clears authentication state

## Future Enhancements

- Backend API integration for real data
- Real map integration (Google Maps, Mapbox)
- Payment gateway integration (Stripe, PayPal)
- User profile management
- Booking history
- Notifications system
- Real-time availability updates
- Mobile app version

## License

This project is part of the Smart Parking Management System.
