import polars as pl
import psycopg2
import pandas as pd

def load_data_from_timescaledb(query, conn_params):
    conn = psycopg2.connect(**conn_params)
    df = pd.read_sql(query, conn)
    conn.close()
    return pl.from_pandas(df)