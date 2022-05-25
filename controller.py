import db_operations as db
def run():
    data = db.get_base()
    print(data[0])
    print(data[1])
    print(data[2])