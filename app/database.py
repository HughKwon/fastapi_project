from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

## yield statement ##
## "yield" returns a generator object to the one who calls the function which contains the yield
## whenever the function is called, the execution will start from the last yield expression
## it will continue the rest of the execution (finally statement) once we're done sending the response
## this is memory efficient, also yield statement stops the function.
## Here's another way to do the get_db
## def get_db():
##    with Sesion(engine) as session:
##        yield session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SQLALCHEMY_DABABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

## TODO: https://docs.sqlalchemy.org/en/20/core/engines.html READ THIS
engine = create_engine(SQLALCHEMY_DABABASE_URL)

##from: https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker
## sessionmaker provides Session objects with fixed configuration (in the parameters below)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='password',cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection was successful")
#         break

#     except Exception as error:
#         print("Connecting to database failed.")
#         print("Error: ",error)
#         time.sleep(2) 
# # my_posts = [{"title":"title of post 1", "content": "content of post 1"}]