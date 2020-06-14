import socket
import random
import chatdata as cd
import threading

global chan_dict
chan_dict = {}


def chan_manage():
    global chan_dict
    while True:
        data,addres = sock.recvfrom(1024)
        chan_num = data.decode('utf-8')[0] + data.decode('utf-8')[1] + data.decode('utf-8')[2] + data.decode('utf-8')[3] + data.decode('utf-8')[4]
        if "[" not in data.decode('utf-8') and chan_dict.get(chan_num) != None:
            if addres not in chan_dict[chan_num]: 
                chan_dict[chan_num].append(addres)
            if "/all" in data.decode('utf-8')[::-1]:
                data = (f'{chan_num}: ' + str(len(chan_dict[chan_num])))[::-1].encode('utf-8')
            for chan in chan_dict[chan_num]:
                sock.sendto(data.encode('utf-8'), client)


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',9090))
conn_list = []
for i in range(10000, 100000):
    conn_list.append(i)

print ('-|Server-activated|-')
# while True:
#     data1 , addres1 = sock.recvfrom(1024)
#     print(data1.decode('utf-8'))
#     print ('Start Server')

#     if data1.decode('utf-8') == "n":
        
#         data2 = sock.recv(1024)
#         if cd.users.get(data2.decode('utf-8')) != None:
#             sock.sendto(b"NO", addres1)
#             print('send')
#             continue;
#         else:
#             sock.sendto(b"OK", addres1)
#             print('send')
#             data3 = sock.recv(1024)
#             cd.users[data2.decode('utf-8')] = data3.decode('utf-8')
#             print(f'{data2.decode("utf-8")} connected to server')
#             break;
#     else:
#         data2 = sock.recv(1024)
#         print(data2)
#         print("lloo")
#         if cd.users.get(data2.decode('utf-8')) == None:
#             sock.sendto(b"NO", addres1)
#             continue;
#         else:
#             sock.sendto(b"OK", addres1)
#             data3 = sock.recv(1024)
#             if cd.users[data2.decode('utf-8')] == data3.decode('utf-8'):
#                 sock.sendto(b"OK", addres1)
#                 print(f'{data2.decode("utf-8")} connected to server')
#                 break;
#             else:
#                 sock.sendto(b"NO", addres1)
#                 continue;



while True:
    data, addres = sock.recvfrom(1024)
    print (f'Sent msg {addres[0], addres[1]}')

    if data.decode('utf-8') == "GETER":
        conn_num = random.choice(conn_list)
        pol = str(conn_num).encode('utf-8')
        sock.sendto(pol, addres)
        print('-|Conn-number-sent|-')
        conn_list.remove(conn_num)

    lol = data.decode('utf-8')[::-1][0] + data.decode('utf-8')[::-1][1] + data.decode('utf-8')[::-1][2] + data.decode('utf-8')[::-1][3] + data.decode('utf-8')[::-1][4]
    if lol.isdigit() == True:
        if  addres not in cd.usercode[lol]: 
            cd.usercode[lol].append(addres)
        if "/all" in data.decode('utf-8')[::-1]:
            data = (f'{lol}:[Server] ' + str(len(cd.usercode[lol])))[::-1].encode('utf-8')

        for client in cd.usercode[lol]:
            sock.sendto(data.decode('utf-8')[::-1].encode('utf-8'), client)
            print("-||System-working-fine||-")




