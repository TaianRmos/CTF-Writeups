# Solution to A l'envers

This one is quite simple for the concept: look at the string you receive, reverse it and send it back !

But of course, if you want to do it manually, it's gonna be painful , so let's try to do it with Python !

I used the `socket` module but `pwntools` is prettier, I just didn't take the time to learn how to use it (yet).

First step is to open a terminal and start the docker. Then, we create our socket and connect to the right address and port (localhost, 4000).

Now, we have to receive the data it gives us, extract the message, reverse the message and send it back !

You can do this using the functions `recv()` and `send()` or `sendall()`. Once you don't find *"continue"* in your answer, it means you got to the end and you can print the flag !

`FCSC{7b20416c4f019ea4486e1e5c13d2d1667eebac732268b46268a9b64035ab294d}`