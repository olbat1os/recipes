import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Container, Grid, Card, CardContent, Typography, Box } from '@mui/material';

const Categories = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/categories/');
        const data = await response.json();
        setCategories(data);
      } catch (error) {
        console.error('Ошибка при загрузке категорий:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  if (loading) {
    return (
      <Container>
        <Typography variant="h4" align="center" sx={{ mt: 4 }}>
          Загрузка...
        </Typography>
      </Container>
    );
  }

  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          Категории рецептов
        </Typography>
        <Grid container spacing={3}>
          {categories.map((category) => (
            <Grid item xs={12} sm={6} md={4} key={category.id}>
              <Link to={`/category/${category.slug}`} style={{ textDecoration: 'none' }}>
                <Card 
                  sx={{ 
                    height: '100%',
                    cursor: 'pointer',
                    transition: 'transform 0.2s ease-in-out',
                    '&:hover': {
                      transform: 'translateY(-5px)'
                    }
                  }}
                >
                  <CardContent>
                    <Typography variant="h5" component="h2" gutterBottom>
                      {category.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      {category.description}
                    </Typography>
                  </CardContent>
                </Card>
              </Link>
            </Grid>
          ))}
        </Grid>
      </Box>
    </Container>
  );
};

export default Categories; 