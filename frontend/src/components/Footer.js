import React from 'react';
import logoWhite from "./../img/main-page/header/logo-white.svg";
import cityWhite from "./../img/main-page/header/city-white.svg";
import hours from "./../img/main-page/header/hours.svg";
import emailWhite from "./../img/main-page/header/email-white.svg";
import phoneWhite from "./../img/main-page/header/phone-white.svg";
import {Link} from "react-router-dom";


function Footer() {
    return (
        <footer className="footer">
            <div className="container-footer">
                <div className="container-footer__column">
                    <div className="container-footer__column-item">
                        <img src={logoWhite} className="logo" alt="Логотип" />
                        <div className="footer-item">
                            <img src={cityWhite} alt="Город" />
                            <p className="footer-text">Харківська область, м. Буди, Квіткова 7.</p>
                        </div>
                        <div className="footer-item">
                            <img src={hours} alt="Часы работы" />
                            <p className="footer-text">Пн-Пт: 09:00 - 23:00<br />Сб-Нд: 12:00 - 23:00</p>
                        </div>
                        <div className="footer-item">
                            <img src={emailWhite} alt="Email" />
                            <p className="footer-text">pastplates@gmail.com</p>
                        </div>
                        <div className="footer-item">
                            <img src={phoneWhite} alt="Телефон" />
                            <p className="footer-text">+38 099 634 46 71</p>
                        </div>
                    </div>
                    <div className="container-footer__column-item">
                        <h1 className="footer-title">Локації ресторану</h1>
                        <Link to="/hall/1" className="footer-links">
                            -Середньовічний зал
                        </Link>
                        <Link to="/hall/2" className="footer-links">
                            -Вікторіанський стиль
                        </Link>
                        <Link to="/hall/3" className="footer-links">
                            -80 ті роки
                        </Link>
                        <Link to="/hall/4" className="footer-links">
                            -Сучасний
                        </Link>
                        <Link to="/hall/5" className="footer-links">
                            -Футуристичний стиль
                        </Link>
                        <Link to="/hall/6" className="footer-links">
                            -Літня тераса в стилі Urban jungle
                        </Link>
                    </div>
                    <div className="container-footer__column-item">
                        <h1 className="footer-title">Інше</h1>
                        <a href="/menu" className="footer-links">-Меню</a>
                        <a href="/delivery" className="footer-links">-Доставка</a>
                        <Link to="/hall" className="footer-links">
                            Наші зали
                        </Link>
                        <Link to="/contacts" className="footer-links">
                            Контакти
                        </Link>
                        <a href="/login" className="footer-links">-Вхід/Реєстрація</a>
                    </div>
                    <p className="copyright">
                        Copyright © 2025. Будь-яке використання або копіювання матеріалів сайту,
                        елементів дизайну та оформлення допускається лише з дозволу правовласника!
                    </p>
                </div>
            </div>
        </footer>    );
}

export default Footer;
