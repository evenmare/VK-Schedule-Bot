import mysql.connector as db

token = "press your VK token here"
admin_id = 0 #press your ID here

def connectDB(dbConnection=None):
    try:
        dbConnection.close()
    except Exception:
        True
    dbConnection = db.connect(
        host="localhost",
        user="myauthuser",
        password="password.",
        database="nameDB"
    )

    return dbConnection