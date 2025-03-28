import React from 'react';
import { Link } from 'react-router-dom';
import { AppBar, Toolbar, Button, Box } from '@mui/material';
import { styled } from '@mui/material/styles';

const StyledAppBar = styled(AppBar)(({ theme }) => ({
  background: 'transparent',
  boxShadow: 'none',
  borderBottom: `1px solid ${theme.palette.primary.main}`,
}));

const NavButton = styled(Button)(({ theme }) => ({
  color: theme.palette.text.primary,
  margin: '0 8px',
  '&:hover': {
    color: theme.palette.primary.main,
  },
}));

const Navbar = () => {
  return (
    <StyledAppBar position="static">
      <Toolbar>
        <Box sx={{ flexGrow: 1, display: 'flex', justifyContent: 'center' }}>
          <Link to="/" style={{ textDecoration: 'none' }}>
            <NavButton>Главная</NavButton>
          </Link>
          <Link to="/categories" style={{ textDecoration: 'none' }}>
            <NavButton>Категории</NavButton>
          </Link>
          <Link to="/about" style={{ textDecoration: 'none' }}>
            <NavButton>О нас</NavButton>
          </Link>
          <Link to="/contact" style={{ textDecoration: 'none' }}>
            <NavButton>Контакты</NavButton>
          </Link>
        </Box>
      </Toolbar>
    </StyledAppBar>
  );
};

export default Navbar; 