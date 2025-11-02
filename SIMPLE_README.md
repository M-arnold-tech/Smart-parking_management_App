# Park Smart - Simple HTML/CSS/JS Version

This is a clean, simple implementation of the Park Smart frontend using only HTML, CSS, and JavaScript - no frameworks needed!

## 📁 Files

- **index.html** - All pages and structure
- **styles.css** - All styling
- **script.js** - All functionality

That's it! Just 3 files.

## 🚀 How to Use

### Option 1: Open Directly
Simply open `index.html` in your browser. That's all!

### Option 2: Use a Local Server (Recommended)
```bash
# Using Python 3
python -m http.server 8000

# Using Python 2
python -m SimpleHTTPServer 8000

# Using Node.js (with http-server)
npx http-server

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

## 📱 Pages Included

1. **Sign In** - Login page
2. **Find Parking** - Browse parking spaces
3. **My Booking** - Book a parking space
4. **Active Booking** - Manage current bookings
5. **Admin Dashboard** - Admin statistics

## 🔑 Test Credentials

### Regular User
- Email: `user@example.com`
- Password: `password123`

### Admin User
- Email: `admin@example.com`
- Password: `password123`

## ✨ Features

✅ All pages from Figma designs
✅ Responsive design (mobile, tablet, desktop)
✅ Purple color scheme
✅ Navigation between pages
✅ Admin role detection
✅ Sign out functionality
✅ Interactive buttons and forms
✅ No dependencies needed
✅ Fast loading
✅ Easy to customize

## 🎨 Customization

### Change Colors
Edit `styles.css` and modify the `:root` variables:
```css
:root {
    --primary: #6b21a8;  /* Change this */
    --primary-dark: #581c87;
    /* ... */
}
```

### Add More Parking Spaces
Edit `script.js` and add to `parkingSpaces` array:
```javascript
const parkingSpaces = [
    // ... existing spaces
    {
        id: 6,
        name: 'New parking',
        icon: '🏢',
        price: '400 frw / 1h',
        available: '50 available space',
        rating: 4
    }
];
```

### Change Text
All text is in `index.html`. Just search and replace.

## 📊 File Sizes

- index.html: ~25 KB
- styles.css: ~20 KB
- script.js: ~5 KB
- **Total: ~50 KB** (very lightweight!)

## 🚀 Deployment

### Netlify
1. Drag and drop the folder to Netlify
2. Done!

### GitHub Pages
1. Push to GitHub
2. Enable GitHub Pages in settings
3. Done!

### Any Web Host
1. Upload the 3 files
2. Done!

## 🔧 What You Can Add

- Backend API integration
- Real database
- Payment processing
- User authentication
- Email notifications
- SMS alerts
- Real maps
- Real images

## 📝 Notes

- All data is mock (for demonstration)
- No server needed to run
- Works offline
- Mobile responsive
- Fast and lightweight
- Easy to understand code

## 🎯 Next Steps

1. Open `index.html` in browser
2. Test all pages
3. Customize colors/text as needed
4. Add real data/API when ready
5. Deploy to web host

## 💡 Tips

- Use browser DevTools (F12) to inspect and debug
- Modify `script.js` to add more functionality
- Edit `styles.css` to change appearance
- Add more pages by copying existing page structure

## ✅ Everything Works!

Just open the file and start using it. No installation, no build process, no complications.

**Enjoy your Park Smart app!** 🚗
