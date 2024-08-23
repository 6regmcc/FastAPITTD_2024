import os

import pytest
from sqlalchemy import create_engine

from tests.utils.database_utils import migrate_to_db
from tests.utils.docker_utils import start_database_container
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def db_session():

    container = start_database_container()

    engine = create_engine(os.getenv("TEST_DATABASE_URL"))

    with engine.begin() as connection:
        try:
            migrate_to_db("migrations", "alembic.ini", connection)
        except Exception as error:
            print(error)



    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

    yield SessionLocal

    #container.stop()
    #container.remove()
    engine.dispose()
