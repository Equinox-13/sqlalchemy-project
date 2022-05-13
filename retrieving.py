from main import User, Session, engine

local_session = Session(bind=engine)

# Returns all objects
# users = local_session.query(User).all()
# # for user in users:
# #     print(user)

# Return for one object
user = local_session.query(User).filter(User.username=='john').first()
print(user)
