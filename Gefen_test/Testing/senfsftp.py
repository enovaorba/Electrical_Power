import paramiko

def send_file_via_sftp(hostname, port, username, password, local_file_path, remote_file_path):
    try:
        # Connect to the SFTP server
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        
        # Upload the local file to the remote server
        sftp.put(local_file_path, remote_file_path)
        
        # Close the SFTP connection
        sftp.close()
        transport.close()
        
        print(f"File '{local_file_path}' successfully sent to '{remote_file_path}'.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
hostname = 'snoga.noga-iso.co.il'
port = 22
username = 'nofrn#inova'
password = ''
local_file_path = '/home/avi/scripts_python/Gefen/testsftp.txt'
remote_file_path = '/External Users BeforeScan/testsftp.txt'
private_key_path = '/home/avi/scripts_python/Gefen/gefenssh.key'

send_file_via_sftp(hostname, port, username, password, local_file_path, remote_file_path)
