import React from 'react';
import logo from "./../img/main-page/header/logo.png";
import cityIcon from "./../img/main-page/header/city.svg";
import emailIcon from "./../img/main-page/header/email.svg";
import phoneIcon from "./../img/main-page/header/phone.svg";

import {NavLink} from 'react-router-dom';

function Header() {
    return (
        <header className="header">
            <div className="header-container">
                <div className="head">
                    <NavLink to="/">
                    <div className="logo">
                        <img src={logo} alt="logo" />
                    </div>
                    </NavLink>

                    <div className="info">
                        <img src={cityIcon} alt="city icon" />
                        <div className="text">Місто Харків</div>
                    </div>
                    <div className="info">
                        <img src={emailIcon} alt="email icon" />
                        <div className="text">pastplates@gmail.com</div>
                    </div>
                    <a className="button-accent" href="../../../restaraunt/frontend/public/index.html">Забронювати столик</a>
                    <div className="info info-hours">
                        <p className="text">
                            Пн-Пт: 09:00 - 23:00<br />
                            Сб-Нд: 12:00 - 23:00<br />
                        </p>
                        <div className="info">
                            <img className="info-hours__img" src={phoneIcon} alt="phone icon" />
                            <div className="text">+38 099 634 46 71</div>
                        </div>
                    </div>
                </div>

                <nav className="nav">
                    <ul className="nav-list">
                        <li className="nav-list__item">
                            <NavLink to="/" className="nav-list__link">
                                Головна
                            </NavLink>
                        </li>
                        <li className="nav-list__item">
                            <NavLink to="/menu" className="nav-list__link">
                            Меню
                            </NavLink>
                        </li>
                        <li className="nav-list__item">
                            <NavLink to="/delivery" className="nav-list__link">
                                Доставка
                            </NavLink>
                        </li>
                        <li className="nav-list__item">
                            <NavLink to="/halls" className="nav-list__link">
                                Наші зали
                            </NavLink>
                        </li>
                        <li className="nav-list__item">
                            <NavLink to="/contacts" className="nav-list__link">
                                Контакти
                            </NavLink>
                        </li>
                        <li className="nav-list__item">
                            <NavLink to="/login" className="nav-list__link">
                                Вхід/Реєстрація
                            </NavLink>
                        </li>
                    </ul>
                </nav>
            </div>
        </header>
    );
}

export default Header;
