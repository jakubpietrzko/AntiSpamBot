# AntiSpamBot
This project is a Discord bot that filters and eliminates spam messages on servers using the Naive Bayes machine learning model. The bot's demo video (demo_video.mkv) showcases its functionality. To run the code locally, you need to create a config.py file with your Discord token.
# Install
1. Install the required dependencies using the pip package manager.

     pip install -r requirements.txt
2. Create a config.py file in the main project directory.

3. Go to the Discord Developers website (https://discord.com/developers/applications) and create a new application. Navigate to the "Bot" section and generate a token.

4. In the config.py file, insert the following code, replacing <TOKEN> with your generated token.

    TOKEN = "YOUR TOKEN"

    Save the config.py file.

5. Go to the Discord Developers website (https://discord.com/developers/applications) and access your application.
6. In the left sidebar, click on "OAuth2".
7. In the "Scopes" section, select bot.
8. In the "Bot Permissions" section,  select the "Manage Messages" permission.
9. Copy the generated OAuth2 URL in the "Scopes" section.
10. Open the copied URL in your web browser.
11. Choose the server where you want to install the bot and follow the on-screen prompts to authorize the bot's access to the server.
12. To run the bot, execute the following command in your command line or terminal:

    
    python main.py


    This will start the bot and it will be ready to operate on your Discord server.
