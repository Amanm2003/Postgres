from db import get_connection

def create_record(name, age, email):
    connection = get_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO your_table (name, age, email) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, age, email))
    connection.commit()
    cursor.close()
    connection.close()

def read_records():
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM your_table"
    cursor.execute(select_query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def update_record(record_id, name, age, email):
    connection = get_connection()
    cursor = connection.cursor()
    update_query = "UPDATE your_table SET name = %s, age = %s, email = %s WHERE id = %s"
    cursor.execute(update_query, (name, age, email, record_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_record(record_id):
    connection = get_connection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM your_table WHERE id = %s"
    cursor.execute(delete_query, (record_id,))
    connection.commit()
    cursor.close()
    connection.close()
