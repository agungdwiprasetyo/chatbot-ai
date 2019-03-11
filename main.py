#!/usr/bin/env python3

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import sys

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib import parse
import json

chatbot = ChatBot("bot")
chatbot.set_trainer(ListTrainer)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = dict(parse.parse_qsl(parse.urlsplit(self.path).query))

        try:
            bot_response = chatbot.get_response(parsed["input"])
            output = str(bot_response)
        except:
            output = "Mohon coba lagi"

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            'output': output
        }).encode())
        return

if __name__ == '__main__':
    server = HTTPServer(('localhost', 4141), RequestHandler)
    print('Starting server at http://localhost:4141')
    server.serve_forever()