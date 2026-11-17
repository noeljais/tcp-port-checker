# TCP Port Checker

A simple Python-based command-line tool that checks whether a TCP port is open or closed on a specified IPv4 address.

## Features

- Accepts an IPv4 address and TCP port number
- Checks TCP connectivity using Python sockets
- Identifies successful and unsuccessful connections
- Uses a 2-second connection timeout
- Validates IPv4 addresses and port numbers
- Handles invalid input and connection errors

## Technologies Used

- Python 3
- Python `socket` module
- Python `ipaddress` module

## How to Run

1. Clone the repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python port_checker.py
```

4. Enter the IPv4 address and port number.

## Example

**Input:**

```text
Enter IP Address: 127.0.0.1
Enter Port Number: 8000
```

**Output when a server is listening:**

```text
Port 8000 is OPEN
```

**Output when the connection fails:**

```text
Port 8000 is CLOSED or UNREACHABLE
```

## How It Works

The program creates an IPv4 TCP socket using Python's `socket` module and attempts to connect to the specified IP address and port.

If the connection succeeds, the port is reported as open. If the connection fails, the program reports that the port is closed or unreachable.

The program uses a connection timeout to avoid waiting too long and validates user input before attempting the connection.

## Learning Outcomes

- Understanding TCP ports and network services
- Creating TCP sockets in Python
- Attempting TCP connections
- Understanding connection success and failure
- Using connection timeouts
- Input validation and exception handling

## Limitations

- Supports IPv4 addresses only
- Checks one TCP port at a time
- Cannot always distinguish a closed port from a blocked or unreachable port
- Intended for localhost and authorized systems only

## Future Improvements

- Check multiple ports
- Display common service names
- Improve connection error reporting