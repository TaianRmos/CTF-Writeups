# Solution to Baby Morse

This challenge is very straightforward and can be done in a minute !

The subject is quite clear: "Say FLAG and you'll get it." (translated in english).

Start the docker, open a second terminal and do `nc localhost 4000` to connect to the machine.

When you connect to it, you get a morse string: `--.- ..- . ...- --- ..- .-.. . --.. ...- --- ..- ...`.

Get the first online converter you want, you'll get the result "quevoulezvous", which means "what do you want" in french.

Using an online converter, convert "FLAG" in morse, you'll get the result `..-. .-.. .- --.`.

Send it back to the server and get your Flag: `FCSC{de8b4af784cd394ecc305979ffa124a112a18046037b42c94e4e85216180847e}`