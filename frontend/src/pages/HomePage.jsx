import React, { useState } from 'react';
import { Container, Typography, Box } from '@mui/material';
import Navbar from '../components/Navbar';
import SearchBar from '../components/SearchBar';
import ParkingCard from '../components/ParkingCard';
import BottomNav from '../components/BottomNav';

const mockParkings = [
  {
    id: 1,
    name: 'Downtown Parking',
    distance: 1.2,
    rating: 4.5,
    price: 5.0,
    availableSpots: 12,
    image: 'https://images.unsplash.com/photo-1600705725956-001c42d9edf0?w=300&h=300&fit=crop',
  },
  {
    id: 2,
    name: 'City Center Parking',
    distance: 0.8,
    rating: 4.2,
    price: 6.5,
    availableSpots: 5,
    image: 'https://images.unsplash.com/photo-1600705725956-001c42d9edf0?w=300&h=300&fit=crop',
  },
  {
    id: 3,
    name: 'Mall Parking',
    distance: 2.1,
    rating: 4.0,
    price: 4.5,
    availableSpots: 8,
    image: 'https://images.unsplash.com/photo-1600705725956-001c42d9edf0?w=300&h=300&fit=crop',
  },
];

const HomePage = () => {
  const [searchTerm, setSearchTerm] = useState('');

  return (
    <Box sx={{ pb: 10 }}>
      <Navbar title="Find Parking" />
      <Container maxWidth="sm" sx={{ py: 2 }}>
        <SearchBar />
        <Typography variant="h6" sx={{ mb: 2, fontWeight: 'bold' }}>
          Nearby Parking
        </Typography>
        {mockParkings.map((parking) => (
          <ParkingCard key={parking.id} parking={parking} />
        ))}
      </Container>
      <BottomNav />
    </Box>
  );
};

export default HomePage;