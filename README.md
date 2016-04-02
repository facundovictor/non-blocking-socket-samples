### Socket server/client samples

The ***first goal*** is to show an example of a service, using **non-blocking tcp sockets**. :+1:

```
non_blocking_service.py
```

Also, for completeness and comparation, there is an example of a service using **blocking tcp sockets**:

```
blocking_socket.py
```

And a **connectionless server/client** example:

```
connectionless_service.py
connectionless_client.py
```

#### How to use them:
1- Download it:

```
git clone --depth=1 https://github.com/facundovictor/non-blocking-socket-samples.git
```

2- Execute the example with python, as an example:

```
python non_blocking_service.py
```
