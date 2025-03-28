import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import { styled } from '@mui/material/styles';
import Home from './pages/Home';
import Category from './pages/Category';
import Recipe from './pages/Recipe';
import Footer from './components/Footer';
import Categories from './pages/Categories';
import About from './pages/About';
import Contact from './pages/Contact';

const theme = createTheme({
  palette: {
    primary: {
      main: '#FFD700', // Золотой
      light: '#FFE44D',
      dark: '#B39D00',
    },
    secondary: {
      main: '#FFA000', // Оранжевый
      light: '#FFD149',
      dark: '#C67100',
    },
    background: {
      default: '#1A1A1A', // Темный фон
      paper: '#2D2D2D', // Чуть светлее для карточек
    },
    text: {
      primary: '#FFFFFF',
      secondary: '#B0B0B0',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h1: {
      fontSize: '2.5rem',
      fontWeight: 700,
    },
    h4: {
      fontWeight: 600,
    },
  },
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          transition: 'transform 0.2s ease-in-out',
          '&:hover': {
            transform: 'translateY(-4px)',
          },
        },
      },
    },
  },
});

const StyledAppBar = styled('header')(({ theme }) => ({
  background: theme.palette.background.paper,
  color: theme.palette.text.primary,
  padding: '1rem',
  textAlign: 'center',
  boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
  borderBottom: `1px solid ${theme.palette.primary.main}`,
}));

const AppTitle = styled('h1')(({ theme }) => ({
  margin: 0,
  fontSize: '2rem',
  fontWeight: 700,
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  gap: '0.5rem',
  color: theme.palette.primary.main,
}));

const AppSubtitle = styled('p')(({ theme }) => ({
  margin: '0.5rem 0 0',
  fontSize: '1rem',
  color: theme.palette.text.secondary,
  fontWeight: 500,
}));

const HeartIcon = styled('span')(({ theme }) => ({
  color: theme.palette.primary.main,
  fontSize: '2.5rem',
  animation: 'pulse 1.5s infinite',
  '@keyframes pulse': {
    '0%': {
      transform: 'scale(1)',
    },
    '50%': {
      transform: 'scale(1.1)',
    },
    '100%': {
      transform: 'scale(1)',
    },
  },
}));

const AppContainer = styled('div')({
  minHeight: '100vh',
  display: 'flex',
  flexDirection: 'column',
});

const MainContent = styled('main')({
  flex: 1,
  padding: '2rem 0',
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <AppContainer>
          <MainContent>
            <StyledAppBar>
              <AppTitle>
                i <HeartIcon>❤</HeartIcon> food
              </AppTitle>
            </StyledAppBar>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/categories" element={<Categories />} />
              <Route path="/category/:slug" element={<Category />} />
              <Route path="/recipe/:slug" element={<Recipe />} />
              <Route path="/about" element={<About />} />
              <Route path="/contact" element={<Contact />} />
            </Routes>
          </MainContent>
          <Footer />
        </AppContainer>
      </Router>
    </ThemeProvider>
  );
}

export default App;
