from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

Base = declarative_base()

try:
	usr = environ['HBNB_YELP_MYSQL_USER']
	pwd = environ['HBNB_YELP_MYSQL_PWD']
	host = environ['HBNB_YELP_MYSQL_HOST']
	db = environ['HBNB_YELP_MYSQL_DB']
except KeyError as err:
	print("""Must provide the following as environment variables:
	      HBNB_YELP_MYSQL_USER, HBNB_YELP_MYSQL_PWD,
	      HBNB_YELP_MYSQL_HOST, HBNB_YELP_MYSQL_DB""")
db_engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db))

if environ.get('HBNB_YELP_ENV') == 'test':
	Base.metadata.drop_all(db_engine)

Base.metadata.create_all(db_engine)

db_session = scoped_session(sessionmaker(bind=db_engine, expire_on_commit=False))
