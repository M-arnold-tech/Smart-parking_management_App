# Park Smart - Files Reference Guide

## Complete File Listing

### Root Configuration Files

| File | Purpose | Key Content |
|------|---------|-------------|
| `package.json` | Dependencies & scripts | React, Router, Tailwind, Lucide |
| `tailwind.config.js` | Tailwind configuration | Theme colors, content paths |
| `postcss.config.js` | PostCSS configuration | Tailwind & autoprefixer |
| `.gitignore` | Git ignore rules | node_modules, build, .env |

### Documentation Files

| File | Purpose | Read When |
|------|---------|-----------|
| `README.md` | Complete documentation | First time setup |
| `QUICKSTART.md` | 3-step quick start | Want to run immediately |
| `PROJECT_SUMMARY.md` | Project overview | Need project status |
| `APP_STRUCTURE.md` | Architecture & diagrams | Understanding structure |
| `API_INTEGRATION_GUIDE.md` | Backend integration | Connecting to API |
| `DEVELOPMENT_GUIDE.md` | Development workflow | Contributing to code |
| `FILES_REFERENCE.md` | This file | Finding files |

### Public Files

| File | Purpose |
|------|---------|
| `public/index.html` | HTML entry point |

### Source Files - Components

| File | Location | Purpose | Key Exports |
|------|----------|---------|------------|
| `Header.js` | `src/components/` | Navigation header | Header component |
| `Footer.js` | `src/components/` | Page footer | Footer component |

### Source Files - Pages

| File | Location | Route | Purpose |
|------|----------|-------|---------|
| `SignIn.js` | `src/pages/` | `/` | User authentication |
| `FindParking.js` | `src/pages/` | `/find-parking` | Browse parking spaces |
| `MyBooking.js` | `src/pages/` | `/my-booking` | Book parking space |
| `ActiveBooking.js` | `src/pages/` | `/active-booking` | Manage bookings |
| `AdminDashboard.js` | `src/pages/` | `/admin-dashboard` | Admin statistics |

### Source Files - Core

| File | Location | Purpose |
|------|----------|---------|
| `App.js` | `src/` | Main router & auth |
| `index.js` | `src/` | React entry point |
| `index.css` | `src/` | Global styles |

## File Details

### package.json
```json
{
  "name": "park-smart",
  "version": "0.1.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "lucide-react": "^0.294.0",
    "axios": "^1.6.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  }
}
```

### App.js Structure
```
App
├── State: isAuthenticated, userRole
├── Routes:
│   ├── / → SignIn
│   ├── /find-parking → FindParking
│   ├── /my-booking → MyBooking
│   ├── /active-booking → ActiveBooking
│   └── /admin-dashboard → AdminDashboard
└── Auth Guard: Protects routes
```

### Component Props

#### Header Component
```javascript
Props: {
  onSignOut: Function,
  showNav: Boolean (optional)
}
```

#### Footer Component
```javascript
Props: None (static)
```

#### Page Components
```javascript
Props: {
  onSignOut: Function
}
```

## File Sizes

```
Documentation:
- README.md                    ~5.2 KB
- QUICKSTART.md               ~3.0 KB
- PROJECT_SUMMARY.md          ~6.5 KB
- APP_STRUCTURE.md            ~7.6 KB
- API_INTEGRATION_GUIDE.md    ~8.6 KB
- DEVELOPMENT_GUIDE.md        ~8.5 KB
- FILES_REFERENCE.md          ~3.5 KB

Configuration:
- package.json                ~0.8 KB
- tailwind.config.js          ~0.5 KB
- postcss.config.js           ~0.1 KB
- .gitignore                  ~0.3 KB

Source Code:
- src/App.js                  ~1.6 KB
- src/index.js                ~0.3 KB
- src/index.css               ~0.9 KB
- src/components/Header.js    ~1.2 KB
- src/components/Footer.js    ~0.5 KB
- src/pages/SignIn.js         ~2.8 KB
- src/pages/FindParking.js    ~3.5 KB
- src/pages/MyBooking.js      ~4.2 KB
- src/pages/ActiveBooking.js  ~3.8 KB
- src/pages/AdminDashboard.js ~3.5 KB

HTML:
- public/index.html           ~0.4 KB

Total Source: ~26 KB
Total with Docs: ~60 KB
```

## Quick File Navigation

### To Modify...

**Authentication Logic**
→ `src/App.js` (state management)
→ `src/pages/SignIn.js` (login form)

**Navigation/Header**
→ `src/components/Header.js`

**Styling**
→ `src/index.css` (global)
→ `tailwind.config.js` (theme)
→ Individual component files (inline classes)

**Add New Page**
→ Create file in `src/pages/`
→ Add route in `src/App.js`
→ Import Header & Footer

**Add New Component**
→ Create file in `src/components/`
→ Import in pages where needed

**Dependencies**
→ `package.json`
→ Run `npm install`

**Build Configuration**
→ `tailwind.config.js`
→ `postcss.config.js`

## File Dependencies

```
index.html
    ↓
index.js
    ↓
App.js
    ├── SignIn.js
    │   └── Footer.js
    ├── FindParking.js
    │   ├── Header.js
    │   └── Footer.js
    ├── MyBooking.js
    │   ├── Header.js
    │   └── Footer.js
    ├── ActiveBooking.js
    │   ├── Header.js
    │   └── Footer.js
    └── AdminDashboard.js
        ├── Header.js
        └── Footer.js

Styling:
index.css
    ↓
tailwind.config.js
    ↓
postcss.config.js
```

## Development Workflow

### Starting Development
1. Open `README.md` or `QUICKSTART.md`
2. Run `npm install`
3. Run `npm start`
4. Edit files in `src/`
5. Changes auto-reload

### Adding Features
1. Read `DEVELOPMENT_GUIDE.md`
2. Create new file in appropriate folder
3. Import in parent component
4. Add styles with Tailwind classes
5. Test in browser

### Integrating Backend
1. Read `API_INTEGRATION_GUIDE.md`
2. Update `src/App.js` authentication
3. Update page components with API calls
4. Replace mock data with real data
5. Add error handling

### Deploying
1. Run `npm run build`
2. Follow deployment guide in `README.md`
3. Deploy `build/` folder
4. Test in production

## File Modification Guide

### Safe to Modify
- ✅ All files in `src/pages/`
- ✅ All files in `src/components/`
- ✅ `src/index.css`
- ✅ `tailwind.config.js`
- ✅ `package.json` (add dependencies)

### Careful When Modifying
- ⚠️ `src/App.js` (affects routing)
- ⚠️ `src/index.js` (entry point)
- ⚠️ `public/index.html` (DOM structure)

### Don't Modify
- ❌ `.git/` (version control)
- ❌ `node_modules/` (dependencies)
- ❌ `.gitignore` (unless intentional)

## Common File Edits

### To Change Colors
Edit `tailwind.config.js`:
```javascript
theme: {
  extend: {
    colors: {
      purple: { /* custom colors */ }
    }
  }
}
```

### To Add Global Styles
Edit `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Add custom styles here */
```

### To Add Dependencies
Edit `package.json`:
```json
"dependencies": {
  "new-package": "^1.0.0"
}
```
Then run: `npm install`

### To Change Routes
Edit `src/App.js`:
```javascript
<Route path="/new-route" element={<NewPage />} />
```

## File Checklist

### Essential Files (Required)
- [x] `package.json`
- [x] `public/index.html`
- [x] `src/index.js`
- [x] `src/App.js`
- [x] `tailwind.config.js`
- [x] `postcss.config.js`

### Component Files (Required)
- [x] `src/components/Header.js`
- [x] `src/components/Footer.js`

### Page Files (Required)
- [x] `src/pages/SignIn.js`
- [x] `src/pages/FindParking.js`
- [x] `src/pages/MyBooking.js`
- [x] `src/pages/ActiveBooking.js`
- [x] `src/pages/AdminDashboard.js`

### Styling Files (Required)
- [x] `src/index.css`

### Documentation (Helpful)
- [x] `README.md`
- [x] `QUICKSTART.md`
- [x] `PROJECT_SUMMARY.md`
- [x] `APP_STRUCTURE.md`
- [x] `API_INTEGRATION_GUIDE.md`
- [x] `DEVELOPMENT_GUIDE.md`
- [x] `FILES_REFERENCE.md`

## Next Steps

1. **Read**: Start with `QUICKSTART.md`
2. **Setup**: Run `npm install && npm start`
3. **Explore**: Test all pages in the app
4. **Develop**: Use `DEVELOPMENT_GUIDE.md` for changes
5. **Integrate**: Follow `API_INTEGRATION_GUIDE.md` for backend
6. **Deploy**: Build and deploy using `README.md`

---

**Last Updated**: November 2, 2025
**Total Files**: 19 (7 docs + 12 source)
**Total Size**: ~60 KB
