# rift-analyzer
discord bot to analyze and rank members' LoL profiles.
## How to run the bot?

### step 1
Generate a Discord Bot, a Riot Dev app and keep both Token.
### step 2
On your server (or local dev environment) set those two tokens as environment variables.

Add those two lines in your .bashrc or equivalent:
```bash 
export RIOT_API_TOKEN=XXX
export DISCORD_TOKEN=XXX
```

### step 3 
Run the app:
```bash
docker-compose up
```