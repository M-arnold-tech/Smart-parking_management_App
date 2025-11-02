# API Integration Guide

This guide explains how to integrate the Park Smart frontend with a backend API.

## Current State

The app currently uses **mock data** for demonstration. All parking spaces, bookings, and admin statistics are hardcoded in the components.

## Integration Points

### 1. Authentication (SignIn.js)

**Current Implementation:**
```javascript
// Mock authentication
if (email && password) {
  const isAdmin = email.includes('admin');
  onSignIn(isAdmin ? 'admin' : 'user');
}
```

**API Integration:**
```javascript
// Replace with API call
const handleSignIn = async (e) => {
  e.preventDefault();
  try {
    const response = await axios.post('/api/auth/login', {
      email,
      password
    });
    
    // Store token
    localStorage.setItem('token', response.data.token);
    
    // Determine role
    const isAdmin = response.data.role === 'admin';
    onSignIn(isAdmin ? 'admin' : 'user');
    
  } catch (error) {
    console.error('Login failed:', error);
  }
};
```

### 2. Find Parking (FindParking.js)

**Current Implementation:**
```javascript
const [parkingSpaces] = useState([
  { id: 1, name: 'Chic parking', ... },
  // ... hardcoded data
]);
```

**API Integration:**
```javascript
const [parkingSpaces, setParkingSpaces] = useState([]);
const [loading, setLoading] = useState(true);

useEffect(() => {
  const fetchParkingSpaces = async () => {
    try {
      const response = await axios.get('/api/parking/spaces', {
        params: { location }
      });
      setParkingSpaces(response.data);
    } catch (error) {
      console.error('Failed to fetch parking spaces:', error);
    } finally {
      setLoading(false);
    }
  };
  
  fetchParkingSpaces();
}, [location]);
```

### 3. My Booking (MyBooking.js)

**API Endpoints Needed:**
```
POST /api/bookings/create
- Request: { parkingId, duration, vehicleType, paymentMethod }
- Response: { bookingId, totalPrice, confirmationCode }

POST /api/payments/process
- Request: { bookingId, paymentMethod, amount }
- Response: { transactionId, status }
```

**Implementation Example:**
```javascript
const handleBooking = async () => {
  try {
    // Create booking
    const bookingResponse = await axios.post('/api/bookings/create', {
      parkingId: selectedParking.id,
      duration,
      vehicleType,
    });
    
    // Process payment
    const paymentResponse = await axios.post('/api/payments/process', {
      bookingId: bookingResponse.data.bookingId,
      paymentMethod,
      amount: bookingResponse.data.totalPrice
    });
    
    if (paymentResponse.data.status === 'success') {
      navigate('/active-booking');
    }
  } catch (error) {
    console.error('Booking failed:', error);
  }
};
```

### 4. Active Booking (ActiveBooking.js)

**API Endpoints Needed:**
```
GET /api/bookings/active
- Response: [{ id, parkingName, startTime, endTime, status }]

POST /api/bookings/{id}/renew
- Request: { duration }
- Response: { newEndTime, additionalCost }

POST /api/bookings/{id}/cancel
- Response: { refundAmount, status }

POST /api/bookings/{id}/confirm-arrival
- Response: { status }
```

**Implementation Example:**
```javascript
useEffect(() => {
  const fetchActiveBookings = async () => {
    try {
      const response = await axios.get('/api/bookings/active', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setActiveBookings(response.data);
    } catch (error) {
      console.error('Failed to fetch bookings:', error);
    }
  };
  
  fetchActiveBookings();
}, []);

const handleRenew = async (bookingId) => {
  try {
    const response = await axios.post(`/api/bookings/${bookingId}/renew`, {
      duration: '2-3hr'
    });
    // Update UI with new end time
  } catch (error) {
    console.error('Renewal failed:', error);
  }
};
```

### 5. Admin Dashboard (AdminDashboard.js)

**API Endpoints Needed:**
```
GET /api/admin/dashboard
- Response: {
    revenue: number,
    activeBookings: number,
    availableSpots: number,
    todayActivity: number,
    systemStatus: string,
    systemPerformance: number,
    errors: number,
    parkingLists: number,
    usage: number
  }

GET /api/admin/parking-lists
- Response: [{ id, name, location, capacity, available }]

POST /api/admin/parking-lists/create
- Request: { name, location, capacity }
- Response: { id, name, ... }
```

**Implementation Example:**
```javascript
useEffect(() => {
  const fetchDashboardData = async () => {
    try {
      const response = await axios.get('/api/admin/dashboard', {
        headers: { Authorization: `Bearer ${adminToken}` }
      });
      setDashboardData(response.data);
    } catch (error) {
      console.error('Failed to fetch dashboard:', error);
    }
  };
  
  fetchDashboardData();
}, []);
```

## Backend API Structure

### Recommended Endpoints

```
Authentication
POST   /api/auth/login
POST   /api/auth/logout
POST   /api/auth/register
POST   /api/auth/refresh-token

Parking Spaces
GET    /api/parking/spaces
GET    /api/parking/spaces/{id}
GET    /api/parking/spaces/search
POST   /api/parking/spaces (admin)
PUT    /api/parking/spaces/{id} (admin)
DELETE /api/parking/spaces/{id} (admin)

Bookings
GET    /api/bookings
GET    /api/bookings/{id}
GET    /api/bookings/active
POST   /api/bookings/create
PUT    /api/bookings/{id}
POST   /api/bookings/{id}/cancel
POST   /api/bookings/{id}/renew
POST   /api/bookings/{id}/confirm-arrival

Payments
POST   /api/payments/process
GET    /api/payments/{id}
GET    /api/payments/history

Admin
GET    /api/admin/dashboard
GET    /api/admin/parking-lists
POST   /api/admin/parking-lists
GET    /api/admin/bookings
GET    /api/admin/revenue
GET    /api/admin/system-status

Users
GET    /api/users/profile
PUT    /api/users/profile
GET    /api/users/history
```

## Environment Configuration

Create `.env` file in project root:

```env
REACT_APP_API_BASE_URL=http://localhost:5000
REACT_APP_API_TIMEOUT=10000
REACT_APP_ENABLE_MOCK_DATA=false
```

## Axios Configuration

Create `src/services/api.js`:

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
  timeout: process.env.REACT_APP_API_TIMEOUT,
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      localStorage.removeItem('token');
      window.location.href = '/';
    }
    return Promise.reject(error);
  }
);

export default api;
```

## Error Handling

```javascript
try {
  const response = await api.get('/endpoint');
  // Handle success
} catch (error) {
  if (error.response) {
    // Server responded with error
    console.error('Error:', error.response.status, error.response.data);
  } else if (error.request) {
    // Request made but no response
    console.error('No response:', error.request);
  } else {
    // Error in request setup
    console.error('Error:', error.message);
  }
}
```

## Testing API Integration

### Using Mock Data (Development)
Set `REACT_APP_ENABLE_MOCK_DATA=true` in `.env`

### Using Real API
Set `REACT_APP_ENABLE_MOCK_DATA=false` and ensure backend is running

### Testing Tools
- Postman: Test API endpoints
- React DevTools: Debug component state
- Network tab: Monitor API calls

## Security Considerations

1. **Token Storage**: Use secure storage (httpOnly cookies preferred)
2. **CORS**: Configure backend to accept requests from frontend domain
3. **Validation**: Validate all user inputs before sending to API
4. **Rate Limiting**: Implement rate limiting on backend
5. **HTTPS**: Use HTTPS in production
6. **Sensitive Data**: Never expose API keys in frontend code

## Performance Optimization

1. **Caching**: Implement request caching for parking spaces
2. **Pagination**: Load bookings/spaces in pages
3. **Debouncing**: Debounce search requests
4. **Lazy Loading**: Load data on demand
5. **Compression**: Enable gzip compression on backend

## Migration Checklist

- [ ] Set up backend API
- [ ] Create API service layer
- [ ] Update SignIn.js with authentication
- [ ] Update FindParking.js with parking spaces API
- [ ] Update MyBooking.js with booking API
- [ ] Update ActiveBooking.js with active bookings API
- [ ] Update AdminDashboard.js with admin API
- [ ] Add error handling and loading states
- [ ] Test all endpoints
- [ ] Set up environment variables
- [ ] Deploy to production
