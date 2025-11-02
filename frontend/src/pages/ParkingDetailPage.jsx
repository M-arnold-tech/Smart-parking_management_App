import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import {
  Container,
  Box,
  Typography,
  Button,
  Rating,
  Divider,
  IconButton,
  Chip,
  Paper,
} from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import LocalParkingIcon from '@mui/icons-material/LocalParking';
import Navbar from '../components/Navbar';
import BottomNav from '../components/BottomNav';

const parkingDetails = {
  id: 1,
  name: 'Downtown Parking',
  address: '123 Main St, City Center',
  distance: 1.2,
  rating: 4.5,
  totalReviews: 128,
  price: 5.0,
  availableSpots: 12,
  totalSpots: 50,
  openHours: '24/7',
  features: ['Covered', 'Security', 'EV Charging', 'Valet'],
  image: 'https://images.unsplash.com/photo-1600705725956-001c42d9edf0?w=800&h=400&fit=crop',
  description:
    'Secure parking facility with 24/7 surveillance and easy access to downtown attractions. Our parking lot offers both covered and uncovered spots with electric vehicle charging stations available.',
};

const ParkingDetailPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  return (
    <Box sx={{ pb: 7 }}>
      <Box sx={{ position: 'relative', height: 200, mb: 2 }}>
        <img
          src={parkingDetails.image}
          alt={parkingDetails.name}
          style={{ width: '100%', height: '100%', objectFit: 'cover' }}
        />
        <IconButton
          sx={{ position: 'absolute', top: 16, left: 16, bgcolor: 'rgba(255,255,255,0.8)' }}
          onClick={() => navigate(-1)}
        >
          <ArrowBackIcon />
        </IconButton>
      </Box>

      <Container maxWidth="sm" sx={{ py: 2 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
          <Box>
            <Typography variant="h5" fontWeight="bold" gutterBottom>
              {parkingDetails.name}
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
              <LocationOnIcon color="action" fontSize="small" />
              <Typography variant="body2" color="text.secondary" sx={{ ml: 0.5 }}>
                {parkingDetails.address} • {parkingDetails.distance} km away
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <Rating value={parkingDetails.rating} precision={0.5} readOnly size="small" />
              <Typography variant="body2" color="text.secondary" sx={{ ml: 1 }}>
                {parkingDetails.rating} ({parkingDetails.totalReviews} reviews)
              </Typography>
            </Box>
          </Box>
          <Chip
            label={`${parkingDetails.availableSpots} spots left`}
            color="primary"
            variant="outlined"
            size="small"
          />
        </Box>

        <Divider sx={{ my: 2 }} />

        <Box sx={{ mb: 3 }}>
          <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
            Features
          </Typography>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1, mb: 2 }}>
            {parkingDetails.features.map((feature, index) => (
              <Chip key={index} label={feature} size="small" />
            ))}
          </Box>
        </Box>

        <Box sx={{ mb: 3 }}>
          <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
            Opening Hours
          </Typography>
          <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
            <AccessTimeIcon color="action" fontSize="small" sx={{ mr: 1 }} />
            <Typography>{parkingDetails.openHours}</Typography>
          </Box>
        </Box>

        <Box sx={{ mb: 3 }}>
          <Typography variant="subtitle1" fontWeight="bold" gutterBottom>
            Description
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {parkingDetails.description}
          </Typography>
        </Box>

        <Paper
          elevation={3}
          sx={{
            position: 'fixed',
            bottom: 56,
            left: 0,
            right: 0,
            p: 2,
            zIndex: 1,
            borderRadius: 0,
            borderTopLeftRadius: 16,
            borderTopRightRadius: 16,
          }}
        >
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <Box>
              <Typography variant="body2" color="text.secondary">
                Price per hour
              </Typography>
              <Typography variant="h6" color="primary" fontWeight="bold">
                ${parkingDetails.price}/h
              </Typography>
            </Box>
            <Button 
              variant="contained" 
              size="large" 
              startIcon={<LocalParkingIcon />}
              sx={{ borderRadius: 2, textTransform: 'none' }}
            >
              Book Parking
            </Button>
          </Box>
        </Paper>
      </Container>

      <BottomNav />
    </Box>
  );
};

export default ParkingDetailPage;