import re, subprocess, struct, socks, socket

# pip3 install pwntools
from pwn import process, remote, context

open('flag.txt', 'w').write('picoCTF{TEST_FLAG_FOR_LOCAL_MACHINE}\n')

def get_flag(p):
	content = p.readall()
	print(content)
	return re.search(b'picoCTF\{\w+\}', content).group().decode()


if 'remote':
	# nc 192.168.2.99 PORT
	# Source https://docs.pwntools.com/en/stable/context.html,
	# retrieved Sep 4, 2022
	context.proxy = (socks.SOCKS5, 'localhost', 8123)
	p = remote('192.168.2.99', '53932')
	# Send EOF to the server, but continue receiving data
	# Source https://docs.python.org/3/howto/sockets.html,
	# retrieved Sep 5, 2022
	p.sock.shutdown(socket.SHUT_WR)
	flag = get_flag(p)
	p.close()
	print(flag)

