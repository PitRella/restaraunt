import React from 'react';
import spoon from './../img/main-page/header/spoon.svg';
import socialPhoto1 from './../img/main-page/social/social-photo-1.png';
import socialPhoto2 from './../img/main-page/social/social-photo-2.png';
import socialPhoto3 from './../img/main-page/social/social-photo-3.png';



function Social() {
    return (
        <div className="social">
                <div className="main-content__container">
                    <div className="social__content">
                        <div className="social__title">
                            <p className="main-page__main-content">Instagram</p>
                            <img src={spoon} alt="" className="spoon" />
                            <h1 className="title-left">Cоціальні мережі</h1>
                        </div>
                        <div className="social__content">
                            <p className="main-page__main-content">Слідкуйте за нами в соцмережах, щоб першими отримувати ексклюзивні промокоди та знижки! А наш Telegram-бот допоможе вам бути в курсі всіх тематичних заходів і вечірок.</p>
                            <div className="social__buttons">
                                <a href="https://www.instagram.com/" className="button-accent">Instagram</a>
                                <a href="/telegram" className="button-non-accent">Telegram</a>
                                <a href="/our-halls" className="button-non-accent">Зали</a>
                            </div>
                        </div>
                    </div>
                    <div className="social__photo">
                        <a href="https://www.instagram.com/" className="social__photo-link"><img src={socialPhoto1} alt="" className="social__photo-item" /></a>
                        <a href="https://www.instagram.com/" className="social__photo-link"><img src={socialPhoto2} alt="" className="social__photo-item" /></a>
                        <a href="https://www.instagram.com/" className="social__photo-link"><img src={socialPhoto3} alt="" className="social__photo-item" /></a>
                    </div>
                </div>
            </div>
    );
}

export default Social;
