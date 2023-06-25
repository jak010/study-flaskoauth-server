from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
)

db = SQLAlchemy()


def get_url():
    return URL(
        drivername='mysql',
        host="127.0.0.1",
        port=5501,
        username='root',
        password='1234',
        database='oos',
        query={'charset': 'utf8'}
    )


class Session:

    def __init__(self):
        self._url = URL(
            drivername='mysql',
            host="127.0.0.1",
            port=5501,
            username='root',
            password='1234',
            database='oos',
            query={'charset': 'utf8'}
        )

        self._engine = create_engine(self._url, echo=True)
        self._session = scoped_session(
            sessionmaker(
                autoflush=False,
                autocommit=False,
                bind=self._engine,
                expire_on_commit=True,
            )
        )

    def __enter__(self):
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.commit()
        self._session.close()
