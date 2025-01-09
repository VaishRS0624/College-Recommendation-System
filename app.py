import mysql.connector
from aimodel import *
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'password',
    'database': 'collegedatabase',
}

def get_db_connection():
    return mysql.connector.connect(**db_config)
import mysql.connector

try:
    db = get_db_connection()
    cursor = db.cursor()

except Exception as e:
    print(f"Error connecting to the database: {e}")

#
# rank = input('instituteCode')
# # print(institute_code)
# score = input('instituteName')
# # Try inserting data into the 'colleges' table
# connection = get_db_connection()
# cursor = connection.cursor()
# print("Request received")
# # Rest of the code...
# print("Data inserted successfully")
# a = aimodel()
# listodchoices = a.trainmodel([int(rank), int(score)])
# insert_query = """
#     insert into choices(choicecodesss) values(%s)
#     """
# insert_query1 = """
#             truncate choices
#             """
# cursor.execute(insert_query1)
# connection.commit()
# for i in listodchoices:
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute(insert_query, [(i)])
#     connection.commit()
#     cursor.close()
#     connection.close()
# insert_query2 = """
#                     call collegedatabase.unite_all(%s);
#                     """
# connection = get_db_connection()
# cursor = connection.cursor()
# cursor.execute(insert_query, [str(listodchoices[0])])
# connection.commit()
# cursor.close()
# connection.close()
# # print(insert_query)
# viewquery = """ select * from final1"""
# cursor.execute(viewquery)
# # Commit the changes to the database
# result = cursor.fetchall()
# print(result)
# connection.commit()
#
# # Assuming some success response
# response_data = {'success': True, 'message': 'College added successfully'}
# print(response_data)
