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
#Запит з використанням INNER JOIN #######################################################################
#t = text("SELECT DISTINCT Message.text, Tag.text FROM Message INNER JOIN Tag ON Message.text = Tag.text")
#Запит з використанням LEFT JOIN#########################################################################
#t = text("SELECT DISTINCT Message.text, Tag.text FROM Message LEFT JOIN Tag ON Message.text = Tag.text")
#Запит з використанням RIGHT JOIN #######################################################################
#t = text("SELECT DISTINCT Message.text, Tag.text FROM Message RIGHT JOIN Tag ON Message.text = Tag.text")
#Запит з використанням INNER JOIN і умовою###############################################################
#t = text("SELECT DISTINCT Message.text, Tag.text FROM Message "
#         "INNER JOIN Tag ON Message.text = Tag.text IS NOT NULL")
#Запит з використанням INNER JOIN і умовою LIKE##########################################################
#t = text("SELECT DISTINCT Message.id, Tag.id FROM Message "
#         "INNER JOIN Tag ON Message.id = Tag.id LIKE(Tag.id>0)")
#Запит з використанням INNER JOIN  і використанням агрегатної функції####################################
#t = text("SELECT MIN(Message.id), Tag.id FROM Message INNER JOIN Tag ON Message.id = Tag.id")
#Запит з використанням INNER JOIN  і використанням агрегатної функції і умови HAVING#####################
t = text("SELECT MIN(Message.id), Tag.id FROM Message INNER JOIN Tag ON Message.id = Tag.id HAVING id>=1")

conn = engine.connect()

result = conn.execute(t)

for row in result:
    print(row[0])
