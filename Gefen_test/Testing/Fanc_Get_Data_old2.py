import mysql.connector

class Fanc_Get_Data1:

    def Run_sql_script(sql):
        try:
            cnx = mysql.connector.connect(
                host="enova-prod-main.cc1atg19czgb.eu-central-1.rds.amazonaws.com",
                user="admin",
                password="JdAA78!fjGjkasdDF8",
                database="Electrical_Power",
                port=3308
            )

            with cnx.cursor() as cursor:
                sqlCommands = sql.split(';')

                for command in sqlCommands:
                    try:
                        if command.strip() != '':
                            cursor.execute(command)
                            # Fetch results if it's a SELECT statement
                            if command.upper().startswith("SELECT"):
                                result = cursor.fetchall()
                                # Process the result if needed
                    except mysql.connector.Error as msg:
                        print("Command skipped:", msg)
                        print("Error in command:", command)

            cnx.commit()

        except mysql.connector.Error as err:
            print("MySQL error:", err)

        finally:
            if 'cnx' in locals() and cnx.is_connected():
                cnx.close()



