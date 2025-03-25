import React from "react";
import { Link } from "react-router-dom";
import spoon from "./../img/main-page/header/spoon.svg";
import tracery from "./../img/main-page/header/tracery.svg";
import hall1 from "./../img/halls/hall-1.svg";
import hall2 from "./../img/halls/hall-2.svg";
import hall3 from "./../img/halls/hall-3.svg";
import hall4 from "./../img/halls/hall-4.svg";
import hall5 from "./../img/halls/hall-5.svg";
import hall6 from "./../img/halls/hall-6.svg";
import plusIcon from "./../img/halls/+.svg";
import separator from "./../img/halls/separator.svg";
import Reviews from "./../components/Reviews";

const halls = [
    { id: 1, name: "Середньовіччя", img: hall1 },
    { id: 2, name: "Вікторіанський стиль", img: hall2 },
    { id: 3, name: "80-ті роки", img: hall3 },
    { id: 4, name: "Сучасний", img: hall4 },
    { id: 5, name: "Футуристичний стиль", img: hall5 },
    { id: 6, name: "Літня тераса Urban jungle", img: hall6 },
];

function Halls() {
    return (
        <main>
            <div className="main-page">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Past & Plates</p>
                    <img className="tracery" src={tracery} alt="" />
                    <h1 className="title-center">Зали ресторану</h1>
                </div>
            </div>
            <div className="halls">
                <div className="halls__item">
                    <div className="halls__item-link">
                        {halls.map((hall) => (
                            <Link to={`/hall/${hall.id}`} key={hall.id}>
                                <img src={hall.img} alt={hall.name} />

                            </Link>
                        ))}
                    </div>
                </div>
            </div>
            <Reviews />
            <div className="question">
                <div className="question__title">
                    <div className="question__title-text">
                        <p className="main-page__main-content">Питання</p>
                        <img src={spoon} alt="" className="spoon"/>
                        <h1 className="title-left">Відповіді на часті питання</h1>
                    </div>
                </div>
                {["Скільки коштує бронювання залу?", "Якщо я не зможу прийти у запланований час?", "Як забронювати зал?", "Чи є можливість зробити подарунковий сертифікат?", "Чи можна на сайті отримати подарунки?"].map((question, index) => (
                    <div key={index} className="question-item">
                        <div className="question-item__question">
                            <div className="question-item__question-row">
                                <h1 className="question-item__question-title">{question}</h1>
                                <img src={plusIcon} className="plus" data-index={index + 1} alt=""/>
                            </div>
                            <div className="question-item__question-answer" data-index={index + 1}>Відповідь на питання...</div>
                        </div>
                        <img src={separator} className="separator-halls" alt=""/>
                    </div>
                ))}
            </div>
            <div className="discount">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Бронювання</p>
                    <img className="tracery" src={tracery} alt=""/>
                    <h1 className="title-center">Забронюй столик та отримуй знижку -10% на перший візит</h1>
                    <p className="main-page__title text-center"><br/>Залишайте свій номер телефону та очікуйте дзвінка менеджера протягом 10 хв</p>
                </div>
                <div className="placeholder">
                    <div className="placeholder__item">
                        <label htmlFor="phone"></label>
                        <input type="tel" id="phone" className="phone-input" placeholder="Номер телефону +38 (___) ___-__-__"/>
                    </div>
                    <a href="" className="button-accent">Надіслати</a>
                </div>
            </div>
        </main>
    );
}

export default Halls;
