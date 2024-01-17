# Spotify Auto Downloader

**In order to utilize this automation code you will need to make sure you have python, chrome and some other packages installed.**

- Run the command to install all the required packages into your enviroment:

        pip install -r requirements.txt

- Create a spotify developer account with the apotify account you want to get your songs from by visting https://developer.spotify.com/

- Create an app, you can name it what ever you would like, add a description.

- In the website field enter "http://localhost/"

- In the Redirects URIs field enter "http://localhost/callback"

- Create the app

- Go into your developer dashboard(if you aren't already there)

- Go into settings

- Note your client ID and client secret

- Create an .env file inside of the automation folder 

- Inside the .env file put:

            SPOTIPY_CLIENT_ID='your_clientID'
            SPOTIPY_CLIENT_SECRET='your_clientSecret'
            SPOTIPY_REDIRECT_URI='http://localhost/callback'

- On line 14 of main.py you need to replace C:\Users\Jonathan King\Documents\Spotify Songs with the path you want the songs to be downloaded in

- On line 15 of main.py you need to replace C:\Users\Jonathan King\Documents\Self Teaching\Python\Projects\Spoofy-Auto-Download\Extensions\AddBlocker.crx with the **absolute path** for the AddBlocker.crx file within the extension folder.

- Go Command Line inside of the Automation Folder and run

        python app.py

- Open another Command Propmt Window in the same folder and run:

        python main.py

- When python main.py is ran a window will open in your browser, copy the link from that page and paste it into the command line and hit enter and the automation will commence.






   




