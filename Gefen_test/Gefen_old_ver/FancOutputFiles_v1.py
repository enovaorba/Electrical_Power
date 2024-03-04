import os
import pandas as pd
import sqlite3
import xml.etree.ElementTree as ET
from Fanc_Get_Data import Fanc_Get_Data
import pytz
from datetime import datetime, timedelta
from Fanc import Fanc
import os
import pandas as pd
import csv
import xml.etree.ElementTree as ET

class FancOutputFiles_old:
    directory = os.getcwd()
    def save_tables(datasets, csv_file, xml_file):
        if isinstance(datasets, dict):
            datasets = [datasets]  # Convert single dictionary to a list containing that dictionary
        
        #print(datasets)
        
        # Save as CSV
        with open(csv_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for dataset in datasets:
                csv_writer.writerow(dataset['columns'])  # Write column headers
                for data_row in dataset['data']:
                    csv_writer.writerow([str(value) for value in data_row])  # Convert each value to string

        # Save as XML
        root = ET.Element("datasets")
        for index, dataset in enumerate(datasets):
            dataset_elem = ET.SubElement(root, f"dataset_{index+1}")
            
            columns = ET.SubElement(dataset_elem, "columns")
            for column in dataset['columns']:
                col = ET.SubElement(columns, "column")
                col.text = column
            
            data = ET.SubElement(dataset_elem, "data")
            for data_row in dataset['data']:
                entry = ET.SubElement(data, "entry")
                for value in data_row:
                    val = ET.SubElement(entry, "value")
                    val.text = str(value)
            
        tree = ET.ElementTree(root)
        tree.write(xml_file)

    # Example usage
    def run_sql_script_and_save(sql_script_file, csv_file, xml_file):
      
        with open(sql_script_file, 'r') as f:
            sql_script = f.read()
        #tables = Fanc_Get_Data.sql_get_tables(sql_script)
        dataset = Fanc_Get_Data.sql_get_dataset(sql_script)
        # Print the dataset
        #print(dataset)

        # Save tables to CSV and XML
        FancOutputFiles.save_tables(dataset, csv_file, xml_file)
        # Close the connection
        #conn.close()
    def GetDays_tomorrow_and_after(numbers_of_days):
            # Get tomorrow and the day after tomorrow
            tomorrow = datetime.now() + timedelta(days=1)
            day_after_tomorrow = datetime.now() + timedelta(days=numbers_of_days)

            # Format dates
            formatted_tomorrow = tomorrow.strftime("%Y%m%d")
            formatted_day_after_tomorrow = day_after_tomorrow.strftime("%Y%m%d")

            # Get current time
            current_time = datetime.now().strftime("%H%M%S")

            # Concatenate the strings
            return  formatted_tomorrow + "_" + formatted_day_after_tomorrow + "_" + current_time

    def create_feport_files():
        xml_file_name = ""  
        israel_timezone = pytz.timezone('Asia/Jerusalem')
        date_ = datetime.now(israel_timezone).strftime('%Y%m%d')
        xml_file = ""
        days_ = ""
        # Get the current date
        current_date = datetime.now()
        # Extract the day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
        day_of_week = current_date.weekday()
        sql=""
        #  the day of the week as an integer, where Monday is 0
        if day_of_week == 6:
            sql="Repot-1.sql"
            days_ = FancOutputFiles.GetDays_tomorrow_and_after(2)
        elif day_of_week == 0:
            sql="Repot-2.sql"
            days_ = FancOutputFiles.GetDays_tomorrow_and_after(2)
        elif day_of_week == 1:
            sql="Repot-3.sql"
            days_ = FancOutputFiles.GetDays_tomorrow_and_after(2)
        elif day_of_week == 2:
            sql="Repot-4.sql"
            days_ = FancOutputFiles.GetDays_tomorrow_and_after(10)
        elif day_of_week == 3:
            sql="Repot-5.sql"
            days_ = FancOutputFiles.GetDays_tomorrow_and_after(3)

        #sql="Repot-1.sql"
        if sql != "":
            sql_script_file = FancOutputFiles.directory + "/SQL/" + sql   
            csv_file_name = "NOFARN_Day_supplyplan_" + days_ + ".csv"
            csv_file = FancOutputFiles.directory + "/send_report_csv/" + csv_file_name
            #xml_file_name = "SUPPNAMEN_Day_supplyplan_" + date_ + "_CreateDate_CreateTime.xml_xml"
            xml_file_name = "NOFARN_Day_supplyplan_" + days_ + ".xml"
            xml_file = FancOutputFiles.directory + "/send_report_xml/" + xml_file_name
            FancOutputFiles.run_sql_script_and_save(sql_script_file, csv_file, xml_file)
            Fanc.PrintFile("create_feport_files" ,"/EventFile.ini")
        return xml_file_name
#FancOutputFiles.create_feport_files()
