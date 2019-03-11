#!/usr/bin/env python3

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

chatbot = ChatBot("bot")
chatbot.set_trainer(ListTrainer)

root_directory = os.path.dirname(__file__)

# train english language
file_name = os.path.join(root_directory, "core/datasets/english")
for file in os.listdir(file_name):
    data = open(file_name+"/"+file , "r").readlines()
    chatbot.train(data)

# train indonesian language
file_name = os.path.join(root_directory, "core/datasets/indonesian")
for file in os.listdir(file_name):
    data = open(file_name+"/"+file , "r").readlines()
    chatbot.train(data)