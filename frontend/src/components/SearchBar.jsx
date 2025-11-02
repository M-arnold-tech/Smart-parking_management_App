import React from 'react';
import { Paper, InputBase, IconButton } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import TuneIcon from '@mui/icons-material/Tune';

const SearchBar = () => {
  return (
    <Paper
      component="form"
      sx={{
        p: '2px 4px',
        display: 'flex',
        alignItems: 'center',
        width: '100%',
        mb: 2,
        borderRadius: 2,
        boxShadow: 2,
      }}
    >
      <IconButton sx={{ p: '10px' }} aria-label="search">
        <SearchIcon />
      </IconButton>
      <InputBase
        sx={{ ml: 1, flex: 1 }}
        placeholder="Search parking location"
        inputProps={{ 'aria-label': 'search parking location' }}
      />
      <IconButton type="submit" sx={{ p: '10px' }} aria-label="filter">
        <TuneIcon />
      </IconButton>
    </Paper>
  );
};

export default SearchBar;