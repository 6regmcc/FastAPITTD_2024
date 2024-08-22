uvicorn app.main:app --reload


pip freeze > requirement.txt


docker-compose rm 
docker-compose build
docker-compose up 


alembic init migrations
alembic revision --autogenerate -m "inital"
alembic -n devdb revision --autogenerate -m "inital"
alembic -n devdb upgrade head
