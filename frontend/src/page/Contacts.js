import React from 'react';
import tracery from './../img/main-page/header/tracery.svg';
import Social from './../components/Social';



function Contacts() {
    return (
        <main>
            <div className="main-page">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Past & Plates</p>
                    <img className="tracery" src={tracery} alt="" />
                    <h1 className="title-center">Контакти</h1>
                </div>
            </div>
            <div className="contacts-container">
                <div className="contacts-container__item">
                    <div className="contacts-container__title">Графік роботи:</div>
                    <div className="contacts-container__content">ПН-ПТ: 09:00 - 23:00<br />СБ-НД: 12:00 - 23:00</div>
                </div>
                <div className="contacts-container__item">
                    <div className="contacts-container__title">Номер телефону:</div>
                    <div className="contacts-container__content">+38 099 634 46 71</div>
                </div>
            </div>
            <Social />
            <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2045.0786663191016!2d36.02441193887725!3d49.89845159798912!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x41279c4183f18d3d%3A0x6396fa98654a29e8!2z0JHRg9C00YssINCl0LDRgNGM0LrQvtCy0YHQutCw0Y8g0L7QsdC70LDRgdGC0YwsIDYyNDU2!5e0!3m2!1sru!2sua!4v1742423698465!5m2!1sru!2sua"
                width="100%"
                height="500"
                style={{ border: 0 }}
                allowFullScreen=""
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                title="Google Maps Location"
            ></iframe>

        </main>

    );
}

export default Contacts;
