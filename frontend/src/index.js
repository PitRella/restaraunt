import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/main.css';

import './scss/main.scss';
import './scss/base/_base.scss';
import './scss/base/_vars.scss';
import './scss/base/_reset.scss';

import './scss/blocks/_accomplishments.scss';
import './scss/blocks/_contacts.scss';
import './scss/blocks/_discount.scss';
import './scss/blocks/_era.scss';
import './scss/blocks/_footer.scss';
import './scss/blocks/_halls.scss';
import './scss/blocks/_header.scss';
import './scss/blocks/_reviews.scss';
import './scss/blocks/_social.scss';

import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>

    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
