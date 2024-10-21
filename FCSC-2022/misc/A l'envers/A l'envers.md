# A l'envers

<pre>
Difficulty: Intro
</pre>

Connectez-vous au service distant et pour chaque chaîne de caractères reçue, vous devez renvoyer la chaîne de caractères contenant les caractères dans l’ordre inverse.

Exemple : pour la chaîne ANSSI, vous devez renvoyer ISSNA (note : le respect de la casse est important).

**Instruction**

1. Pour commencer, téléchargez le fichier docker-compose.yml :

`curl https://hackropole.fr/challenges/fcsc2022-misc-a-l-envers/docker-compose.public.yml -o docker-compose.yml`

*The download didn't work for me via curl so I just downloaded the file manually and openend a terminal in the directory*

2. Lancez l'épreuve en exécutant dans le même dossier :

`docker compose up`

3. Dans un second terminal, accédez à l'épreuve via Netcat avec :

`nc localhost 4000`