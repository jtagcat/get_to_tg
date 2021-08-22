# get_to_tg
GET request with paramaters to Telegram message. No brains included, no gurantees.

## Github Actions Docker image
```sh
docker pull ghcr.io/jtagcat/get_to_tg:1
```

 - `GTT_BOT_TOKEN` is a required environment variable, you can get it from [@botfather](https://t.me/botfather).
 - The container will listen on port `8000`.

## Usage
`/<chat_id>/?message=[message]`
`/<chat_id>/?content=[message]`

The bot must be in the chat already. In the case of direct messages, the user must open the chat.

## Live instance
[@jtagcatbot](https://t.me/jtagcatbot)

```sh
curl https://gtt.c7.ee/0118999/?message=Hello
```

Replace `0118999` with your account id. You can get your account id from [@get_id_bot](https://t.me/get_id_bot).
