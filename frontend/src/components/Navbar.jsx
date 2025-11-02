import React from 'react';
import { AppBar, Toolbar, Typography, IconButton, Box } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';

const Navbar = ({ title }) => {
  return (
    <AppBar position="static" color="default" elevation={1} sx={{ bgcolor: 'white' }}>
      <Toolbar>
        <IconButton edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
          <MenuIcon />
        </IconButton>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1, fontWeight: 'bold' }}>
          {title || 'Smart Parking'}
        </Typography>
        <IconButton color="inherit">
          <NotificationsNoneIcon />
        </IconButton>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;