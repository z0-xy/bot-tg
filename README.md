# Docker bot-tg
Telegram bot translitetare full name from cyrillic to latin to the norm of MFA.

 <img src='tg.jpeg'>

First, go to [@BotFather](https://t.me/botfather) and get TOKEN from your new bot and then add it to dockerfile.

Run the following command in terminal to build and run docker:

```
docker build -t bot .
docker run -d -p 80:80 bot
```


