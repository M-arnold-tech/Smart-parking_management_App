// Parking data
const parkingSpaces = [
    {
        id: 1,
        name: 'Chic parking',
        icon: '🏢',
        price: '600 frw / 1h',
        available: '25 available space',
        rating: 4.5
    },
    {
        id: 2,
        name: 'Mic parking',
        icon: '🏗️',
        price: '400 frw / 1h',
        available: '65 available space',
        rating: 3.5
    },
    {
        id: 3,
        name: 'City center parking',
        icon: '🏙️',
        price: '500 frw / 1h',
        available: '40 available space',
        rating: 3.5
    },
    {
        id: 4,
        name: 'Makuza parking',
        icon: '🌆',
        price: '600 frw / 1h',
        available: '150 available space',
        rating: 4
    },
    {
        id: 5,
        name: 'Kigali hall parking',
        icon: '🏛️',
        price: '500 frw / 1h',
        available: '80 available space',
        rating: 5
    }
];

// Available spots for active booking
const availableSpots = [
    { id: 1, name: 'City center parking', icon: '🏙️', available: true },
    { id: 2, name: 'Makuza parking', icon: '🌆', available: false },
    { id: 3, name: 'Mic parking', icon: '🏗️', available: true },
    { id: 4, name: 'Chic parking', icon: '🏢', available: true }
];

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
    // Load parking cards
    loadParkingCards();
    loadSpots();
    
    // Handle sign in form
    const signinForm = document.getElementById('signin-form');
    if (signinForm) {
        signinForm.addEventListener('submit', handleSignIn);
    }
});

// Show/hide pages
function showPage(pageId) {
    // Hide all pages
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => page.classList.remove('active'));
    
    // Show selected page
    const selectedPage = document.getElementById(pageId);
    if (selectedPage) {
        selectedPage.classList.add('active');
    }
}

// Handle sign in
function handleSignIn(e) {
    e.preventDefault();
    
    const email = document.querySelector('#signin-form input[type="email"]').value;
    const password = document.querySelector('#signin-form input[type="password"]').value;
    
    if (email && password) {
        // Check if admin
        if (email.includes('admin')) {
            showPage('admin-page');
        } else {
            showPage('find-parking-page');
        }
    }
}

// Sign out
function signOut() {
    showPage('signin-page');
    // Clear form
    const signinForm = document.getElementById('signin-form');
    if (signinForm) {
        signinForm.reset();
    }
}

// Load parking cards
function loadParkingCards() {
    const container = document.getElementById('parking-cards');
    if (!container) return;
    
    container.innerHTML = parkingSpaces.map((space, index) => `
        <div class="parking-card">
            <div class="parking-image">${space.icon}</div>
            <div class="parking-info">
                <div class="parking-name">${space.name}</div>
                <div class="parking-available">${space.available}</div>
                <div class="parking-rating">
                    ${generateStars(space.rating)}
                    <span>${space.rating}</span>
                </div>
            </div>
            <div class="parking-actions">
                <div class="parking-price">${space.price}</div>
                <button class="btn btn-primary" onclick="viewParkingDetails(${index + 1})">Book Now</button>
            </div>
        </div>
    `).join('');
}

// Generate star rating
function generateStars(rating) {
    let stars = '';
    for (let i = 0; i < 5; i++) {
        if (i < Math.floor(rating)) {
            stars += '⭐';
        } else {
            stars += '☆';
        }
    }
    return stars;
}

// Load available spots
function loadSpots() {
    const container = document.getElementById('spots-grid');
    if (!container) return;
    
    container.innerHTML = availableSpots.map(spot => `
        <div class="spot-card">
            <div class="spot-image">${spot.icon}</div>
            <div class="spot-info">
                <div class="spot-name">${spot.name}</div>
                <div class="spot-footer">
                    <span class="spot-status">${spot.available ? 'Available' : 'Booked'}</span>
                    <button class="spot-btn" onclick="showPage('my-booking-page')">Book Now</button>
                </div>
            </div>
        </div>
    `).join('');
}

// Select duration
function selectDuration(element, duration) {
    document.querySelectorAll('.duration-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    element.classList.add('active');
}

// Select vehicle
function selectVehicle(element, vehicle) {
    document.querySelectorAll('.vehicle-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    element.classList.add('active');
}

// Countdown timer (optional - for active booking)
function startCountdown() {
    const countdownElements = document.querySelectorAll('.countdown');
    
    countdownElements.forEach(element => {
        let seconds = 72; // 1 minute 12 seconds
        
        const timer = setInterval(() => {
            const hours = Math.floor(seconds / 3600);
            const minutes = Math.floor((seconds % 3600) / 60);
            const secs = seconds % 60;
            
            element.textContent = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            
            if (seconds > 0) {
                seconds--;
            } else {
                clearInterval(timer);
            }
        }, 1000);
    });
}

// Start countdown when active booking page is shown
const observer = new MutationObserver(() => {
    const activeBookingPage = document.getElementById('active-booking-page');
    if (activeBookingPage && activeBookingPage.classList.contains('active')) {
        startCountdown();
    }
});

observer.observe(document.body, { attributes: true, subtree: true });

// Navigation history for back button
let pageHistory = [];

// Go back to previous page
function goBack() {
    if (pageHistory.length > 1) {
        pageHistory.pop(); // Remove current page
        const previousPage = pageHistory[pageHistory.length - 1];
        showPage(previousPage);
    }
}

// Update showPage to track history
const originalShowPage = showPage;
showPage = function(pageId) {
    pageHistory.push(pageId);
    originalShowPage(pageId);
};

// Select payment method
function selectPaymentMethod(element, method) {
    // Remove active from all cards
    document.querySelectorAll('.payment-method-card').forEach(card => {
        card.classList.remove('active');
    });
    
    // Add active to selected card
    element.classList.add('active');
    
    // Hide all forms
    document.getElementById('card-form').style.display = 'none';
    document.getElementById('mobile-form').style.display = 'none';
    
    // Show selected form
    if (method === 'card') {
        document.getElementById('card-form').style.display = 'block';
    } else if (method === 'mobile') {
        document.getElementById('mobile-form').style.display = 'block';
    }
}

// Process payment
function processPayment() {
    // Simulate payment processing
    alert('Processing payment...');
    
    // Show success page
    showPage('payment-success-page');
    
    // Set booking date
    const today = new Date();
    const dateStr = today.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    });
    document.getElementById('booking-date').textContent = dateStr;
}

// View parking details
function viewParkingDetails(parkingId) {
    const parking = parkingSpaces[parkingId - 1];
    if (parking) {
        document.getElementById('detail-name').textContent = parking.name;
        document.getElementById('detail-price').textContent = parking.price;
        document.getElementById('detail-available').textContent = parking.available;
        document.getElementById('detail-rating').textContent = generateStars(parking.rating) + ' ' + parking.rating;
        showPage('parking-details-page');
    }
}

// Show first page on load
window.addEventListener('load', () => {
    showPage('signin-page');
    pageHistory = ['signin-page'];
});
