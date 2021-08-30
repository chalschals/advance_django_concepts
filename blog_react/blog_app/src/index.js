import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom'
import Header from './components/Header'
import Register from './components/Register'
import Footer from './components/Footer'
import Login from './components/Login'
import Logout from './components/Logout'
ReactDOM.render(
  <Router>
    <React.StrictMode>
      <Header />
      <Switch>
        <Route exact path="/" component={App} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/logout" component={Logout} />
      </Switch>
      <Footer />
    </React.StrictMode>
  </Router>
  ,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
