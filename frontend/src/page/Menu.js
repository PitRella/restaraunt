import React, { useEffect, useState } from "react";
import separator from "./../img/main-page/header/separator.svg";
import tracery from "./../img/main-page/header/tracery.svg";

function Menu() {
    const [menus, setMenus] = useState([]);
    const [selectedMenuId, setSelectedMenuId] = useState(null);
    const [dishes, setDishes] = useState([]);
    const [activeMenuName, setActiveMenuName] = useState('');

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/menu/')
            .then(res => res.json())
            .then(data => {
                setMenus(data);
                if (data.length > 0) {
                    setSelectedMenuId(data[0].id);
                    setActiveMenuName(data[0].name);
                }
            });
    }, []);

    useEffect(() => {
        if (selectedMenuId !== null) {
            fetch(`http://127.0.0.1:8000/api/menu/${selectedMenuId}/dishes/`)
                .then(res => res.json())
                .then(data => setDishes(data));
        }
    }, [selectedMenuId]);

    return (
        <main>
            <div className="main-page">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Past & Plates</p>
                    <img className="tracery" src={tracery} alt="" />
                    <h1 className="title-center">Меню ресторану</h1>
                </div>
            </div>

            <div className="menu-tabs">
                {menus.map(menu => (
                    <button
                        key={menu.id}
                        className={`menu-tab-btn ${selectedMenuId === menu.id ? 'active' : ''}`}
                        onClick={() => {
                            setSelectedMenuId(menu.id);
                            setActiveMenuName(menu.name);
                        }}
                    >
                        {menu.name}
                    </button>
                ))}
            </div>

            <div className="menu-block">
                <h2 className="menu-block__title">{activeMenuName}</h2>
                <div className="menu-block__grid">
                    {dishes.map((dish, index) => (
                        <div key={index} className="menu-card">
                            <img
                                src={`http://127.0.0.1:8000${dish.image}`}
                                alt={dish.name}
                                className="menu-card__image"
                            />
                            <div className="menu-card__info">
                                <p className="menu-card__name">{dish.name}</p>
                                <p className="menu-card__details">{dish.grams}г / {dish.calories} ккал</p>
                                <p className="menu-card__price">{dish.price} грн</p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            <img className="separator" src={separator} alt="separator" />
        </main>
    );
}

export default Menu;
