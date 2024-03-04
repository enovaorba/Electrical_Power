import paramiko

def sftp_list_files(private_key_path, password, username, hostname, remote_directory, port=22):
    try:
        # Create a new SSH client object
        ssh = paramiko.SSHClient()

        # Automatically add the server's RSA key to the list of known hosts
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key for SSH key authentication
        private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

        # Connect to the SSH server using both private key and password
        ssh.connect(hostname, port, username, pkey=private_key, password=password)

        print("SSH connection established successfully!")

        # Create an SFTP client
        sftp = ssh.open_sftp()

        # Change directory to the specified remote directory
        sftp.chdir(remote_directory)

        # List files in the remote directory
        files = sftp.listdir()

        print(f"Files in directory '{remote_directory}':")
        for file in files:
            print(file)

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
remote_directory = '/External Users BeforeScan/'
port = 22

sftp_list_files(private_key_path, password, username, hostname, remote_directory, port)
