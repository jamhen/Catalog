from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///workoutcatalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='InitUser',
    email='contact.InitUser@gmail.com',
    picture='https://img.com/sdf'
)

session.add(user1)
session.commit()

category1 = Category(
    name='Shoulder',
    user=user1
)

session.add(category1)
session.commit()

item1 = Item(
    name='Dumbell Shoulder Press',
    description='This is exercise is a variation fo the standard military press that puts more focus on the trap muscles and deltoid muscles.',
    category=category1,
    user=user1
)

session.add(item1)
session.commit()

print('Database successfully initialized!')
