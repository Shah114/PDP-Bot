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

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shah114/plant-disease-prediction-bot.git
   cd plant-disease-prediction-bot
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the configuration: <br/>
   Replace the placeholders in config.py with your Gemini API key and Telegram bot token.
4. Run the bot:
   ```bash
   python main.py
   ```
<br/>

## Usage
* Start the bot on Telegram: Open your Telegram app, find your bot, and start a chat.
* Send a plant leaf image: The bot will analyze the image using the CNN model and respond with the health status of the plant.
* Receive disease information: If the plant is diseased, the bot will provide the name of the disease and how to solve the issue. <br/>
<br/>

## Technologies Used
* Python: The primary programming language for the bot.
* Telegram Bot API: Used to create and manage the Telegram bot.
* Gemini API: Analyzes the plant leaf images.
* EasyGoogleTranslate: For language translation between English and Azerbaijani.
* google.generativeai palm: For AI functionalities.
* CNN Model: Pre-trained model for predicting plant diseases. <br/>
<br/>

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.
