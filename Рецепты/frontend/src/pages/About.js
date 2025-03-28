import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';

const About = () => {
  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Typography variant="h3" component="h1" gutterBottom align="center">
          О нас
        </Typography>
        <Paper sx={{ p: 4, mt: 4 }}>
          <Typography variant="h5" gutterBottom>
            Добро пожаловать на наш кулинарный сайт!
          </Typography>
          <Typography paragraph>
            Мы создали этот проект для всех, кто любит готовить и хочет открыть для себя новые рецепты. 
            На нашем сайте вы найдете множество интересных рецептов, которые помогут вам разнообразить 
            ваше меню и порадовать близких вкусными блюдами.
          </Typography>
          <Typography paragraph>
            Наша миссия - сделать приготовление пищи доступным и увлекательным для каждого. 
            Мы тщательно отбираем рецепты, чтобы они были не только вкусными, но и простыми в приготовлении.
          </Typography>
          <Typography paragraph>
            Мы постоянно работаем над улучшением нашего сайта и добавлением новых рецептов. 
            Если у вас есть предложения или вопросы, мы всегда рады обратной связи!
          </Typography>
        </Paper>
      </Box>
    </Container>
  );
};

export default About; 