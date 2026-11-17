import socket
import ipaddress

try:
    ip = input("Enter IP Address: ")
    ipaddress.IPv4Address(ip)
    port = int(input("Enter Port Number: "))

    if port < 1 or port > 65535:
        print("Invalid port! Enter a number between 1 and 65535.")
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        address = (ip, port)
        result = s.connect_ex(address)

        if result == 0:
            print("Port", port, "is OPEN")
        else:
            print("Port", port, "is CLOSED or UNREACHABLE")

        s.close()

except ValueError:
    print("Invalid input! Enter a valid IP address and port number.")

except (socket.timeout, OSError) as error:
    print("Connection error:", error)