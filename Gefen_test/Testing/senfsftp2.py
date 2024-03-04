import paramiko

def sftp_transfer(private_key_path, password, username, hostname, local_file_path, remote_file_path, port=22):
    try:
        # Create a new SSH client object
        ssh = paramiko.SSHClient()

        # Automatically add the server's RSA key to the list of known hosts
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key for SSH key authentication
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)




        # Connect to the SSH server using both private key and password
        ssh.connect(hostname, port, username,  password=password , pkey=private_key)

        print("SSH connection established successfully!")

        
        # Create an SFTP client
        sftp = ssh.open_sftp()

        # Upload the local file to the remote server
        sftp.put(local_file_path, remote_file_path)
        #sftp.get(wobble_file,local_file)
        print(f"File '{local_file_path}' successfully transferred to '{remote_file_path}'.")

        # Close the SFTP session and SSH connection
        sftp.close()
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")

# Example usage
private_key_path = '/home/avi/scripts_python/Gefen/gefenssh.key'
password = 'le3srqnJ'
username = 'nofrn#inova'
hostname = 'snoga.noga-iso.co.il'
local_file_path = '/home/avi/scripts_python/Gefen/testsftp.txt'  # Replace with the path to your local file
remote_file_path = '/External Users BeforeScan/testsftp.txt'
port = 22

sftp_transfer(private_key_path, password, username, hostname, local_file_path, remote_file_path, port)
