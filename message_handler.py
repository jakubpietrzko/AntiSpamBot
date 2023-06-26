import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
async def on_message_handler(message,bot):
    if message.author == bot.user:
        return

    # Wywołaj swój model tutaj, aby przewidzieć, czy wiadomość jest spamem
    # Odczyt modelu z pliku
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
        is_spam = model.predict([message.content])

        if is_spam=="spam":
            await message.delete()
            # Tutaj możesz dodać inne działania, takie jak karanie użytkownika, np. banowanie itp.

        await bot.process_commands(message)
