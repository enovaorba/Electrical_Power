import mysql.connector

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
    def execute_sql_script(sql):
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
                    print("Command skipped:", msg)
                    print("Error in command:", command)

            # Commit the changes if the stored procedure modifies data in the database
            # Fanc_Get_Data.connection.commit()

        finally:
            cursor.close()
