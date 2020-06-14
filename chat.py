import socket
import threading
import random
from tkinter import * 
from tkinter import ttk  
from tkinter import scrolledtext

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))
server = '192.168.56.1', 9090
abcde = []




# while True:
# 	base = str(input("Have you checked-in? (y/n)"))
# 	if base == "n":
# 		sock.sendto(base.encode('utf-8'), server)
# 		name = str(input('Your new nickname: '))
# 		sock.sendto(name.encode('utf-8'), server)
# 		data1 = sock.recv(1024)
# 		print(data1)
# 		if data1.decode('utf-8') == "NO":
# 			print('This nick is occupied or not real. Try again, please')
# 			continue;
# 		else:
# 			passw == str(input("Your new password: "))
# 			sock.sendto(passw.encode('utf-8'), server)
# 			print(f'All right. Welcome to AllChat, {name}')
# 			break
# 	else:
# 		sock.sendto(base.encode('utf-8'), server)
# 		name = str(input('Your old nickname: '))
# 		sock.sendto(name.encode('utf-8'), server)
# 		data1 = sock.recv(1024)
# 		if data.decode('utf-8') == "NO":
# 			print('This nick is occupied or not real. Try again, please')
# 			continue;
# 		else:
# 			passw == str(input("Your old password: "))
# 			sock.sendto(passw.encode('utf-8'), server)
# 			data3 = sock.recv(1024)
# 			if data3.decode('utf-8') == "OK":
# 				print(f'All right. Welcome to AllChat, {name}')
# 				break
# 			else:
# 				print('Try again. Your password or nickname are incorrect...')
# 				continue;
def read():
	global conncode
	while True:
		try:
			data = sock.recv(1024)
			if not data:
				continue

			elif data.decode('utf-8').isdigit() == True:
				conncode = data.decode('utf-8')
			
			write.insert(INSERT, data.decode('utf-8') + "\n")
		except:
			print("Please reload AllChat")


def clear():
	slaves = window.pack_slaves()
	for i in slaves:
		i.destroy()

def clean():
	write.delete(1.0, END)

def send():
	global ms
	global nick
	msg = ms.get()
	global conncode
	if conncode == 0:
		sendu = "GETER"
		sock.sendto(sendu.encode('utf-8'), server)
	
	sending = f'{str(conncode)}:[{nick}] '+ msg
	sender = sending[::-1]
	sock.sendto(sender.encode('utf-8'), server)
	

def click():
	global txt
	global ms
	global nick
	global conncode
	clear()
	ms = Entry(window, width=50)
	ms.focus()  
	ms.grid(column=0, row=10)
	btn1.configure(text = "Send!", command = send)  
	nick = txt.get()
	who = f'{str(conncode)}:{nick} connected to server!'[::-1]
	sock.sendto(who.encode('utf-8'), server)
		
def create():
	global conncode
	global txt
	global btn1
	global btn2
	global tab1
	conncode = 0
	clear()
	txt = Entry(window,width=50)
	txt.focus()  
	txt.grid(column=0, row=10)

	btn1.configure(text="Go!", command=click)
	btn2.configure(text='Clean!', command=clean)





def jojo():
	global conncode
	global jt
	global txt
	conncode = jt.get()
	clear()
	txt = Entry(window,width=50)
	txt.focus()  
	txt.grid(column=0, row=10)

	btn1.configure(text = "Go!", command=click)
	btn2.configure(text='Clean!',command=clean)


def join():
	global conncode
	global jt
	jt = Entry(window, width=50)
	jt.focus()  
	jt.grid(column=0, row=10)
	btn1.configure(text="Jump!", command=jojo)
	btn2.configure(text='Clean!',command=clean)


#LOL



tabs = []
window = Tk()  
window.title("AllChat")
# window.geometry('340x250')
global tab1
global tab2

write = scrolledtext.ScrolledText(window, width=40, height=10, font=("Helvetica", 11))
write.insert(INSERT, "AllChat v.0.0\n") 
write.insert(INSERT, "Do you want to create room or join?\n") 
write.grid(column=0, row=0)
# for i in abcde: 
# 	tab = ttk.Frame(tab_control)
# 	tab_control.add(tab, text=i)  
# 	tabs.append(tab)


# for t in tabs:
# 	write_ch = scrolledtext.ScrolledText(t, width=40, height=10, font=("Helvetica", 11))
# 	write_ch.insert(INSERT, "AllChat v.0.0\n") 
# 	write_ch.insert(INSERT, "Channel-window\n") 
# 	write_ch.grid(column=0, row=0)
global btn1
global btn2
btn1 = Button(window, text="Create", command=create, bg = "white")
btn1.grid(column=0, row=11)
btn2 = Button(window, text="Join", command=join, bg = "white")
btn2.grid(column=0, row=12)

some = threading.Thread(target=read)
some.start()



window.mainloop()
