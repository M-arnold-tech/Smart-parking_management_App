# Park Smart - App Structure & Flow

## Application Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        App.js (Router)                       │
│                  Authentication & Route Guard                │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
   ┌─────────┐        ┌─────────┐      ┌──────────────┐
   │ SignIn  │        │  User   │      │    Admin     │
   │ Page    │        │ Routes  │      │    Routes    │
   └─────────┘        └────┬────┘      └──────┬───────┘
                           │                  │
        ┌──────────────────┼──────────────────┤
        │                  │                  │
        ▼                  ▼                  ▼
   ┌──────────┐    ┌──────────────┐   ┌──────────────┐
   │ Header   │    │ Find Parking │   │ Admin        │
   │Component │    │ Page         │   │ Dashboard    │
   └──────────┘    │              │   │              │
        │          │ - Search     │   │ - Revenue    │
        │          │ - Browse     │   │ - Bookings   │
        │          │ - Ratings    │   │ - Performance│
        │          │ - Book Now   │   │ - Parking    │
        │          └──────┬───────┘   │   Lists      │
        │                 │           └──────────────┘
        │                 ▼
        │          ┌──────────────┐
        │          │ My Booking   │
        │          │ Page         │
        │          │              │
        │          │ - Duration   │
        │          │ - Vehicle    │
        │          │ - Payment    │
        │          └──────┬───────┘
        │                 │
        │                 ▼
        │          ┌──────────────┐
        │          │ Active       │
        │          │ Booking      │
        │          │              │
        │          │ - Session    │
        │          │ - Renew      │
        │          │ - Cancel     │
        │          └──────────────┘
        │
        ▼
   ┌──────────┐
   │ Footer   │
   │Component │
   └──────────┘
```

## Component Hierarchy

```
App
├── Router
│   ├── SignIn
│   │   └── Footer
│   ├── FindParking
│   │   ├── Header
│   │   └── Footer
│   ├── MyBooking
│   │   ├── Header
│   │   └── Footer
│   ├── ActiveBooking
│   │   ├── Header
│   │   └── Footer
│   └── AdminDashboard
│       ├── Header
│       └── Footer
```

## Data Flow

### Authentication Flow
```
User Input (Email/Password)
         │
         ▼
   Validate Input
         │
         ▼
   Check if Admin (email contains "admin")
         │
    ┌────┴────┐
    │          │
    ▼          ▼
  Admin      User
    │          │
    ▼          ▼
Admin Dashboard  Find Parking
```

### Booking Flow
```
Find Parking Page
         │
         ▼
   Select Parking
         │
         ▼
   My Booking Page
         │
    ┌────┴────┐
    │          │
    ▼          ▼
Duration   Vehicle Type
    │          │
    └────┬─────┘
         │
         ▼
   Payment Method
         │
         ▼
   Active Booking
         │
    ┌────┼────┐
    │    │    │
    ▼    ▼    ▼
  Renew Arrived Cancel
```

## State Management

### App.js State
```javascript
- isAuthenticated: boolean
- userRole: 'user' | 'admin'
```

### Page-Level State
- **SignIn**: email, password
- **FindParking**: location
- **MyBooking**: duration, vehicleType
- **ActiveBooking**: activeTab
- **AdminDashboard**: none (display only)

## Routing Map

| Route | Component | Auth Required | Role |
|-------|-----------|---------------|------|
| `/` | SignIn | No | Public |
| `/find-parking` | FindParking | Yes | User |
| `/my-booking` | MyBooking | Yes | User |
| `/active-booking` | ActiveBooking | Yes | User |
| `/admin-dashboard` | AdminDashboard | Yes | Admin |

## Component Props

### Header
```javascript
Props:
- onSignOut: Function
- showNav: Boolean (default: true)
```

### Footer
```javascript
Props: None (static component)
```

### Pages
```javascript
Props:
- onSignOut: Function (all pages)
```

## Styling System

### Tailwind CSS Utilities Used
- **Layout**: flex, grid, gap, max-w, mx-auto, px, py
- **Colors**: bg-purple-*, text-*, border-*
- **Effects**: shadow-md, rounded-lg, hover:*, transition
- **Responsive**: hidden, md:flex, lg:col-span-*

### Color Scheme
```
Primary: Purple (#9333ea)
├── Light: #f3e8ff
├── Dark: #7e22ce
└── Darker: #6b21a8

Secondary Colors:
├── Gray: #6b7280
├── Green: #16a34a
├── Red: #dc2626
└── Blue: #2563eb
```

## File Size Overview

```
src/
├── App.js                    (~1.6 KB)
├── index.js                  (~0.3 KB)
├── index.css                 (~0.9 KB)
├── components/
│   ├── Header.js             (~1.2 KB)
│   └── Footer.js             (~0.5 KB)
└── pages/
    ├── SignIn.js             (~2.8 KB)
    ├── FindParking.js        (~3.5 KB)
    ├── MyBooking.js          (~4.2 KB)
    ├── ActiveBooking.js      (~3.8 KB)
    └── AdminDashboard.js     (~3.5 KB)

Total: ~26 KB (source code)
```

## Browser Compatibility

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile browsers: iOS Safari 12+, Chrome Android

## Performance Considerations

- Code splitting via React Router
- Lazy loading ready (can be added)
- Optimized Tailwind CSS build
- Minimal dependencies (5 main packages)
- Responsive images with emoji placeholders

## Future Enhancements

### Phase 1: Backend Integration
- Connect to REST API
- Real-time data updates
- User authentication with JWT
- Payment processing

### Phase 2: Advanced Features
- Real map integration
- Push notifications
- Booking history
- User reviews and ratings
- Advanced search filters

### Phase 3: Optimization
- Code splitting
- Image optimization
- Service workers
- Offline support
- PWA capabilities

### Phase 4: Mobile App
- React Native version
- Native payment integration
- GPS tracking
- Offline maps
