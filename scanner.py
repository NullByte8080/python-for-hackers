#!usr/bin/python3

import nmap

scanner = nmap.PortScanner()
print("Welcone to the webby's port scanner")
print("-----------------------------------")

ip_address= input("enter the target ip address:")
print("Your entered IP Adress is:", ip_address)
type(ip_address)

responce = input("""\n Enter Type Of Scan You Want To Run
                    1)SYN ACK SCAN
                    2)UDP SCAN
                    3)COMPREHNSIVE SCAN\n""")

print("you enter choice is:", responce)
if responce == '1':
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v', '-sS')
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_address].state())
    print(scannner[ip_address].all_protocols())
    print("open port",scanner[ip_address]['tcp'].keys())

elif responce == '2':
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v', '-sU')
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("open port", scanner[ip_address]['udp'].keys())

elif responce == '3':
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip_address, '1-65535', '-v -sS -sV -O -A')
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("open port", scanner[ip_address]['tcp'].keys())

elif responce == '4':
    print("please enter a valid option")