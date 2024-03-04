import pexpect

def sftp_upload(private_key_path, password, username, hostname, local_file_path, remote_file_path):
    try:
        # Define the sftp command
        command = f'sftp -i {private_key_path} {username}@{hostname}'

        # Spawn a process
        child = pexpect.spawn(command, timeout=60)

        # Log interactions
        child.logfile = open("sftp_log.txt", "wb")

        # Expect password prompt
        index = child.expect(['password:', '(?i)password for .*'])
        if index == 0 or index == 1:
            # Send password
            child.sendline(password)
        else:
            print("Unexpected prompt:", child.before.decode())
            raise RuntimeError("Unexpected prompt encountered")

        # Expect sftp prompt
        child.expect('sftp>')

        # Execute sftp commands
        child.sendline(f'put {local_file_path} "{remote_file_path}"')

        # Wait for the command to complete
        child.expect('sftp>')

        # Print the output
        print(child.before.decode())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the child process
        child.close()

# Example usage:
private_key_path = '/home/avi/scripts_python/Gefen/gefenssh.key'
password = 'le3srqnJ'
username = 'nofrn#inova'
hostname = 'snoga.noga-iso.co.il'
local_file_path = '/home/avi/scripts_python/Gefen/testsftp.txt'
remote_file_path = '/External Users BeforeScan/testsftp.txt'

sftp_upload(private_key_path, password, username, hostname, local_file_path, remote_file_path)
