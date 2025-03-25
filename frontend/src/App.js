import React from 'react';

import {BrowserRouter as Router, Routes, Route} from "react-router-dom";

import Header from './components/Header';
import Footer from './components/Footer';

import Home from './page/Home';
import Contacts from './page/Contacts';
import Halls from './page/Halls';
import HallDetails from "./page/HallDetails";
import ScrollToTop from "./utils/scrollToTop";


function App() {
  return (
    <div className="App">
        <Router>
            <ScrollToTop />
            <Header />
            <Routes>

                <Route path="/" element={<Home />} />
                <Route path="/halls" element={<Halls />} />
                <Route path="/hall/:id" element={<HallDetails />} />
                <Route path="/contacts" element={<Contacts />} />
            </Routes>
            <Footer />
        </Router>

    </div>
  );
}

export default App;
