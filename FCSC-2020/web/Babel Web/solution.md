# Solution to Babel Web

This challenge shows you some basic php vulnerabilities.

The first step is to download the docker file and to launch it using `docker compose up`. You can then access the website in local with url `http://localhost:8000/`.

## Finding the php code

When you get on the page, there's nothing really interesting.

When you open the web console (usually F12), you find a comment in the HTML code: `<!-- <a href="?source=1">source</a> -->`.

You can right click and edit the HTML code to get rid of the comment. You have now a clickable url that gets you to `http://localhost:8000/?source=1`.

You end up in front of the source code of the page, containing a first part with php code.

## Understanding the PHP code

The php we have looks like this:

```php
<?php
    if (isset($_GET['source'])) {
        @show_source(__FILE__);
    }  else if(isset($_GET['code'])) {
        print("<pre>");
        @system($_GET['code']);
        print("<pre>");
    } else {
?>
```

Let's break it down:
* If we have an argument "source", we show the current file
* If we have an argument "code", we execute the command given in argument
* Else we do nothing

The first part is exactly what we just did, we added the argument "source" by adding `?source=1` in the URL (the argument "source" is equal to 1).

But the second condition shows us that if we give a command, the php code will execute it !

## Exploiting the vulnerability

We can try to list all the files on server side by adding the argument `?code=ls` (we go to the URL `http://localhost:8000/?code=ls`).

We see that we have two files: `flag.php` and `index.php`.

We can finally add the argument `?code=cat flag.php` to read the document (we go to the URL `http://localhost:8000/?code=cat%20flat?php` with `%20` being interpreted as a space).

We end up on a blank page, but we have the flag in comment in the source code ! 

Flag: `FCSC{5d969396bb5592634b31d4f0846d945e4befbb8c470b055ef35c0ac090b9b8b7}`