import os
import pandas as pd
import sqlite3
import xml.etree.ElementTree as ET
from Fanc_Get_Data import Fanc_Get_Data
import pytz
from datetime import datetime, timedelta
from Fanc import Fanc

class FancOutputFiles:
    directory = os.getcwd()
    def save_tables(tables, csv_file, xml_file):
        # Separate tables
        table1_data = tables[:len(tables)//2]
        table2_data = tables[len(tables)//2:]

        # Create DataFrames for each table
        table1_df = pd.DataFrame(table1_data, columns=['Timestamp', 'Value'])
        table2_df = pd.DataFrame(table2_data, columns=['Timestamp', 'Value'])

        # Save as CSV
        csv_filename = os.path.join(FancOutputFiles.directory, f"{csv_file}.csv")
        with open(csv_filename, 'w') as file:
            file.write("Consdomestic\n")
            table1_df.to_csv(file, index=False)
            
            # Add a newline between tables
            file.write("\nConsgeneral\n")
            table2_df.to_csv(file, index=False)
        print(f"CSV file saved: {csv_filename}")


        # Save as XML
        root = ET.Element("tables")
        for i, table in enumerate(tables):
            if (i == 0):
                table_name = "Consdomestic"
            else:
                table_name = "Consgeneral"
            table_element = ET.SubElement(root, table_name)
            for _, row in pd.DataFrame(table).iterrows():
                record = ET.SubElement(table_element, "Time value")
                for col_name, value in row.items():
                    ET.SubElement(record, str(col_name)).text = str(value)

        xml_filename = os.path.join(FancOutputFiles.directory, f"{xml_file}")
        tree = ET.ElementTree(root)
        tree.write(xml_filename)
        print(f"XML file saved: {xml_filename}")

    # Example usage
    def run_sql_script_and_save(sql_script_file, csv_file, xml_file):
      
        with open(sql_script_file, 'r') as f:
            sql_script = f.read()
        tables = Fanc_Get_Data.sql_get_tables(sql_script)
        # Save tables to CSV and XML
        FancOutputFiles.save_tables(tables, csv_file, xml_file)
        # Close the connection
        #conn.close()


    def create_feport_files():    
        israel_timezone = pytz.timezone('Asia/Jerusalem')
        date_ = datetime.now(israel_timezone).strftime('%Y%m%d')

        # Get the current date
        current_date = datetime.now()
        # Extract the day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
        day_of_week = current_date.weekday()
        sql=""
        #  the day of the week as an integer, where Monday is 0
        if day_of_week == 6:
            sql="Repot-1.sql"
        elif day_of_week == 0:
            sql="Repot-2.sql"
        elif day_of_week == 1:
            sql="Repot-3.sql"
        elif day_of_week == 2:
            sql="Repot-4.sql"
        elif day_of_week == 3:
            sql="Repot-5.sql"

        sql="Repot-4.sql"
        if sql != "":
            sql_script_file = FancOutputFiles.directory + "/SQL/" + sql   
            csv_file = FancOutputFiles.directory + "/send_report_csv/SUPPNAMEN_Day_supplyplan_" + date_ + "_CreateDate_CreateTime.csv_csv"
            xml_file = FancOutputFiles.directory + "/send_report_xml/SUPPNAMEN_Day_supplyplan_" + date_ + "_CreateDate_CreateTime.xml_xml"
            FancOutputFiles.run_sql_script_and_save(sql_script_file, csv_file, xml_file)
            Fanc.PrintFile("create_feport_files" ,"/EventFile.ini")

FancOutputFiles.create_feport_files()