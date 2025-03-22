import React from 'react';

import tracery from './../img/main-page/header/tracery.svg';
import review1 from './../img/main-page/review/review-1.png';
import review2 from './../img/main-page/review/review-2.png';
import review3 from './../img/main-page/review/review-3.png';
import review4 from './../img/main-page/review/review-4.png';


function Reviews() {
    const reviews = [
        {
            img: review1,
            text: "Неймовірне місце! Відчув себе мандрівником у часі — кожен зал має свою унікальну атмосферу, а страви просто вражають. Особливо сподобалася середньовічна зала: автентичний інтер’єр, жива музика та смачне м’ясо на вертелі. Обов’язково повернуся ще раз, щоб відвідати інші епохи!",
            name: "Олександр Гаврилюк",
            age: "35 років"
        },
        {
            img: review2,
            text: "Це більше, ніж просто ресторан – це  подорож у часі! Атмосфера продумана до дрібниць: інтер’єр, музика, меню – все відповідає обраній епосі. Особливо вразила зала в стилі 80-х: ретро-музика та смачні молочні коктейлі. Обов’язково повернуся, щоб випробувати всі епохи!",
            name: "Анастасія Коваль",
            age: "23 роки"
        },
        {
            img: review3,
            text: "Ресторан просто вражає! Обирали зал у стилі Вікторіанської епохи — витончена атмосфера, класична музика та неймовірно смачні десерти. Було відчуття, ніби потрапила у справжній старовинний салон. Дуже приємне обслуговування. Обов’язково повернуся, щоб відвідати інші зали!",
            name: "Марина Остапенко",
            age: "29 років"
        },
        {
            img: review4,
            text: "Ідея з рестораном епох просто геніальна! Ми з друзями провели вечір у середньовічному залі – величезні дубові столи, факели, камін, а м’ясо на вертелі та медовий ель були просто фантастичні. Відчуття, ніби опинився на справжньому лицарському бенкеті. Дуже атмосферно, рекомендую всім!",
            name: "Дмитро Савчук",
            age: "24 роки"
        }
    ];
    return (

        <div className="reviews reviews-halls">
                <div className="main-page">
                    <div className="main-page__title">
                        <p className="main-page__main-content main-page__title">Відгуки</p>
                        <img className="tracery" src={tracery} alt=""/>
                        <h1 className="title-center">Посмішки наших гостей</h1>
                    </div>
                    <div className="container-reviews">
                        {reviews.map((review, index) => (
                            <div className="container-reviews__item" key={index}>
                                <div className="photo">
                                    <img src={review.img} alt=""/>
                                </div>
                                <div className="container-reviews__item-review">
                                    <p className="main-page__main-content content-review">{review.text}</p>
                                    <p className="description-item__title">{review.name}<br/>{review.age}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

    );
}

export default Reviews;