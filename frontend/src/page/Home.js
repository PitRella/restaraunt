import React from 'react';
import { Link } from "react-router-dom";

import tracery from "./../img/main-page/header/tracery.svg";
import slideshow1 from "./../img/main-page/header/slideshow-1.png";
import slideshowRight from "./../img/main-page/header/slideshow-right.png";
import spoon from "./../img/main-page/header/spoon.svg";
import separator from "./../img/main-page/header/separator.svg";

import era1 from './../img/main-page/era/era-1.png';
import era2 from './../img/main-page/era/era-2.png';
import era3 from './../img/main-page/era/era-3.png';
import era4 from './../img/main-page/era/era-4.png';
import era5 from './../img/main-page/era/era-5.png';
import era6 from './../img/main-page/era/era-6.png';
import number1 from './../img/main-page/accomplishments/number-1.svg';
import number2 from './../img/main-page/accomplishments/number-2.svg';
import number3 from './../img/main-page/accomplishments/number-3.svg';
import number4 from './../img/main-page/accomplishments/number-4.svg';
import accomplishmentsPhoto from './../img/main-page/accomplishments/accomplishments-photo.svg';
import Social from './../components/Social';
import Reviews from './../components/Reviews';

function Home() {
    return (
        <main>
            <div className="main-page">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Past & Plates</p>
                    <img className="tracery" src={tracery} alt="Текстурный узор"/>
                    <h1 className="title-center">
                        Ресторан, що об'єднує епохи в смаку та атмосфері
                    </h1>
                </div>
            </div>
            <div className="main-page__content">
                <div className="main-page__content-left">
                    <div className="main-page__main-content">
                        Наш ресторан — це подорож у часі, де кожна зала переносить вас у певну
                        історичну епоху. Ми створили це місце, щоб подарувати вам не лише вишукані
                        страви, а й атмосферу минулого, втілену в інтер'єрі, музиці та традиціях.
                    </div>
                    <div className="slideshow">
                        <img src={slideshow1} alt="Слайд-шоу" className="slideshow__img-1"/>
                    </div>
                </div>

                <div className="main-page__content-right">
                    <img
                        src={slideshowRight}
                        alt="Фоновое изображение"
                        className="main-page__content-right-img"
                    />
                    <div className="description">
                        <h1 className="description-item__title description-item__main-title">
                            Протягом багатьох років
                        </h1>
                        <div className="description-item">
                            <div className="description-item-1">
                                <p className="description-item__title">200+</p>
                                <img src={spoon} alt="Ложка" className="spoon"/>
                                <p className="description-item__text-content">Проведених заходів</p>
                            </div>
                            <img src={separator} alt="Разделитель" className="separator"/>
                            <div className="description-item-1">
                                <p className="description-item__title">90+</p>
                                <img src={spoon} alt="Ложка" className="spoon"/>
                                <p className="description-item__text-content">Вишуканих страв</p>
                            </div>
                            <img src={separator} alt="Разделитель" className="separator"/>
                            <div className="description-item-1">
                                <p className="description-item__title">5</p>
                                <img src={spoon} alt="Ложка" className="spoon"/>
                                <p className="description-item__text-content">Залів епох</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <Social />
            <div className="era">
                <div className="main-page">
                    <div className="main-page__title">
                        <p className="main-page__main-content main-page__title">5 епох, 5 унікальних історій</p>
                        <img className="tracery" src={tracery} alt=""/>
                        <h1 className="title-center">Яку обереш ти?</h1>
                    </div>
                </div>
                <div className="container-era">
                    <div className="era-item">
                        <img src={era1} alt="" className="era-item__image"/>
                        <h1 className="description-item__title era-item__title">Зал Середньовіччя</h1>
                        <div className="main-page__main-content era-content">Переступивши важкі двері, ви опиняєтесь у середньовічному замку. Кам’яні стіни, дубові столи, факели та герби створюють атмосферу лицарських бенкетів. У меню — печені, м’ясо на вертелі, медовий ель і хліб із печі.</div>
                        <Link to="/hall/1" className="button-non-accent">
                            Дізнатись більше
                        </Link>
                    </div>
                    <div className="era-item">
                        <img src={era2} alt="" className="era-item__image"/>
                        <h1 className="description-item__title era-item__title">Зал Барокко</h1>
                        <div className="main-page__main-content era-content">Вишуканість і розкіш переносять вас у світ королівських прийомів. Золоті деталі, оксамит, картини та кришталеві люстри створюють атмосферу величі. У меню — делікатеси французької кухні, вишукані вина та десерти.</div>
                        <Link to="/hall/2" className="button-non-accent">
                            Дізнатись більше
                        </Link>
                    </div>
                    <div className="era-item">
                        <img src={era3} alt="" className="era-item__image"/>
                        <h1 className="description-item__title era-item__title">Зал 80-х</h1>
                        <div className="main-page__main-content era-content">Неон, яскраві кольори та дух свободи — зал у стилі 80-х перенесе вас у світ дискотек, ретро-кіно та поп-культури. Неон, яскраві кольори та дух свободи — зал у стилі 80-х перенесе вас у світ дискотек, ретро-кіно та поп-культури.</div>
                        <Link to="/hall/3" className="button-non-accent">
                            Дізнатись більше
                        </Link>
                    </div>
                    <div className="era-item">
                        <img src={era4} alt="" className="era-item__image"/>
                        <h1 className="description-item__title era-item__title">Зал Сучасності</h1>
                        <div className="main-page__main-content era-content">Яскраві кольори, неонові вивіски та ілюстрації аніме-персонажів перенесуть вас у світ японської поп-культури. У меню — рамен, оніґірі, бульбашковий чай і японські десерти. Зал сучасного світу відкритий для вас!</div>
                        <Link to="/hall/4" className="button-non-accent">
                            Дізнатись більше
                        </Link>
                    </div>
                    <div className="era-item">
                        <img src={era5} alt="" className="era-item__image"/>
                        <h1 className="description-item__title era-item__title">Зал Майбутнього</h1>
                        <div className="main-page__main-content era-content">Голограми, металевий блиск і панорамні екрани створюють атмосферу майбутнього. Мінімалізм, інтерактивні технології та неонове світло додають футуристичного шарму. У меню — молекулярна кухня, космічні коктейлі.</div>
                        <Link to="/hall/5" className="button-non-accent">
                            Дізнатись більше
                        </Link>
                    </div>
                    <div className="era-item">
                        <img src={era6} alt="" className="era-item__image"/>
                        <h1 className="description-item__title era-item__title">Літня Тераса</h1>
                        <div className="main-page__main-content era-content">Оазис серед міста з живими рослинами, дерев’яними меблями та затишною атмосферою. Тут можна насолоджуватися настільними іграми, прохолодними коктейлями та легкими літніми стравами.</div>
                        <Link to="/hall/6" className="button-non-accent">
                            Дізнатись більше
                        </Link>
                    </div>
                </div>
            </div>
            <div className="accomplishments">
                <div className="main-content__container">
                    <div className="accomplishments-container-text">
                        <div className="accomplishments__title">
                            <div className="accomplishments__title-text">
                                <p className="main-page__main-content">Концепція</p>
                                <img src={spoon} alt="" className="spoon"/>
                                <h1 className="title-left">Наші переваги</h1>
                            </div>
                        </div>
                        <div className="accomplishments__content">
                            <div className="accomplishments__content-item">
                                <img src={number1} alt="" className="number"/>
                                <div className="accomplishments__content-item-contant">
                                    <h1 className="accomplishments__content-item-title">Безліч залів на будь-який смак</h1>
                                    <p className="accomplishments__content-item-text">Кожен зал оформлений у стилі певного історичного періоду</p>
                                </div>
                            </div>
                            <div className="accomplishments__content-item">
                                <img src={number2} alt="" className="number"/>
                                <div className="accomplishments__content-item-contant">
                                    <h1 className="accomplishments__content-item-title">Меню для кожної епохи</h1>
                                    <p className="accomplishments__content-item-text">Страви, натхненні кулінарними традиціями відповідної епохи</p>
                                </div>
                            </div>
                            <div className="accomplishments__content-item">
                                <img src={number3} alt="" className="number"/>
                                <div className="accomplishments__content-item-contant">
                                    <h1 className="accomplishments__content-item-title">Заходи, лекції, тематичні вечори</h1>
                                    <p className="accomplishments__content-item-text">Тематичні вечори, лекції та майстер-класи для повного занурення</p>
                                </div>
                            </div>
                            <div className="accomplishments__content-item">
                                <img src={number4} alt="" className="number"/>
                                <div className="accomplishments__content-item-contant">
                                    <h1 className="accomplishments__content-item-title">Автентична атмосфера</h1>
                                    <p className="accomplishments__content-item-text">Костюми персоналу, музика та освітлення передають дух минулого</p>
                                </div>
                            </div>
                        </div>
                        <div className="accomplishments__buttons">
                            <a href="/bron" className="button-accent">Забронювати</a>
                            <a href="/our-halls" className="button-non-accent">Зали</a>
                            <a href="/menu/Menu" className="button-non-accent">Меню</a>
                        </div>
                    </div>
                    <div className="accomplishments__photo">
                        <a href="https://www.instagram.com/" className="accomplishments__photo-link">
                            <img src={accomplishmentsPhoto} alt="" className="accomplishments__photo-item"/>
                        </a>
                    </div>
                </div>
            </div>
            <Reviews />
            <div className="discount">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Бронювання</p>
                    <img className="tracery" src={tracery} alt="" />
                    <h1 className="title-center">Забронюй столик та отримуй знижку -10% на перший візит</h1>
                    <p className="main-page__title text-center"><br />Залишайте свій номер телефону та очікуйте дзвінка менеджера протягом 10 хв</p>
                </div>
                <div className="placeholder">
                    <div className="placeholder__item">
                        <label htmlFor="phone"></label>
                        <input type="tel" id="phone" className="phone-input" placeholder="Номер телефону +38 (___) ___-__-__" />
                    </div>
                    <a href="/index" className="button-accent">Надіслати</a>
                </div>
            </div>
            <div className="big-tracery-container">
                <img src={tracery} className="big-tracery" alt="" />
            </div>

        </main>
    );
}

export default Home;
