#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging

from flask import Flask, request

# Enable logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def tg_handler():
    content = request.get_json()
    try:
        logger.info("post json == > {}".format(content))
        from msg_handler import alert_msg_handler
        for alert_json in content['alerts']:
            transform_msg = alert_msg_handler(alert_json)
            print(transform_msg)
    except:
        logger.error("parse error ==> {}".format(content))
    return 'ok'

if __name__ == "__main__":
    # Running server
    app.run(host='0.0.0.0', port=9166)