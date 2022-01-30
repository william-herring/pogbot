from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


db = create_engine('postgresql://localhost:5432')
meta = MetaData(db)
user_table = Table('user', meta,
                   Column('username', String),
                   Column('description', String),
                   Column('pogness', Integer),
                   Column('img', String))


def create_user(username: str, description: str, pogness: int, img: str):
    with db.connect() as connection:
        user_table.insert().values(username=username, description=description, pogness=pogness, img=img)
        statement = user_table.select()
        result_set = connection.execute(statement)
        print(result_set)
        for i in result_set:
            print(i)
