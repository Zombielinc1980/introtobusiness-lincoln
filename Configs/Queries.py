from Configs.DatabaseConnection import *

def retrieve_names():
    names = []
    try:
        with engine.connect() as conn:
            result = conn.execute(text('SELECT * from "Places"'))
            for i in result:
                names.append(i[1])
    except Exception as e:
        print(f"Connection failed: {e}")
    return names