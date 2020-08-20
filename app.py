from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('nMhQsKWH9zJ9WhQ+sUGDdypr5AqmBx7oVQ7vpdc/NppuHQwzI6Loa+BGzJJVVHQtZqh+7zpbBPI44XXMkDj9alRpAnxV8tNSSC757skZnAahSG/1ioJnznlLBbH4a3PtsCsc0Rs7dYETbHRNZtLxcgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('77db789913d280b1c3393735c3498f1e')

# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "123":
        message = TextSendMessage(text="你好呀~~")
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='http://0.tcp.ngrok.io:10921/homepage/img/encryption.png', preview_image_url='http://0.tcp.ngrok.io:10921/homepage/img/encryption.png'))
    else:
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url='http://0.tcp.ngrok.io:10921/homepage/img/encryption.png', preview_image_url='http://0.tcp.ngrok.io:10921/homepage/img/encryption.png'))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
