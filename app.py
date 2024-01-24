from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['LCoJB18nFcutgZ6TDqWwNGt8ezaRw6ME7juHsOYZ1fNLRKWoN8b1x0bVholiOAZGrfTZBEJ+v+NMwaqhbkGL1jPxg7pB2ClR1VhTS6K/DGpW7UBP5rlsxIp3HiDd1npvWm3zas2s13/m05An+TsdaAdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['2764afba007f3d253faa38658e598632'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
