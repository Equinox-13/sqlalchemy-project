from main import Session, engine, User

local_session = Session(bind=engine)

user_to_update = local_session.query(User).filter(User.username=='john').first()
user_to_update.username = "johnathan"
user_to_update.email = "johnathan@company.com"
local_session.commit()
print(user_to_update)
