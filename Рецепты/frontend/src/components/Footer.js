import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-left">
          <div className="footer-logo">
            <span className="heart-icon">❤</span>
            <span className="logo-text">i love food</span>
          </div>
          <div className="footer-links">
            <Link to="/">Главная</Link>
            <Link to="/categories">Категории</Link>
            <Link to="/about">О нас</Link>
            <Link to="/contact">Контакты</Link>
          </div>
        </div>
        
        <div className="footer-right">
          <div className="social-links">
            <a href="https://vk.com" target="_blank" rel="noopener noreferrer">
              <span className="social-icon">VK</span>
            </a>
            <a href="https://telegram.org" target="_blank" rel="noopener noreferrer">
              <span className="social-icon">TG</span>
            </a>
            <a href="https://youtube.com" target="_blank" rel="noopener noreferrer">
              <span className="social-icon">YT</span>
            </a>
          </div>
          <div className="footer-copyright">
            © 2024 i love food
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 