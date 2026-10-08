from models.user import User
user = User(
    'Apoorva',
    'apoorva@gmail.com',
    '98787867656',
    'B.Tech'
)
res = user.display()
print(res)