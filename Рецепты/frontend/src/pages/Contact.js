import React from 'react';
import { Container, Typography, Box, Paper, Grid } from '@mui/material';

const Contact = () => {
  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          Контакты
        </Typography>
        <Paper sx={{ p: 4, mt: 4 }}>
          <Grid container spacing={4}>
            <Grid item xs={12} md={6}>
              <Typography variant="h5" gutterBottom>
                Свяжитесь с нами
              </Typography>
              <Typography paragraph>
                Если у вас есть вопросы, предложения или вы хотите поделиться своим рецептом, 
                мы всегда рады общению!
              </Typography>
              <Typography variant="h6" gutterBottom sx={{ mt: 3 }}>
                Наши контакты:
              </Typography>
              <Typography paragraph>
                Email: info@recipes.com
              </Typography>
              <Typography paragraph>
                Телефон: +7 (999) 123-45-67
              </Typography>
              <Typography paragraph>
                Адрес: г. Москва, ул. Кулинарная, 1
              </Typography>
            </Grid>
            <Grid item xs={12} md={6}>
              <Typography variant="h5" gutterBottom>
                Социальные сети
              </Typography>
              <Typography paragraph>
                Следите за нашими обновлениями в социальных сетях:
              </Typography>
              <Box sx={{ mt: 2 }}>
                <Typography component="a" href="https://vk.com" target="_blank" rel="noopener noreferrer" sx={{ mr: 2 }}>
                  ВКонтакте
                </Typography>
                <Typography component="a" href="https://telegram.org" target="_blank" rel="noopener noreferrer" sx={{ mr: 2 }}>
                  Telegram
                </Typography>
                <Typography component="a" href="https://youtube.com" target="_blank" rel="noopener noreferrer">
                  YouTube
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Paper>
      </Box>
    </Container>
  );
};

export default Contact; 