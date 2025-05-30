# Restaraunt

## 📦 Stack

- Python 3.12
- Django 5
- PostgreSQL
- Docker + Docker Compose

---


### Local deploy

> Required python 3.12 and PostgresSQL

1. Clone repository

```bash
git clone https://github.com/PitRella/restaraunt.git
cd restaraunt
```
2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install requirements
```bash
pip install -r requirements.txt
```

4. Create .env
```bash
cp .env_example .env
```
5. Set .env variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
POSTGRES_DB=your-db
POSTGRES_USER=your-pg-user
POSTGRES_PASSWORD=your-pg-pass
POSTGRES_HOST=host
POSTGRES_PORT=5432
```
6. Make migrations, create admin
```bash
python manage.py migrate
python manage.py createsuperuser
```
7. Run server
```bash
python manage.py runserver
```

### Docker compose
1. Make sure you have installed docker, docker compose
2. Create .env
```bash
cp .env_example .env
```
3. Set .env variables
```bash
SECRET_KEY=your-secret-key
DEBUG=False
POSTGRES_DB=your-db
POSTGRES_USER=your-pg-user
POSTGRES_PASSWORD=your-pg-pass
POSTGRES_HOST=host
POSTGRES_PORT=5432
```
4. Run docker compose services
```bash
docker-compose up -d --build
```
5. Run migrations, create superuser
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```
