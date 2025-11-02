import React from 'react';
import { Card, CardContent, CardMedia, Typography, Box, Rating, Button } from '@mui/material';
import LocationOnIcon from '@mui/icons-material/LocationOn';

const ParkingCard = ({ parking }) => {
  return (
    <Card sx={{ display: 'flex', mb: 2, borderRadius: 2, boxShadow: 3 }}>
      <CardMedia
        component="img"
        sx={{ width: 120, height: 120, objectFit: 'cover' }}
        image={parking.image}
        alt={parking.name}
      />
      <CardContent sx={{ flex: 1, p: 2, display: 'flex', flexDirection: 'column' }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <Box>
            <Typography variant="subtitle1" fontWeight="bold" noWrap>
              {parking.name}
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'center', mt: 0.5, mb: 1 }}>
              <LocationOnIcon color="action" fontSize="small" />
              <Typography variant="body2" color="text.secondary" sx={{ ml: 0.5 }}>
                {parking.distance} km
              </Typography>
            </Box>
            <Rating value={parking.rating} size="small" readOnly />
          </Box>
          <Typography variant="h6" color="primary" fontWeight="bold">
            ${parking.price}/h
          </Typography>
        </Box>
        <Box sx={{ mt: 'auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Typography variant="body2" color="text.secondary">
            {parking.availableSpots} spots left
          </Typography>
          <Button variant="contained" size="small" sx={{ borderRadius: 2, textTransform: 'none' }}>
            Book Now
          </Button>
        </Box>
      </CardContent>
    </Card>
  );
};

export default ParkingCard;