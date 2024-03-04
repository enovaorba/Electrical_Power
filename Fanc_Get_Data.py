import mysql.connector
from Fanc import Fanc
from datetime import datetime, timedelta
import sqlite3

class Fanc_Get_Data:
    connection = None  # Global connection variable

    @classmethod
    def connect_to_db(cls):
        # Establish a connection to the MySQL database
        cls.connection = mysql.connector.connect(
            host= "enova-prod-main.cc1atg19czgb.eu-central-1.rds.amazonaws.com",
            user="admin",
            password="JdAA78!fjGjkasdDF8",
            database="Electrical_Power",
            port = 3308  
        )
        # Create a cursor object to interact with the database
        cursor = cls.connection.cursor()
        return cls.connection, cursor

    @staticmethod
    def sql_run_script(sql):
        if Fanc_Get_Data.connection is None:
            Fanc_Get_Data.connect_to_db()
        cursor = Fanc_Get_Data.connection.cursor()
        try:
            sqlCommands = sql.split(';')

            for command in sqlCommands:
                try:
                    if command.strip() != '':
                        cursor.execute(command)
                        
                        # Check if the query produces a result set before fetching
                        if cursor.description is not None:
                            result = cursor.fetchall()
                            result = "O.K"
                            #print("Result:", result)
                except mysql.connector.Error as msg:
                    Fanc.PrintFile("Command skipped:" + str(msg),"/EventFile.ini")
                    print("Command skipped:", msg)
                    Fanc.PrintFile("Error in command: " + command,"/EventFile.ini")
                    print("Error in command:", command)

            # Commit the changes if the stored procedure modifies data in the database
            # Fanc_Get_Data.connection.commit()

        finally:
            cursor.close()
    @staticmethod
    def run_stored_procedure_with_parameters(procedure_name, params):
        if Fanc_Get_Data.connection is None:
            Fanc_Get_Data.connect_to_db()
        cursor = Fanc_Get_Data.connection.cursor()

        # Call the stored procedure
        try:
            cursor.callproc(procedure_name, params)  # Pass parameters as a tuple
            # Commit the transaction
            Fanc_Get_Data.connection.commit()
        except mysql.connector.Error as msg:
            Fanc.PrintFile("run_stored_procedure_with_parameters error: " + str(msg), "/EventFile.ini")
            print("Command skipped:", msg)
        finally:
            cursor.close()
        print("Stored procedure executed successfully!")



    @staticmethod
    def sql_get_tables(sql):
        tables = None  # Initialize tables outside the try block
        if Fanc_Get_Data.connection is None:
            Fanc_Get_Data.connect_to_db()
        cursor = Fanc_Get_Data.connection.cursor()
        try:                     
            # Execute SQL script
            cursor.execute(sql)

            # Fetch all tables
            tables = cursor.fetchall()

            # Close the cursor, but keep the connection open for later use
            cursor.close()
        except mysql.connector.Error as msg:
            Fanc.PrintFile("Command skipped:" + str(msg),"/EventFile.ini")
            print("Command skipped:", msg)
            Fanc.PrintFile("Error in command:" + sql,"/EventFile.ini")
            print("Error in command:", sql)
        return tables

    @staticmethod
    def sql_get_dataset(sql):
        dataset = None  # Initialize dataset outside the try block
        if Fanc_Get_Data.connection is None:
            Fanc_Get_Data.connect_to_db()
        cursor = Fanc_Get_Data.connection.cursor()
        try:                     
            # Execute SQL script
            cursor.execute(sql)

            # Fetch all rows from the cursor
            rows = cursor.fetchall()

            # Get column names
            columns = [desc[0] for desc in cursor.description]

            # Organize into a dataset
            dataset = {'columns': columns, 'data': rows}

            # Close the cursor, but keep the connection open for later use
            cursor.close()
        except mysql.connector.Error as msg:
            Fanc.PrintFile("Command skipped:" + str(msg), "/EventFile.ini")
            print("Command skipped:", msg)
            Fanc.PrintFile("Error in command:" + sql, "/EventFile.ini")
            print("Error in command:", sql)
        return dataset