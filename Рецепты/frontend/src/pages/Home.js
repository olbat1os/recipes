import React, { useState, useEffect } from 'react';
import { Link as RouterLink } from 'react-router-dom';
import { 
  Container, 
  Grid,
  Typography, 
  CardActionArea,
  CardMedia,
  Box,
  CircularProgress,
  Alert,
  useTheme,
  TextField,
  InputAdornment,
  Paper,
  Card
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import axios from 'axios';

function Home() {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const theme = useTheme();

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        setLoading(true);
        const response = await axios.get('http://localhost:8000/api/categories/');
        console.log('API Response:', response.data);
        const categoriesData = response.data.results || [];
        console.log('Processed Categories:', categoriesData);
        setCategories(categoriesData);
      } catch (error) {
        console.error('Error fetching categories:', error);
        setError('Ошибка при загрузке категорий');
      } finally {
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  const filteredCategories = categories.filter(category =>
    category.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    category.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  console.log('Filtered Categories:', filteredCategories);
  console.log('Categories structure:', JSON.stringify(filteredCategories, null, 2));

  if (loading) {
    return (
      <Container sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Container>
    );
  }

  if (error) {
    return (
      <Container sx={{ mt: 4 }}>
        <Alert severity="error">{error}</Alert>
      </Container>
    );
  }

  return (
    <Box sx={{ minHeight: '100vh', pb: 6 }}>
      {/* Приветственный баннер */}
      <Box
        sx={{
          background: `linear-gradient(45deg, ${theme.palette.primary.dark} 30%, ${theme.palette.secondary.dark} 90%)`,
          color: 'white',
          py: 8,
          mb: 6,
          position: 'relative',
          overflow: 'hidden',
          '&::before': {
            content: '""',
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: 'url(https://source.unsplash.com/1600x900/?food,cooking)',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            opacity: 0.2,
          }
        }}
      >
        <Container>
          <Typography 
            variant="h2" 
            component="h1" 
            sx={{ 
              fontWeight: 700,
              textAlign: 'center',
              mb: 2,
              textShadow: '2px 2px 4px rgba(0,0,0,0.3)'
            }}
          >
            Кулинарное путешествие
          </Typography>
          <Typography 
            variant="h5" 
            sx={{ 
              textAlign: 'center',
              maxWidth: 800,
              mx: 'auto',
              opacity: 0.9,
              textShadow: '1px 1px 2px rgba(0,0,0,0.2)'
            }}
          >
            Откройте для себя мир вкусных рецептов и начните готовить с удовольствием
          </Typography>
        </Container>
      </Box>

      <Container>
        {/* Поле поиска */}
        <Paper 
          elevation={3}
          sx={{ 
            p: 3,
            mb: 6,
            borderRadius: '16px',
            background: `linear-gradient(45deg, ${theme.palette.background.paper} 30%, ${theme.palette.background.default} 90%)`
          }}
        >
          <TextField
            fullWidth
            variant="outlined"
            placeholder="Поиск категорий..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            sx={{
              '& .MuiOutlinedInput-root': {
                backgroundColor: theme.palette.background.paper,
                borderRadius: '12px',
                '& fieldset': {
                  borderColor: theme.palette.primary.main,
                  borderWidth: '2px',
                },
                '&:hover fieldset': {
                  borderColor: theme.palette.primary.light,
                },
                '&.Mui-focused fieldset': {
                  borderColor: theme.palette.primary.main,
                },
                color: theme.palette.text.primary,
              }
            }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon sx={{ color: theme.palette.primary.main }} />
                </InputAdornment>
              ),
            }}
          />
        </Paper>

        {/* Сетка категорий */}
        <Grid container spacing={4}>
          {filteredCategories.map((category) => (
            <Grid item xs={12} sm={6} md={4} key={category.id}>
              <Card 
                sx={{ 
                  height: '280px',
                  position: 'relative',
                  borderRadius: '20px',
                  overflow: 'hidden',
                  transition: 'all 0.3s ease-in-out',
                  '&:hover': {
                    transform: 'translateY(-8px) scale(1.02)',
                    boxShadow: (theme) => `0 14px 28px rgba(0, 0, 0, 0.2)`,
                  }
                }}
              >
                <CardActionArea 
                  component={RouterLink} 
                  to={`/category/${category.slug}`}
                  sx={{ height: '100%', position: 'relative' }}
                >
                  <CardMedia
                    component="img"
                    height="280"
                    image={category.image_url || `https://source.unsplash.com/400x300/?${encodeURIComponent(category.name.toLowerCase())},food`}
                    alt={category.name}
                    sx={{
                      height: '100%',
                      objectFit: 'cover',
                      objectPosition: 'center',
                    }}
                  />
                  <Box
                    sx={{
                      position: 'absolute',
                      bottom: 0,
                      left: 0,
                      right: 0,
                      background: 'linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2))',
                      padding: 3,
                      transition: 'all 0.3s ease-in-out',
                    }}
                  >
                    <Typography 
                      variant="h5"
                      sx={{
                        color: 'white',
                        fontWeight: 700,
                        textShadow: '2px 2px 4px rgba(0,0,0,0.5)',
                        mb: 1
                      }}
                    >
                      {category.name}
                    </Typography>
                    <Typography
                      variant="body2"
                      sx={{
                        color: 'rgba(255,255,255,0.8)',
                        textShadow: '1px 1px 2px rgba(0,0,0,0.5)',
                        display: '-webkit-box',
                        WebkitLineClamp: 2,
                        WebkitBoxOrient: 'vertical',
                        overflow: 'hidden'
                      }}
                    >
                      {category.description}
                    </Typography>
                  </Box>
                </CardActionArea>
              </Card>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
}

export default Home; 