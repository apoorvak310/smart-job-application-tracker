from models.user import User
user = User(
    id=1,
    name='Apoorva',
    email='apoorva@gmail.com',
    phone='98787867656',
    education='B.Tech'
)
res = user.display()
print(res)