# Solution to À l'aise

## What is a Vigenere Cypher ?

This challenge is a standard Vigenere cypher. It is very similar to a Cesar cypher, where you shift all the letters of the alphabet by a certain amount (A becomes B, B bcomes C etc...), but instead of using a standard shift, you're gonna use a key of a certain size and shift each letter according to the key. Here's an example:

| H | E | L | L | O | T | H | E | R | E |
|---|---|---|---|---|---|---|---|---|---|
| K | E | Y | K | E | Y | K | E | Y | K |
| R | I | J | V | S | R | R | I | P | O |

Here's how to implement it using maths:

Encryption: $(message + key) % 26$

Decryption: $(message - key + 26) % 26$

## Solution to the challenge

I decided to implement a full algorithm, with encryption and decryption (because why not ?) and checking for lowercase and uppercase for the message and the key if I ever want to use this tool again in a different situation.

After running the program, here's the result:
```
Bonjour cher agent ! Votre prochaine mission, si vous l'acceptez bien sur, sera d'infiltrer le reseau souterrain ou se cache nos ennemis. Rendez-vous a Nantes le 29 avril pour le debut de votre mission.
```

For non-French speakers, here's the translation in English:

```
Hello dear agent! Your next mission, if you accept it of course, will be to infiltrate the underground network where our enemies are hiding. See you in Nantes on April 29 for the start of your mission.
```

We know that the flag is the city mentioned in the message, so we can deduce that the flag is `Nantes` !