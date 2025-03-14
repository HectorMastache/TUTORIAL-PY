from sqlalchemy import create_engine, MetaData, Table
import pandas

if __name__ == '__main__':

    user = 'hmastache2'
    password = 'ntKi692yFiQs'
    host = 'powerflow.cluster-cqdr2juebleo.us-east-2.rds.amazonaws.com'
    port = '5432'
    nameDB = 'pciDB'

    conexion_str = f'postgresql://{user}:{password}@{host}:{port}/{nameDB}'

    engine = create_engine(conexion_str)

    query = 'SELECT * FROM catalogo;'

    df = pandas.read_sql(query,engine)

    print(df)