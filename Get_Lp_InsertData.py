import mysql.connector
from datetime import datetime


# Data from the JSON
data = {
    'totalRecords': 3,
    'status': 'Success',
    'pageNr': 1,
    'meterList': [
        {
            'meterNumber': '73717004482',
            'lpList': [
                {
                    'transformer_U': 10.0,
                    'status': None,
                    'startOfInterval': '2023-11-18T21:00:00.000Z',
                    'recExportTime': '2023-11-19T16:36:40.000Z',
                    'reactiveIKVARH': 0.0,
                    'reactiveEKVARH': 0.0,
                    'lastRecordStatus': 1,
                    'endOfInternal': '2023-11-18T21:15:00.000Z',
                    'activeIKWH': 0.0,
                    'activeEKWH': 0.0
                }
            ]
        },
        {
            'meterNumber': '85306150909',
            'lpList': [
                {
                    'transformer_U': 20.0,
                    'status': None,
                    'startOfInterval': '2023-11-18T21:00:00.000Z',
                    'recExportTime': '2023-11-19T05:31:24.000Z',
                    'reactiveIKVARH': 14.75,
                    'reactiveEKVARH': 0.0,
                    'lastRecordStatus': 1,
                    'endOfInternal': '2023-11-18T21:15:00.000Z',
                    'activeIKWH': 57.75,
                    'activeEKWH': 0.0
                }
            ]
        },
        {
            'meterNumber': '86017000061',
            'lpList': [
                {
                    'transformer_U': 20.0,
                    'status': None,
                    'startOfInterval': '2023-11-18T21:00:00.000Z',
                    'recExportTime': '2023-11-19T05:31:24.000Z',
                    'reactiveIKVARH': 0.0,
                    'reactiveEKVARH': 6.34,
                    'lastRecordStatus': 1,
                    'endOfInternal': '2023-11-18T21:15:00.000Z',
                    'activeIKWH': 1.66,
                    'activeEKWH': 0.16
                }
            ]
        }
    ]
}

# Connect to MySQL
connection = mysql.connector.connect(
    host="enova-prod-main.cc1atg19czgb.eu-central-1.rds.amazonaws.com",
    user="admin",
    password="JdAA78!fjGjkasdDF8",
    database="stage_enova",
    port = 3308  
)

# Create a cursor
cursor = connection.cursor()

# Loop through meterList and lpList to insert data into the table
for meter in data['meterList']:
    meterNumber = meter['meterNumber']
    for lp in meter['lpList']:
        transformer_U = lp['transformer_U']
        startOfInterval = datetime.strptime(lp['startOfInterval'], '%Y-%m-%dT%H:%M:%S.%fZ')
        recExportTime = datetime.strptime(lp['recExportTime'], '%Y-%m-%dT%H:%M:%S.%fZ')
        reactiveIKVARH = lp['reactiveIKVARH']
        reactiveEKVARH = lp['reactiveEKVARH']
        lastRecordStatus = lp['lastRecordStatus']
        endOfInternal = datetime.strptime(lp['endOfInternal'], '%Y-%m-%dT%H:%M:%S.%fZ')
        activeIKWH = lp['activeIKWH']
        activeEKWH = lp['activeEKWH']

        # Insert data into the table
        query = "INSERT INTO electrical_power_SATEC_LP2 (meterNumber, transformer_U, startOfInterval, recExportTime, reactiveIKVARH, reactiveEKVARH, lastRecordStatus, endOfInternal, activeIKWH, activeEKWH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (meterNumber, transformer_U, startOfInterval, recExportTime, reactiveIKVARH, reactiveEKVARH, lastRecordStatus, endOfInternal, activeIKWH, activeEKWH)
        cursor.execute(query, values)

# Commit changes and close connections
connection.commit()
cursor.close()
connection.close()
