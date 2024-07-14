#! /bin/bash

# Keeping the system going
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install prometheus-node-exporter

pip3 install gradio transformers torch promethesus-client

