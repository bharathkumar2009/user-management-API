from database import get_connection

def create_user(name,email,age):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name,email,age) VALUES (?,?,?)",
                   (name,email,age))
    connection.commit()
    user_id = cursor.lastrowid

    connection.close()
    return user_id


def get_users():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall

    connection.close()
    return users


def get_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id  = ?",
                   (user_id))

    user = cursor.fetchone
    connection.close()
    return user