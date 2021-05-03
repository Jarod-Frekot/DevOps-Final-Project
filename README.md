# DevOps Final Project - Discord Bot

## Project Overview
The goal of our project was to generate a Discord bot (his name is Felix) that responds to certain statements within a Discord channel. Essentially, you can run `vagrant up` and this will start Felix and run his corresponding script. Once that occurs, Felix will be awake and ready to respond within the channel, based on certain keywords or phrases that others write. We are also hosting the project in Heroku's cloud platform. Felix is automatde in the sense that when you run `vagrant up`, he is awake and ready to respond in the channel, and the project is hosted within Heroku's cloud platform automatically. 

## Set Up
There are a few initial set up aspects you must do before running either locally or virtually. 

1. Create a .env file `nano .env`
2. Add Discord api key in the .env file `API_KEY=[insert key here]`, to save and exit: control X, Y, enter
3. Lastly, you need to make sure the Discord certificate is installed correctly on your machine. Paste this in terminal: `sudo /Applications/Python\ 3.9/Install\ Certificates.command ; exit;
 -- pip install --upgrade certifi`. However, if you are running a different version of python, say 3.7, replace the `3.9` with `3.7`. To check your version, run `python --version` from your root directory. 


### Running Locally
Be sure the three steps above are completed first!

1. Create a virtual environment `python -m venv .venv`
2. Activate the virtual environment `source .venv/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Run the script `python bot.py`

### Running Virtually
Be sure the three steps above are completed first!

1. Run `vagrant up` - that's it!

To shutdown the machine, run `vagrant destroy -f`. 


## Functionality of Felix
1. $good bot - Returns a cat smiling png file (will also return this file if a message contains 'good bot')
2. $bad bot - Returns a sad face (will also return this file if a message contains 'bad bot')
3. $mood - Returns a random png with Felix's possible mood at the time
4. $hello - Returns a Hello {Your Name}!
5. $kanye - Returns a random quote by accessing the kanye.rest API.


## Technologies Used
1. [Python](https://www.python.org/)
3. [Vagrant](https://www.vagrantup.com/)
4. [Heroku](https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=CjwKCAjwj6SEBhAOEiwAvFRuKCWkP06AThR0JEjkBSIR_Sihz6VPdB3zvTo6HGKDa9iUNOy_vWkSUxoCrE0QAvD_BwE)


## Background
1. [Discord API Reference](https://discord.com/developers/docs/reference)
2. [How to make a Discord bot](https://www.youtube.com/watch?v=BPvg9bndP1U)
3. [Discord.py Python library](https://pypi.org/project/discord.py/)

## Authors
* Colby Hillman ([ColbyHman](https://github.com/ColbyHman))
* Trae Freeman ([MrTsfree](https://github.com/MrTsfree))
* Kylie Norwood ([kylienorwood](https://github.com/kylienorwood))
* Jarod Frekot ([Jarod-Frekot](https://github.com/Jarod-Frekot))
