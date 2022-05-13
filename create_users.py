from main import User, Session, engine

users = [
    {
        'username':'jackson',
        'email':'jackson@company.com',
    },
    {
        'username':'jim',
        'email':'jim@company.com',
    },
    {
        'username':'jill',
        'email':'jill@company.com',
    },
]

local_session = Session(bind=engine)

for u in users:
    new_user = User(username=u['username'], email=u['email'])
    local_session.add(new_user)
    local_session.commit()
    print(f"Add {u['username']}")
