from main import Session, engine, User
from sqlalchemy import desc

local_session = Session(bind=engine)

# sort by ascending order
# users_asc = local_session.query(User).order_by(User.username).all()

# sort by descending order
users_desc = local_session.query(User).order_by(desc(User.username)).all()

for user in users_desc:
    print(f"User {user.username}")
