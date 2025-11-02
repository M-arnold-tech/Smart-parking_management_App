# Park Smart - Smart Parking Management App

A clean, structured web application for parking management with individual pages and organized assets.

## Project Structure

```
Smart-parking_management_App/
├── login.html                 # Entry point - User login
├── pages/                     # Individual page files
│   ├── find-parking.html     # Browse parking spaces
│   ├── my-booking.html       # Book parking space
│   ├── payment.html          # Payment method selection
│   ├── payment-success.html  # Payment confirmation
│   └── active-booking.html   # Manage active booking
├── assets/                    # Shared resources
│   ├── styles.css            # All styling
│   └── script.js             # All functionality
└── README.md                 # This file
```

## Getting Started

1. Open **login.html** in your browser
2. Enter any email and password to login
3. Navigate through the app

## Navigation Flow

```
login.html
    ↓
pages/find-parking.html
    ↓
pages/my-booking.html
    ↓
pages/payment.html
    ↓
pages/payment-success.html
    ↓
pages/active-booking.html
```

## Features

- Individual HTML pages for each section
- Centralized CSS styling (assets/styles.css)
- Shared JavaScript functionality (assets/script.js)
- Responsive design
- Purple color scheme
- Clean code without emojis
- Functional login system
- Page-to-page navigation

## File Descriptions

### Root Level
- **login.html** - User authentication page

### Pages Folder
- **find-parking.html** - Browse available parking spaces
- **my-booking.html** - Select duration, vehicle type, and payment
- **payment.html** - Choose payment method
- **payment-success.html** - Booking confirmation
- **active-booking.html** - Manage current booking

### Assets Folder
- **styles.css** - Complete styling for all pages
- **script.js** - Shared JavaScript functions

## Customization

### Change Colors
Edit `assets/styles.css` - modify CSS variables at the top:
```css
:root {
    --primary: #6b21a8;
    --primary-dark: #581c87;
    /* ... */
}
```

### Add Parking Spaces
Edit `assets/script.js` - modify the `parkingSpaces` array

### Update Content
Edit individual HTML files in `pages/` folder

## Browser Compatibility

Works on all modern browsers:
- Chrome/Edge
- Firefox
- Safari
- Mobile browsers

## Responsive Design

- Mobile: 320px+
- Tablet: 768px+
- Desktop: 1024px+
