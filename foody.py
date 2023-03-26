from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from scraper import IFoodie

app = Flask(__name__)

line_bot_api = LineBotApi('WzrDyNZbVIr+FjgQ6wAGp4NGnpD0WpNLAs/S3/8ARjR7M87NqY9YEDNCx1QvLJZcX/55R2s+Xfe36hCxCA1f4615+M5wt0EDJkqqss16cNTvbjM9TLniUcvS+m5MWKNW0C9ZxJHxgVp3eAsnodBQHwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3fce18129b68e225fc6974ac6e807cb5')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message1(event):
    food = IFoodie(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=food.scrape()))


if __name__ == "__main__":
    app.run()

