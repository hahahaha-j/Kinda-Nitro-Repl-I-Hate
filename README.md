# How to host this bot:

If you want to jump strait to local hosting, click [here](https://github.com/TheCatsMoo/Kinda-Nitro#local-hosting)

If you don't want to host the bot, click [here](https://discord.com/oauth2/authorize?client_id=952313154547875850&permissions=8&scope=bot%20applications.commands) to invite a public version of the bot. 

Generate a bot token from the [Discord developer portal](https://discord.com/developers)

**You can also watch [this video](https://youtu.be/5zm_yV3H4IA) for better examples.**

Click on "New Application"

Name it whatever you want. 

You can type in the about me section of the bot. 

Then click on the bots tab on the side of the portal

Click "Regenerate Token". 

COPY THAT TOKEN AND PASTE IT IN A NOTES APP OR WHATEVER, BUT SAVE IT!

### If you want to host on the cloud:
[Click here](https://replit.com/github/TheCatsMoo/Kinda-Nitro)

Make an account

Click the lock icon on the side of the replit page. 

In the box that says `key` type the word ``TOKEN``

In the box that says `value` paste the token you got from the developer portal

Click `Add new secret`

Click the button that says `run` at the top of the page. The bot might take anywhere to a min to boot up. 

** If the run button goes back to `run` after you clicked it, click the packages icon and type in `nextcord` and click the `+` next to the name.**

![packages](https://i.ibb.co/wpZ7D3L/Screen-Shot-2022-03-12-at-4-24-41-PM.png)

Click to the Console tab ![console](https://i.ibb.co/VDqqY9Z/Screen-Shot-2022-03-12-at-4-27-09-PM.png)

There should be a link, and a page should have popped up. On the top. 

![page](https://i.ibb.co/Cb7rVTW/Screen-Shot-2022-03-12-at-4-29-41-PM.png)

Go to [uptime robot](https://uptimerobot.com/dashboard#mainDashboard) and create an account. 

Watch [this video](https://youtu.be/dEQGTR_RVlU) on how to set up hosting. 

In the console tab, you should have gotten an invite link for the bot. Click that, and add it to any server!

## Local Hosting
`git clone github.com/TheCatsMoo/Kinda-Nitro.git`

Make a .env file with the value `TOKEN={your bot's token}`

Run `pip install nextcord`

Delete ```py
import server
server.go()```

Delete `server.py`

then run `python main.py`

## Thank you so much! If anything comes up, please [let me know on discord](https://discord.com/users/788148692196261960)!
