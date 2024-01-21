import socket
#getting the host name and ip address of a local machine
name = socket.gethostname()
print(f'Hostname of local machine is {name}')
ip_addr = socket.gethostbyname(name)
print(f'IP address of {name} is {ip_addr}')


#getting the host name and ip address of a remote machine
remote_host = 'www.python.org'
ip_addr = socket.gethostbyname(remote_host)
print(f'IP address of {remote_host} is {ip_addr}')