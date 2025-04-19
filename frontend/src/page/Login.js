import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import tracery from "../img/main-page/header/tracery.svg";

function Login() {
    const [activeTab, setActiveTab] = useState('login');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phone, setPhone] = useState('');
    const [error, setError] = useState('');

    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError('');

        try {
            const response = await fetch('http://127.0.0.1:8000/api/token/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': '*/*'
                },
                body: JSON.stringify({ email, password })
            });

            if (!response.ok) {
                throw new Error('Невірний email або пароль');
            }

            const data = await response.json();
            localStorage.setItem('accessToken', data.access);
            localStorage.setItem('refreshToken', data.refresh);
            localStorage.setItem('userEmail', email);

            navigate('/menu');
        } catch (err) {
            setError(err.message);
        }
    };

    const handleRegister = async (e) => {
        e.preventDefault();
        setError('');

        try {
            const response = await fetch('http://127.0.0.1:8000/api/user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': '*/*'
                },
                body: JSON.stringify({
                    email,
                    password,
                    first_name: firstName,
                    last_name: lastName,
                    phone
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(
                    errorData?.detail || 'Помилка реєстрації. Перевір дані.'
                );
            }

            alert('Реєстрація успішна! Тепер увійди в акаунт.');
            setActiveTab('login');
        } catch (err) {
            setError(err.message);
        }
    };


    return (
        <main>
            <div className="main-page">
                <div className="main-page__title">
                    <p className="main-page__main-content main-page__title">Past & Plates</p>
                    <img className="tracery" src={tracery} alt="Текстурний візерунок" />
                    <h1 className="title-center">
                        Зареєструйся на сайті, щоб першим дізнаватись про <br />
                        тематичні вечори та ексклюзивні знижки
                    </h1>
                </div>
            </div>

            <div className="login">
                <div className="login__tabs">
                    <button
                        className={`tab ${activeTab === 'login' ? 'active' : ''}`}
                        onClick={() => setActiveTab('login')}
                    >
                        Вхід
                    </button>
                    <button
                        className={`tab ${activeTab === 'register' ? 'active' : ''}`}
                        onClick={() => setActiveTab('register')}
                    >
                        Реєстрація
                    </button>
                </div>

                {activeTab === 'login' && (
                    <form className="login__form" onSubmit={handleLogin}>
                        <input
                            type="email"
                            placeholder="Email"
                            className="login__input"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                        <input
                            type="password"
                            placeholder="Пароль"
                            className="login__input"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                        {error && <p className="login__error">{error}</p>}
                        <p className="login__text">
                            Ще немає акаунту? <button className="button-nav" type="button" onClick={() => setActiveTab('register')}>Зареєструватись</button>
                        </p>

                        <button type="submit" className="login__button">Увійти в акаунт</button>
                    </form>
                )}

                {activeTab === 'register' && (
                    <form className="login__form" onSubmit={handleRegister}>
                        <input
                            type="text"
                            placeholder="Ім'я"
                            className="login__input"
                            value={firstName}
                            onChange={(e) => setFirstName(e.target.value)}
                            required
                        />
                        <input
                            type="text"
                            placeholder="Прізвище"
                            className="login__input"
                            value={lastName}
                            onChange={(e) => setLastName(e.target.value)}
                            required
                        />
                        <input
                            type="tel"
                            placeholder="Номер телефону"
                            className="login__input"
                            value={phone}
                            onChange={(e) => setPhone(e.target.value)}
                            required
                        />
                        <input
                            type="email"
                            placeholder="Email"
                            className="login__input"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                        <input
                            type="password"
                            placeholder="Пароль"
                            className="login__input"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                        {error && <p className="login__error">{error}</p>}
                        <p className="login__text">
                            Вже є акаунт? <button className="button-nav" onClick={() => setActiveTab('login')}>Увійти</button>
                        </p>
                        <button type="submit" className="login__button">Зареєструватись</button>
                    </form>
                )}
            </div>
        </main>
    );
}

export default Login;
