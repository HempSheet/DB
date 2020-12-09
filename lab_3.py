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

#Запит з функцією min або max###############################################################
#Запит на вибірку з використанням агрегатної функції і виведенням ще декількох полів########
#t = text("SELECT MAX(User.id) AS maximum FROM User")
#Запит з функцією sum або avg###############################################################
#t = text("SELECT SUM(User.id) FROM User")
#Запит з функцією count#####################################################################
#t = text("SELECT count(*) FROM User")
#Запит на вибірку з використанням агрегатної функції і умовою на вибірку поля###############
#t = text("SELECT MIN(User.id) FROM User WHERE User.username IS NOT NULL")
#Запит на вибірку з використанням агрегатної функції і умовою на агрегатну функцію##########
#t = text("SELECT MIN(User.id) FROM User WHERE User.id = 1 OR User.id = 2")
#Запит на вибірку з використанням агрегатної функції, умовою на агрегатну функцію, умовою на
# вибірку поля з сортуванням даних.#########################################################
t = text("SELECT MIN(User.id) FROM User WHERE User.id = 1 OR User.id = 2 ORDER BY User.id")

conn = engine.connect()

result = conn.execute(t)

for row in result:
    print(row[0])
