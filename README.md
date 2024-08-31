# PDP-Bot
This repository contains the code for a Telegram Bot that predicts plant diseases by analyzing images of plant leaves. The bot uses a Convolutional Neural Network (CNN) model that was trained to detect whether a plant is healthy or suffering from a disease. If the plant is healthy, the bot informs the user. If the plant is unhealthy, the bot identifies the disease and provides essential information and solutions. <br/>
<br/>

## Features
* Plant Health Detection: Upload a picture of a plant leaf, and the bot will determine if the plant is healthy or not using a trained CNN model.
* Disease Identification: If the plant is unhealthy, the bot identifies the specific disease affecting the plant.
* Solution Suggestions: The bot provides information about the disease and suggests ways to address the problem.
* Language Translation: The bot can translate information between English and Azerbaijani using the EasyGoogleTranslate module.
* AI Integration: Utilizes the google.generativeai palm module for enhanced AI capabilities. <br/>
<br/>

## Project Structure
* main.py: The main script to run the Telegram bot.
* config.py: Stores the API keys and token required for the Gemini API and Telegram bot, managed using the config module.
* cnn_model.h5: The pre-trained CNN model used for predicting plant diseases.
* class_indices.json: Json file that includes all the plants that trained 
* requirements.txt: A list of all necessary Python packages for the project. <br/>
<br/>

## 
