# Import Dependencies
import os
import json
from PIL import Image
import numpy as np
import tensorflow as tf
import google.generativeai as palm
from io import BytesIO
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler, filters, 
                          CallbackContext, ConversationHandler)
from easygoogletranslate import EasyGoogleTranslate
import config

# Initialize Translators
translator_to_en = EasyGoogleTranslate(
    source_language='az',
    target_language='en',
    timeout=10)

translator_to_az = EasyGoogleTranslate(
    source_language='en',
    target_language='az',
    timeout=10)

# Load the model and class indices
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_model/pdp_model.h5"
model = tf.keras.models.load_model(model_path)

class_indices = json.load(open(f"{working_dir}/class_indices.json"))

# Google Generative AI API Key
palm.configure(api_key=config.api_key)

# Telegram Bot Token
application = ApplicationBuilder().token(config.bot_token).build()

# Conversation states
ASKING_IMAGE, PREDICT_IMAGE, HANDLE_IMAGE = range(3)

# Language preference (default is English)
language_preference = 'en'

# Function to load and preprocess the image using Pillow
def load_and_preprocess_image(image):
    target_size = (224, 224)
    img = image.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255
    return img_array

# Function to predict the class of an image
def predict_image_class(model, image_array, class_indices):
    predictions = model.predict(image_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    
    if "healthy" in predicted_class_name.lower():
        return "healthy", predicted_class_name
    else:
        return "disease", predicted_class_name

# Function to get disease or healthy plant information using Google Generative AI
async def get_disease_info(class_type, class_name):
    if class_type == "healthy":
        response_text = f"The plant is healthy. {class_name} plants are in good condition."
    else:
        response = palm.generate_text(
            prompt=f"Provide detailed information about the plant disease called {class_name}.",
            model="models/text-bison-001"
        )
        response_text = response.result if response and response.result else "No information available."
    
    return response_text

# Function to handle incoming images
async def handle_image(update: Update, context: CallbackContext) -> int:
    photo = await update.message.photo[-1].get_file()
    image_stream = BytesIO()
    await photo.download_to_memory(image_stream)
    image_stream.seek(0)
    image = Image.open(image_stream)

    # Preprocess the image
    preprocessed_img = load_and_preprocess_image(image)

    # Predict the class (disease or healthy)
    class_type, class_name = predict_image_class(model, preprocessed_img, class_indices)

    # Get information about the class (disease or healthy plant)
    info = await get_disease_info(class_type, class_name)

    # Translate the information to Azerbaijani if the language preference is set to Azerbaijani
    if language_preference == 'az':
        translated_info = translator_to_az.translate(info)
        await update.message.reply_text(f"Bitki ehtimal olunur: {class_name}\n\n{translated_info}")
    else:
        await update.message.reply_text(f"The plant is likely: {class_name}\n\n{info}")
    
    return ASKING_IMAGE  # Continue the conversation

# Command to start the bot
async def start(update: Update, context: CallbackContext) -> int:
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Welcome to PDP Bot! Send me a picture of the plant leaf, and I will predict the disease or inform you if it is healthy. Type /aze to switch to Azerbaijani. Type /eng to switch to English. Type /cancel to stop the conversation.')
    return ASKING_IMAGE

# Command to translate the bot's response to Azerbaijani
async def translate(update: Update, context: CallbackContext) -> None:
    global language_preference
    language_preference = 'az'
    await update.message.reply_text('Translation to Azerbaijani is now enabled.')

# Command to cancel the conversation
async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Conversation canceled.')
    return ConversationHandler.END

# Command to reset the language to English
async def reset_language(update: Update, context: CallbackContext) -> None:
    global language_preference
    language_preference = 'en'
    await update.message.reply_text('Language reset to English.')

# Command to handle errors
async def error(update: Update, context: CallbackContext) -> None:
    print(f'Update {update} caused error {context.error}')

# Main function to start the bot
if __name__ == "__main__":
    print('Starting bot...')
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            ASKING_IMAGE: [MessageHandler(filters.PHOTO & (~filters.COMMAND), handle_image)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    
    application.add_handler(conversation_handler)
    application.add_handler(CommandHandler('aze', translate))
    application.add_handler(CommandHandler('eng', reset_language))
    application.add_error_handler(error)

    print('Polling...')
    application.run_polling()
