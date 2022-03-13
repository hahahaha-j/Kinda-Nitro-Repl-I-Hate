import nextcord
import os

discord = nextcord

client = discord.Client()

@client.event
async def on_ready():
  print("Logged in as", client.user.name, "|", str(client.user.id) + f"\n Invite bot: https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot%20applications.commands")
@client.slash_command(name = "nitroify", description = "Send any emoji without nitro!")
async def nitro(ctx, msg):
  webhook = await get_hook(ctx)
  try:
    await webhook.send(content = msg, username = ctx.user.display_name, avatar_url = ctx.user.display_avatar, allowed_mentions = discord.AllowedMentions.none())
  except :
    await webhook.send(content = msg, username = ctx.user.display_name, allowed_mentions = discord.AllowedMentions.none())
  await ctx.send("Done!", ephemeral=True)

async def get_hook(message):
  x = False
  webhooks = await message.channel.webhooks()
  for webhook in webhooks:
    if client.user.name.lower() in str(webhook.name).lower():
      x = True
      return webhook
  if x != True:
    webhook = await message.channel.create_webhook(name = f"{client.user.name} Webhook for #"+message.channel.name)
    return webhook

import server
server.go()

client.run(os.getenv("TOKEN"))