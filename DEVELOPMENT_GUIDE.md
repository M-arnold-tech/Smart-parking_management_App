# Park Smart - Development Guide

## Getting Started for Developers

### Prerequisites
- Node.js v14+ installed
- npm or yarn package manager
- Git for version control
- Code editor (VS Code recommended)

### Initial Setup

```bash
# 1. Navigate to project directory
cd Smart-parking_management_App

# 2. Install dependencies
npm install

# 3. Start development server
npm start

# 4. Open browser to http://localhost:3000
```

## Development Workflow

### File Organization

```
src/
├── components/          # Reusable UI components
│   ├── Header.js       # Navigation header
│   └── Footer.js       # Page footer
├── pages/              # Page components
│   ├── SignIn.js       # Login page
│   ├── FindParking.js  # Browse parking
│   ├── MyBooking.js    # Booking page
│   ├── ActiveBooking.js# Active sessions
│   └── AdminDashboard.js# Admin panel
├── App.js              # Main router
├── index.js            # Entry point
└── index.css           # Global styles
```

### Adding a New Page

1. Create file in `src/pages/NewPage.js`:
```javascript
import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

export default function NewPage({ onSignOut }) {
  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Header onSignOut={onSignOut} />
      <main className="flex-1 max-w-7xl mx-auto w-full px-4 py-6">
        {/* Your content here */}
      </main>
      <Footer />
    </div>
  );
}
```

2. Add route in `App.js`:
```javascript
import NewPage from './pages/NewPage';

// Inside Routes component:
<Route 
  path="/new-page" 
  element={isAuthenticated ? <NewPage onSignOut={handleSignOut} /> : <Navigate to="/" />} 
/>
```

### Adding a New Component

1. Create file in `src/components/NewComponent.js`:
```javascript
import React from 'react';

export default function NewComponent({ prop1, prop2 }) {
  return (
    <div className="component-styles">
      {/* Component content */}
    </div>
  );
}
```

2. Import and use in pages:
```javascript
import NewComponent from '../components/NewComponent';

// In JSX:
<NewComponent prop1="value" prop2="value" />
```

## Styling with Tailwind CSS

### Common Tailwind Classes Used

```javascript
// Layout
className="flex flex-col gap-4"           // Flexbox column with gap
className="grid grid-cols-1 md:grid-cols-2" // Responsive grid
className="max-w-7xl mx-auto"             // Max width container

// Spacing
className="px-4 py-6"                     // Padding
className="mb-4 mt-2"                     // Margins
className="gap-3"                         // Gap between items

// Colors
className="bg-purple-600"                 // Background
className="text-white"                    // Text color
className="border border-gray-300"        // Border

// Effects
className="rounded-lg"                    // Border radius
className="shadow-md"                     // Shadow
className="hover:bg-purple-700"           // Hover state
className="transition"                    // Smooth transition

// Responsive
className="hidden md:flex"                // Hide on mobile, show on tablet+
className="lg:col-span-2"                 // Span 2 columns on large screens
```

### Adding Custom Styles

Edit `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom component styles */
.custom-button {
  @apply bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition;
}

/* Custom utilities */
.card-shadow {
  @apply shadow-md rounded-lg;
}
```

## State Management

### Using React Hooks

```javascript
import React, { useState, useEffect } from 'react';

export default function MyComponent() {
  // State
  const [count, setCount] = useState(0);
  const [data, setData] = useState([]);
  
  // Effect (runs on mount and when dependencies change)
  useEffect(() => {
    // Fetch data
    console.log('Component mounted');
    
    return () => {
      // Cleanup
      console.log('Component unmounted');
    };
  }, [dependencies]);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

### Passing State Between Pages

Use App.js to manage authentication state:
```javascript
// In App.js
const [isAuthenticated, setIsAuthenticated] = useState(false);

// Pass to pages
<Route 
  path="/page" 
  element={<Page onSignOut={() => setIsAuthenticated(false)} />} 
/>
```

## Routing

### Current Routes

```
/                    → SignIn (public)
/find-parking        → FindParking (authenticated)
/my-booking          → MyBooking (authenticated)
/active-booking      → ActiveBooking (authenticated)
/admin-dashboard     → AdminDashboard (admin only)
```

### Adding New Routes

```javascript
import NewPage from './pages/NewPage';

// In App.js Routes:
<Route 
  path="/new-route" 
  element={
    isAuthenticated ? 
    <NewPage onSignOut={handleSignOut} /> : 
    <Navigate to="/" />
  } 
/>
```

### Navigation Between Pages

```javascript
import { useNavigate, Link } from 'react-router-dom';

// Using useNavigate hook
const navigate = useNavigate();
navigate('/find-parking');

// Using Link component
<Link to="/my-booking">Go to Booking</Link>
```

## Form Handling

### Basic Form Example

```javascript
const [formData, setFormData] = useState({
  email: '',
  password: ''
});

const handleChange = (e) => {
  const { name, value } = e.target;
  setFormData(prev => ({
    ...prev,
    [name]: value
  }));
};

const handleSubmit = (e) => {
  e.preventDefault();
  console.log('Form submitted:', formData);
  // Send to API
};

return (
  <form onSubmit={handleSubmit}>
    <input
      type="email"
      name="email"
      value={formData.email}
      onChange={handleChange}
      placeholder="Email"
      className="input-field"
    />
    <button type="submit">Submit</button>
  </form>
);
```

## Common Patterns

### Conditional Rendering

```javascript
{isAuthenticated ? (
  <Dashboard />
) : (
  <SignIn />
)}

{items.length > 0 && <ItemsList items={items} />}

{loading ? <Spinner /> : <Content />}
```

### List Rendering

```javascript
{parkingSpaces.map((space) => (
  <div key={space.id} className="space-card">
    <h3>{space.name}</h3>
    <p>{space.price}</p>
    <button onClick={() => bookSpace(space.id)}>Book</button>
  </div>
))}
```

### Event Handling

```javascript
// Click
<button onClick={() => handleClick()}>Click me</button>

// Input change
<input onChange={(e) => setValue(e.target.value)} />

// Form submit
<form onSubmit={(e) => handleSubmit(e)}>

// Hover
<div onMouseEnter={() => setHovered(true)}>Hover me</div>
```

## Debugging

### Console Logging

```javascript
console.log('Value:', value);           // Log value
console.error('Error:', error);         // Log error
console.warn('Warning:', warning);      // Log warning
console.table(arrayOfObjects);          // Log as table
```

### React DevTools

1. Install React DevTools browser extension
2. Open DevTools (F12)
3. Go to Components tab
4. Inspect component state and props

### Network Tab

1. Open DevTools (F12)
2. Go to Network tab
3. Make API calls
4. View request/response details

## Performance Tips

### Optimization Techniques

```javascript
// 1. Memoization
import { useMemo } from 'react';
const memoizedValue = useMemo(() => expensiveCalculation(), [dependency]);

// 2. Callback memoization
import { useCallback } from 'react';
const memoizedCallback = useCallback(() => {
  // function body
}, [dependency]);

// 3. Code splitting (future)
const LazyComponent = React.lazy(() => import('./Component'));

// 4. Avoid unnecessary renders
// Use keys in lists
// Lift state only when needed
// Use React.memo for pure components
```

## Testing

### Manual Testing Checklist

- [ ] All pages load without errors
- [ ] Navigation works between pages
- [ ] Forms accept input correctly
- [ ] Buttons trigger expected actions
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Sign in/out functionality works
- [ ] Admin detection works (email with "admin")
- [ ] Protected routes redirect properly

### Testing Credentials

```
Regular User:
Email: user@example.com
Password: password123

Admin User:
Email: admin@example.com
Password: password123
```

## Building for Production

```bash
# Create optimized build
npm run build

# Output in 'build' folder
# Ready to deploy to hosting service
```

## Deployment Options

### Netlify
```bash
npm install -g netlify-cli
netlify deploy --prod --dir=build
```

### Vercel
```bash
npm install -g vercel
vercel --prod
```

### GitHub Pages
```bash
npm install --save-dev gh-pages
# Add to package.json: "homepage": "https://username.github.io/repo"
npm run build
npm run deploy
```

## Environment Variables

Create `.env` file:
```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_ENABLE_MOCK_DATA=true
```

Access in code:
```javascript
const apiUrl = process.env.REACT_APP_API_URL;
```

## Troubleshooting

### Port 3000 Already in Use
```bash
PORT=3001 npm start
```

### Dependencies Issues
```bash
rm -rf node_modules package-lock.json
npm install
```

### Tailwind Styles Not Showing
- Ensure `tailwind.config.js` has correct content paths
- Check `index.css` has @tailwind directives
- Restart dev server

### Routes Not Working
- Verify routes in `App.js`
- Check component imports
- Ensure Router wraps all routes

## Resources

- [React Documentation](https://react.dev)
- [React Router Documentation](https://reactrouter.com)
- [Tailwind CSS Documentation](https://tailwindcss.com)
- [Lucide Icons](https://lucide.dev)

## Code Style Guidelines

### Naming Conventions
- Components: PascalCase (MyComponent)
- Functions: camelCase (myFunction)
- Constants: UPPER_CASE (MY_CONSTANT)
- CSS classes: kebab-case (my-class)

### File Organization
- One component per file
- Related files in same folder
- Descriptive file names
- Index files for exports

### Comments
```javascript
// Single line comment

/* Multi-line
   comment */

// TODO: Add feature
// FIXME: Fix bug
```

## Next Steps

1. **Backend Integration**: Connect to API endpoints
2. **Real Data**: Replace mock data with API responses
3. **Error Handling**: Add proper error messages
4. **Loading States**: Show loading indicators
5. **Validation**: Add form validation
6. **Testing**: Write unit and integration tests
7. **Deployment**: Deploy to production

---

Happy coding! 🚀
