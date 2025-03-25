import React from "react";
import { Link } from "react-router-dom";

import tracery from "../../img/main-page/header/tracery.svg";
import hall1 from "../../img/halls/hall-1.svg";
import hall2 from "../../img/halls/hall-2.svg";
import hall3 from "../../img/halls/hall-3.svg";
import hall4 from "../../img/halls/hall-4.svg";
import hall5 from "../../img/halls/hall-5.svg";
import hall6 from "../../img/halls/hall-6.svg";

import separator from "../../img/halls/separator.svg";

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
                    <h1 className="title-center">Меню ресторану</h1>
                </div>
            </div>
            <div className="menu">
                <div className="menu-button">
                    <Link to="/"></Link>
                </div>
                <div className="menu-item">

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

        </main>
    );
}

export default Halls;
