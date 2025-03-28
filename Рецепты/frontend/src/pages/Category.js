import React, { useState, useEffect } from 'react';
import { useParams, Link as RouterLink } from 'react-router-dom';
import { 
  Container, 
  Grid, 
  Card, 
  CardContent, 
  Typography, 
  CardActionArea, 
  CardMedia,
  Breadcrumbs, 
  Link, 
  CircularProgress, 
  Alert,
  Box,
  useTheme
} from '@mui/material';
import axios from 'axios';

function Category() {
  const { slug } = useParams();
  const [category, setCategory] = useState(null);
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const theme = useTheme();

  useEffect(() => {
    const fetchCategoryAndRecipes = async () => {
      try {
        setLoading(true);
        setError(null);
        console.log('Fetching category and recipes for slug:', slug);
        
        // Получаем категорию
        const categoryResponse = await axios.get(`http://localhost:8000/api/categories/?slug=${slug}`);
        console.log('Category response:', categoryResponse.data);
        
        // Находим категорию по slug
        const categoryData = categoryResponse.data.results.find(cat => cat.slug === slug);
        
        if (!categoryData) {
          console.error('Category not found for slug:', slug);
          setError('Категория не найдена');
          return;
        }

        setCategory(categoryData);
        console.log('Found category:', categoryData);
        
        // Получаем рецепты для этой категории
        const recipesResponse = await axios.get(`http://localhost:8000/api/recipes/`);
        console.log('All recipes response:', recipesResponse.data);
        
        // Фильтруем рецепты по slug категории
        const recipesData = recipesResponse.data.results.filter(recipe => {
          console.log('Comparing recipe:', recipe.title, 'category:', recipe.category);
          return recipe.category === categoryData.id || 
                 (recipe.category && recipe.category.id === categoryData.id);
        });
        
        console.log('Filtered recipes for category:', recipesData);
        setRecipes(recipesData);
      } catch (error) {
        console.error('Error fetching category and recipes:', error);
        console.error('Error details:', error.response?.data || error.message);
        setError('Ошибка при загрузке данных');
      } finally {
        setLoading(false);
      }
    };

    fetchCategoryAndRecipes();
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

  if (!category) {
    return (
      <Container sx={{ mt: 4 }}>
        <Alert severity="warning">Категория не найдена</Alert>
      </Container>
    );
  }

  return (
    <Container sx={{ mt: 4 }}>
      <Breadcrumbs sx={{ mb: 4 }}>
        <Link component={RouterLink} to="/" color="inherit">
          Главная
        </Link>
        <Typography color="text.primary">{category.name}</Typography>
      </Breadcrumbs>

      <Box sx={{ textAlign: 'center', mb: 6 }}>
        <Typography 
          variant="h3" 
          component="h1" 
          gutterBottom 
          sx={{ 
            fontWeight: 700,
            color: theme.palette.primary.main,
            mb: 2
          }}
        >
          {category.name}
        </Typography>
        <Typography 
          variant="h6" 
          color="text.secondary" 
          sx={{ maxWidth: '600px', mx: 'auto' }}
        >
          {category.description}
        </Typography>
      </Box>

      <Grid container spacing={4}>
        {recipes.length > 0 ? (
          recipes.map((recipe) => (
            <Grid item key={recipe.id} xs={12} sm={6} md={4}>
              <Card 
                sx={{ 
                  height: '100%',
                  display: 'flex',
                  flexDirection: 'column',
                  borderRadius: '16px',
                  overflow: 'hidden',
                  transition: 'all 0.3s ease-in-out',
                  '&:hover': {
                    transform: 'translateY(-8px)',
                    boxShadow: 6
                  }
                }}
              >
                <CardActionArea 
                  component={RouterLink} 
                  to={`/recipe/${recipe.slug}`}
                  sx={{ flexGrow: 1, display: 'flex', flexDirection: 'column' }}
                >
                  <CardMedia
                    component="img"
                    height="200"
                    image={recipe.image_url || `https://source.unsplash.com/400x300/?${encodeURIComponent(recipe.title.toLowerCase())},food`}
                    alt={recipe.title}
                    sx={{
                      objectFit: 'cover',
                      objectPosition: 'center'
                    }}
                  />
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography 
                      variant="h6" 
                      component="h2" 
                      gutterBottom
                      sx={{ 
                        fontWeight: 600,
                        color: theme.palette.text.primary
                      }}
                    >
                      {recipe.title}
                    </Typography>
                    <Typography 
                      variant="body2" 
                      color="text.secondary"
                      sx={{
                        display: '-webkit-box',
                        WebkitLineClamp: 3,
                        WebkitBoxOrient: 'vertical',
                        overflow: 'hidden',
                        mb: 2
                      }}
                    >
                      {recipe.description}
                    </Typography>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <Typography variant="body2" color="text.secondary">
                        {recipe.cooking_time} мин
                      </Typography>
                      <Typography variant="body2" color="text.secondary">
                        {recipe.servings} порц.
                      </Typography>
                    </Box>
                  </CardContent>
                </CardActionArea>
              </Card>
            </Grid>
          ))
        ) : (
          <Grid item xs={12}>
            <Alert severity="info" sx={{ mt: 2 }}>
              В этой категории пока нет рецептов
            </Alert>
          </Grid>
        )}
      </Grid>
    </Container>
  );
}

export default Category; 