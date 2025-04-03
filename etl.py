import pandas as pd
from database import create_connection

def extract_data():
    conn = create_connection()
    query = "SELECT * FROM transaction"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def transform_data(df):
    df['amount'] = df['amount'].apply(lambda x: round(x, 2))
    df['category'] = df['category'].str.title()
    return df

def load_data(df, output_file='processed_data.csv'):
    df.to_csv(output_file, index=False)
    return output_file
