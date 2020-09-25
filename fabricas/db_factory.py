from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbFactory:
    def __init__(self, user, password, host, port, schema, driver, dialect):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__schema = schema
        self.__driver = driver
        self.__dialect = dialect

    def engine(self):
        uri = "{}+{}://{}:{}@{}:{}/{}".format(
            self.__dialect,
            self.__driver,
            self.__user,
            self.__password,
            self.__host,
            self.__port,
            self.__schema
        )
        new_engine = create_engine(uri)
        return new_engine

    def session(self, engine=None):
        if engine is None:
            engine = self.engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
