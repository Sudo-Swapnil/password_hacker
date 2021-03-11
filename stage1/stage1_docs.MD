This stage contains simple implementation of a client side socket. 
It takes the server's ip and port number as input and forms a connection using socket module.
Finally, it passes the data entered as the last input to the server and prints the response received from the server.

The algorithm is the following:

1. Create a new socket.
2. Connect to a host and a port using the socket.
3. Send a message from the third command line argument to the host using the socket.
4. Receive the server’s response.
5. Print the server’s response.
6. Close the socket.

Inputs:
Program takes inputs from command line interface in this order:

1. IP address
2. port
3. message for sending