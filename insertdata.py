import datetime
import os
from ftplib import FTP
import glob
import fnmatch
from Fanc import Fanc
import pymysql
import time
from time import gmtime, strftime, timezone

def InsrtFileDataToDB(local_file_path,mysql_table):

    # MySQL credentials
    mysql_host = 'future-main.cjpskwpmheoa.eu-central-1.rds.amazonaws.com'
    mysql_user = 'admin'
    mysql_password = 'Fdsf57yjngDSDdFDSsa8sd'
    mysql_database = 'maindb'
    # mysql_table = 'Tr69_Inventory_Daily_report'
    mysql_port = 3308

    # Connect to MySQL database
    db = pymysql.connect(host=mysql_host, user=mysql_user, password=mysql_password, db=mysql_database, port=mysql_port)
    cursor = db.cursor()

    # Read and insert data into MySQL
    with open(local_file_path, 'r') as file:
        lines = file.readlines()
        column_names = lines[0].strip().split(';')  # Extract column names from the first line
        column_names[0] = 'ID'
        column_names[1] = 'Serial'
        column_names[2] = 'Created'
        column_names[3] = 'Updated'
        column_names[4] = 'Manufacturer'
        column_names[5] = 'Model_name'
        column_names[6] = 'Firmware'
        column_names[7] = 'MAC_Address'
        column_names[8] = 'Host_MAC_Addresses'

    data_rows = []
    for line in lines[1:]:
        line = line.strip()
        if line and line != '8: \'\'':
            data = line.split(';')
            data = data[:9]  # Limit the data to the number of columns
            created = datetime.datetime.strptime(data[2].strip('""'), "%m/%d/%Y %I:%M:%S %p")
            updated = datetime.datetime.strptime(data[3].strip('""'), "%m/%d/%Y %I:%M:%S %p")
            data[2] = created.strftime("%Y-%m-%d %H:%M:%S")
            data[3] = updated.strftime("%Y-%m-%d %H:%M:%S")
            data = [field.strip('""') for field in data]
            data_rows.append(data)
            
            # Limit Host_MAC_Addresses to 1024 characters
            host_mac_addresses = data[8][:1024] if len(data) > 8 else ''
            data[8] = host_mac_addresses

# TRUNCATE table
    query = 'TRUNCATE table  ' + mysql_table + '_Temp'
    cursor.execute(query)
    db.commit()


# Generate the block insert query
    column_names_with_backticks = ['`{}`'.format(name) for name in column_names]
    query = "INSERT INTO {} ({}) VALUES ({})".format(mysql_table + '_Temp', ', '.join(column_names_with_backticks), ', '.join(['%s'] * len(column_names)))
    cursor.executemany(query, data_rows)
    db.commit()
    
# switch_tables
    procedure_call = "CALL {}('{}', '{}')".format('switch_tables', mysql_table, mysql_table + '_Temp')
    cursor.execute(procedure_call)
    db.commit()


def download_ftp_file(hostname, username, password, port, directory, local_file_name):
    try:
        ftp = FTP()
        ftp.connect(hostname, port)
        ftp.login(user=username, passwd=password)

    # Change to the remote directory (root directory)
        ftp.cwd('/')

    # List files in the current directory
        file_list = ftp.nlst()

    # Construct the pattern for matching files
        file_pattern = 'Report(Inventory_Daily_report_Futurenet_*'

    # Find all files in the directory matching the pattern
        matching_files = [filename for filename in file_list if fnmatch.fnmatch(filename, file_pattern)]

    # Sort the files by modification time
        matching_files.sort(key=lambda f: ftp.sendcmd('MDTM ' + f).split()[1])

        if matching_files:
             # Get the last modified file
            last_modified_file = matching_files[-1]
            if local_file_name != last_modified_file:
                print("Last modified file:", last_modified_file)
                Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " Last modified file:" + last_modified_file ,directory +    'EventFile.ini')
                # Get a list of all files in the directory
                file_list = os.listdir(directory + 'files/')

                # Iterate over the file list and delete each file
                for file_name in file_list:
                    file_path = os.path.join(directory + 'files/', file_name)
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                    Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " Deleted file: {file_path}" ,directory +    'EventFile.ini')
           
                local_filename = directory + 'files/' + last_modified_file
                with open(local_filename, 'wb') as file:
                    ftp.retrbinary('RETR ' + last_modified_file, file.write)
                    print("File downloaded successfully!")
                    Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " File downloaded successfully!" ,directory +    'EventFile.ini')
                    ftp.quit()
                    return local_filename
        else:
            Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " No Have File" ,directory +    'EventFile.ini')
            print("NO Have New File.")
            ftp.quit()
            return 0

    # Close the FTP connection
        Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " No Have New File" ,directory +    'EventFile.ini')
        print("NO Have New File.")
        ftp.quit()
        return 0
    except Exception as e:
        print("An error occurred:", str(e))
        Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " an error occurred:", str(e) ,directory +    'EventFile.ini')
        return 0
        
# FTP server details
ftp_hostname = '135.181.209.211'
ftp_username = 'futurenet'
ftp_password = 'future@123#'
ftp_port = 60000

# List all files in the directory
directory = '/home/future_scripts/frendly_daily_repot/'
file_list = os.listdir(directory + 'files/')

# Iterate over the file list and print each file name
local_file_name=''
for file_name in file_list:
    local_file_name=file_name
if local_file_name == '':
    local_file_name = 'XXX'

# Download the file
local_file_path=download_ftp_file(ftp_hostname, ftp_username, ftp_password, ftp_port, directory, local_file_name)
# InsrtFileDataToDB
if local_file_path != 0:
    InsrtFileDataToDB(local_file_path,'Tr69_Inventory_Daily_report')
    Fanc.PrintFile(strftime("%Y-%m-%d %H:%M:%S", time.localtime())  + " Insert Data successfully!" ,directory +    'EventFile.ini')
    