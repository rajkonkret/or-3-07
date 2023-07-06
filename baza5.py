from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
ssesion = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# create
Base.metadata.create_all(engine)
user1 = User(name="John", age=25)
ssesion.add(user1)
ssesion.commit()

# select - get
users = ssesion.query(User).all()
for user in users:
    print(user)  # <__main__.User object at 0x000001DBAF01D190>

    print(user.name)  # John
    print(user.age)

# update
user1.age = 45
ssesion.commit()

# delete
ssesion.delete(user1)
ssesion.commit()
