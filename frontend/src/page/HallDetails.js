import React from "react";
import { useParams } from "react-router-dom";
import tracery from "./../img/main-page/header/tracery.svg";
import spoon from "./../img/main-page/header/spoon.svg";
import dislocationImg from "./../img/halls/dislocation.png";

import hall1_1 from "./../img/halls/hall-1-column-1.png";
import hall1_2 from "./../img/halls/hall-1-column-2.png";
import hall1_3 from "./../img/halls/hall-1-column-3.png";

import hall2_1 from "./../img/halls/hall-2-column-1.png";
import hall2_2 from "./../img/halls/hall-2-column-2.png";
import hall2_3 from "./../img/halls/hall-2-column-3.png";

import hall3_1 from "./../img/halls/hall-3-column-1.png";
import hall3_2 from "./../img/halls/hall-3-column-2.png";
import hall3_3 from "./../img/halls/hall-3-column-3.png";

import hall4_1 from "./../img/halls/hall-4-column-1.png";
import hall4_2 from "./../img/halls/hall-4-column-2.png";
import hall4_3 from "./../img/halls/hall-4-column-3.png";

import hall5_1 from "./../img/halls/hall-5-column-1.png";
import hall5_2 from "./../img/halls/hall-5-column-2.png";
import hall5_3 from "./../img/halls/hall-5-column-3.png";

import hall6_1 from "./../img/halls/hall-6-column-1.png";
import hall6_2 from "./../img/halls/hall-6-column-2.png";
import hall6_3 from "./../img/halls/hall-6-column-3.png";

const halls = {
    1: {
        name: "Зал Середньовіччя: дух стародавніх часів",
        images: [hall1_1, hall1_2, hall1_3],
        place: "68 місць"
    },
    2: {
        name: "Зал Бароко: епоха розкоші та вишуканості",
        images: [hall2_1, hall2_2, hall2_3],
        place: "105 місць"
    },
    3: {
        name: "Зал 80-х: неон, ритм і дух свободи",
        images: [hall3_1, hall3_2, hall3_3],
        place: "86 місць"
    },
    4: {
        name: "Зал Сучасності: яскравий світ аніме",
        images: [hall4_1, hall4_2, hall4_3],
        place: "45 місць"
    },
    5: {
        name: "Зал Майбутнього: втілення технологій і стилю",
        images: [hall5_1, hall5_2, hall5_3],
        place: "68 місць"
    },
    6: {
        name: "Літня тераса: зелений простір для гри та релаксу",
        images: [hall6_1, hall6_2, hall6_3],
        place: "120 місць"
    }
};

function HallDetails() {
    const { id } = useParams();
    const hall = halls[Number(id)]; // Приводим к числу

    if (!hall) {
        return <h1>Зал не знайдено</h1>;
    }

    return (
        <main>
            <div className="main-page">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Past & Plates</p>
                    <img className="tracery" src={tracery} alt=""/>
                    <h1 className="title-center">{hall.name}</h1>
                    <p className="main-page__main-content main-page__title">{hall.place}</p>
                </div>
            </div>
            <div className="hall-details">
                <div className="hall-images">
                    {hall.images.map((image, index) => (
                        <div key={index} className="hall-images__item">
                            <img src={image} alt={`${hall.name} - ${index + 1}`}/>
                        </div>
                    ))}
                </div>
            </div>
            <div className="social">
                <div className="main-content__container">
                    <div className="social__content">
                        <div className="social__title">
                            <p className="main-page__main-content">Зв'язок</p>
                            <img src={spoon} alt="spoon" className="spoon" />
                            <h1 className="title-left">
                                Зателефонуйте нам, щоб дізнатись умови та забронювати зал
                            </h1>
                        </div>
                        <div className="social__content">
                            <p className="main-page__main-content">
                                Зв’язатись з нашими менеджерами Ви зможете через соціальні
                                мережі Instagram та Telegram Bot, а також забронювати столик за
                                цим посиланням. За номером телефону: +38 099 634 46 71.
                                Менеджери відповідають тільки у робочий час!
                            </p>
                            <div className="social__buttons">
                                <a
                                    href="https://www.instagram.com/"
                                    className="button-accent"
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    Instagram
                                </a>
                                <a href="#" className="button-non-accent">
                                    Telegram
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="dislocation">
                <div className="dislocation__title">
                    <img src={dislocationImg} alt="Location" />
                </div>
                <div className="dislocation__content">
                    <p>
                        Ресторан Past & Plates розташований у затишному куточку Харківської
                        області, у місті Буди, на вулиці Квітковій, 7. Тут кожен гість може
                        вирушити в захопливу подорож крізь століття, насолоджуючись
                        автентичною атмосферою та вишуканими стравами різних епох.
                    </p>
                    <div className="button-accent__container">
                        <a
                            href="https://maps.app.goo.gl/tu9EcuHrLckmSz6g6"
                            className="button-accent"
                            target="_blank"
                            rel="noopener noreferrer"
                        >
                            Прокласти маршрут
                        </a>
                    </div>
                </div>
            </div>
        </main>
    );
}

export default HallDetails;
