# `get_to_tg`
**archived: provided sending messages without a bot token, but this has been abused; [Telegram API](https://core.telegram.org/bots/api#sendmessage) supports POST messaging.**

GET request with paramaters to Telegram message. No brains included, no gurantees.

## Github Actions Docker image
```sh
docker pull ghcr.io/jtagcat/get_to_tg:1
```

 - `GTT_BOT_TOKEN` is a required environment variable, you can get it from [@botfather](https://t.me/botfather).
 - The container will listen on port `8000`.

## Usage
 - `/<chat_id>/?message=[message]`
 - `/<chat_id>/?content=[message]`

The bot must be in the chat already. In the case of direct messages, the user must open the chat.

By the nature of no authentication, anyone can send messages to all chats the bot participates in, provided they have the chat id.

## Live instance
[@jtagcatbot](https://t.me/jtagcatbot)

```sh
curl https://gtt.c7.ee/0118999/?message=Hello
```

Replace `0118999` with your account id. You can get your account id from [@get_id_bot](https://t.me/get_id_bot).

***

`get_to_tg` is a valid endpoint for [Binary Eye](https://github.com/markusfisch/BinaryEye).
