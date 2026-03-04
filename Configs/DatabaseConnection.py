from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://neondb_owner:npg_WUCG0E6alMYq@ep-jolly-smoke-a8roga89-pooler.eastus2.azure.neon.tech/my_database?sslmode=require&channel_binding=require'

engine = create_engine(DATABASE_URL)

"""
if __name__ == '__main__':
    try:
        with engine.connect() as conn:
            result = conn.execute(text('SELECT * from "Places"'))
            for i in result:
                    print(f"The name retrieved is {i[1]}")
    except Exception as e:
        print(f"Connection failed: {e}")
"""