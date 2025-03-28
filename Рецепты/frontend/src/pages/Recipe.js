import React, { useState, useEffect } from 'react';
import { useParams, Link as RouterLink } from 'react-router-dom';
import { 
  Container, 
  Typography, 
  Paper, 
  Grid, 
  Breadcrumbs, 
  Link, 
  CircularProgress, 
  Alert,
  Box,
  useTheme,
  Chip
} from '@mui/material';
import axios from 'axios';

function Recipe() {
  const { slug } = useParams();
  const [recipe, setRecipe] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const theme = useTheme();

  useEffect(() => {
    const fetchRecipe = async () => {
      try {
        setLoading(true);
        setError(null);
        console.log('Fetching recipe with slug:', slug);
        const response = await axios.get(`http://localhost:8000/api/recipes/`);
        console.log('API response:', response.data);
        
        // Проверяем структуру ответа
        const recipes = Array.isArray(response.data) ? response.data : 
                       (response.data.results ? response.data.results : []);
        
        // Ищем рецепт по slug среди всех рецептов
        const recipeData = recipes.find(recipe => recipe.slug === slug);

        if (recipeData) {
          console.log('Found recipe:', recipeData);
          setRecipe(recipeData);
        } else {
          setError('Рецепт не найден');
        }
      } catch (error) {
        console.error('Error fetching recipe:', error);
        setError('Ошибка при загрузке рецепта');
      } finally {
        setLoading(false);
      }
    };

    if (slug) {
      fetchRecipe();
    }
  }, [slug]);

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

  if (!recipe) {
    return (
      <Container sx={{ mt: 4 }}>
        <Alert severity="warning">Рецепт не найден</Alert>
      </Container>
    );
  }

  return (
    <Container sx={{ mt: 4 }}>
      <Breadcrumbs sx={{ mb: 4 }}>
        <Link component={RouterLink} to="/" color="inherit">
          Главная
        </Link>
        {recipe.category && (
          <Link component={RouterLink} to={`/category/${recipe.category.slug}`} color="inherit">
            {recipe.category.name}
          </Link>
        )}
        <Typography color="text.primary">{recipe.title}</Typography>
      </Breadcrumbs>

      <Paper 
        sx={{ 
          p: 4,
          background: `linear-gradient(45deg, ${theme.palette.background.paper} 30%, ${theme.palette.background.default} 90%)`,
          border: `1px solid ${theme.palette.primary.main}`,
          boxShadow: `0 4px 20px rgba(0,0,0,0.2)`
        }}
      >
        <Box 
          sx={{ 
            textAlign: 'center', 
            mb: 4,
            position: 'relative',
            height: '300px',
            overflow: 'hidden',
            borderRadius: '8px',
            '&::before': {
              content: '""',
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              backgroundImage: `url(${recipe.image_url || `https://source.unsplash.com/800x400/?${recipe.title}`})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              filter: 'brightness(0.7)',
            },
            '&::after': {
              content: '""',
              position: 'absolute',
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              background: 'linear-gradient(45deg, rgba(0,0,0,0.5), rgba(0,0,0,0.2))',
            }
          }}
        >
          <Box sx={{ position: 'relative', zIndex: 1, height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <Typography 
              variant="h3" 
              component="h1" 
              gutterBottom 
              sx={{ 
                fontWeight: 700,
                color: theme.palette.text.primary,
                mb: 2,
                textShadow: '2px 2px 4px rgba(0,0,0,0.5)'
              }}
            >
              {recipe.title}
            </Typography>
            <Box sx={{ display: 'flex', gap: 2, justifyContent: 'center', mb: 3 }}>
              <Chip 
                icon={<span>⏱</span>} 
                label={`${recipe.cooking_time} минут`}
                color="primary"
                variant="outlined"
                sx={{
                  borderColor: theme.palette.primary.main,
                  color: theme.palette.primary.main,
                  '& .MuiChip-icon': {
                    color: theme.palette.primary.main
                  }
                }}
              />
              <Chip 
                icon={<span>👥</span>} 
                label={`${recipe.servings} порций`}
                color="primary"
                variant="outlined"
                sx={{
                  borderColor: theme.palette.primary.main,
                  color: theme.palette.primary.main,
                  '& .MuiChip-icon': {
                    color: theme.palette.primary.main
                  }
                }}
              />
            </Box>
            <Typography 
              variant="h6" 
              color="text.primary" 
              sx={{ 
                maxWidth: '800px', 
                mx: 'auto',
                textShadow: '1px 1px 2px rgba(0,0,0,0.5)'
              }}
            >
              {recipe.description}
            </Typography>
          </Box>
        </Box>

        <Grid container spacing={4}>
          <Grid xs={12} md={6}>
            <Paper 
              elevation={2} 
              sx={{ 
                p: 3,
                height: '100%',
                background: theme.palette.background.paper,
                border: `1px solid ${theme.palette.primary.main}`,
                boxShadow: `0 4px 20px rgba(0,0,0,0.2)`
              }}
            >
              <Typography 
                variant="h5" 
                gutterBottom 
                sx={{ 
                  fontWeight: 600,
                  color: theme.palette.primary.main,
                  mb: 3
                }}
              >
                Ингредиенты
              </Typography>
              <Typography 
                variant="body1" 
                sx={{ 
                  whiteSpace: 'pre-line',
                  lineHeight: 2,
                  color: theme.palette.text.primary
                }}
              >
                {recipe.ingredients}
              </Typography>
            </Paper>
          </Grid>
          <Grid xs={12} md={6}>
            <Paper 
              elevation={2} 
              sx={{ 
                p: 3,
                height: '100%',
                background: theme.palette.background.paper,
                border: `1px solid ${theme.palette.primary.main}`,
                boxShadow: `0 4px 20px rgba(0,0,0,0.2)`
              }}
            >
              <Typography 
                variant="h5" 
                gutterBottom 
                sx={{ 
                  fontWeight: 600,
                  color: theme.palette.primary.main,
                  mb: 3
                }}
              >
                Инструкция по приготовлению
              </Typography>
              <Typography 
                variant="body1" 
                sx={{ 
                  whiteSpace: 'pre-line',
                  lineHeight: 2,
                  color: theme.palette.text.primary
                }}
              >
                {recipe.instructions}
              </Typography>
            </Paper>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
}

export default Recipe; 