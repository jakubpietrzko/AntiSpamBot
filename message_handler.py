import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from googletrans import Translator
async def on_message_handler(message,bot):
    if message.author == bot.user:
        return

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
        translator = Translator()
        detected_language = translator.detect(message.content).lang
        translated_text = translator.translate(message.content, src=detected_language, dest='en').text

        is_spam = model.predict([translated_text])

        if is_spam=="spam":
            await message.delete()
            

        await bot.process_commands(message)

