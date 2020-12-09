from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, \
    BOOLEAN, TIME, Text, SMALLINT, ForeignKey
from sqlalchemy import text
engine = create_engine("mysql+pymysql://root:Rootpass12345@localhost/testflask", echo=True)
meta = MetaData()

Message = Table(
    'message', meta,
    Column('id', Integer, primary_key=True),
    Column('text', String(255), nullable=False)
)

Tag = Table(
    'tag', meta,
    Column('id', Integer, primary_key=True),
    Column('text', String(32), nullable=False)

)

User = Table(
    'user', meta,
    Column('id', Integer, nullable=False, primary_key=True),
    Column('username', String(80)),
    Column('email', String(120)),
    Column('password', String(80))
)

meta.create_all(engine)
#Простий запит на вибірку######################################################
#s = User.select()

#Запит на вибірку з однією умовою##############################################
s = User.select().where(User.c.id < 3)

#Запит на вибірку з двома умовами через “and”###################################
#t = text("SELECT User.username, User.email FROM User WHERE User.email BETWEEN :x and :y")
#Запит на вибірку з двома умовами через «оr»#####################################
#t = text("SELECT User.username, User.email, User.id FROM User WHERE User.id = 1 OR User.id = 2")
#Запит на вибірку з використанням DISTINCT#######################################
#t = text("SELECT DISTINCT User.email FROM User")
#Запит на вибірку з  умовою between…and, not between…and#########################
#t = text("SELECT User.email FROM User "
#         "WHERE User.id = 2 AND User.email BETWEEN :x and :y")
#Запит на вибірку з умовою in, not in############################################
#t = text("SELECT User.email FROM User WHERE User.id IN (1, 2)")
#3 запити на вибірку з умовою like з використанням різних шаблонів вибірки#######
#t = text("SELECT User.username FROM User WHERE User.username LIKE(username)")
#t = text("SELECT * FROM User WHERE User.id LIKE(id)")
#t = text("SELECT User.password FROM User WHERE  User.id LIKE(id>0)")
#Запит на вибірку з використанням IS NULL і IS NOT NULL##########################
t = text("SELECT * FROM User WHERE  User.username IS NOT NULL")

conn = engine.connect()

results = conn.execute(s)
print("S")
for rows in results:
    print(rows)

result = conn.execute(t, x='A', y='Z').fetchall()
print("T")
for row in result:
    print(row)
