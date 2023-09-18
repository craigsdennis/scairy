# scAIry

AI scares people. 🎃 What if we intentionally made it scare people? 👻

This was built during the [Replicate Arts & Crafts Hackathon](https://partiful.com/e/ac7NHwQ8ZLVIrkSHoVLP) on it's way to a sketchy iPad web app.

It is a [Streamlit](https://streamlit.io/) app that makes heavy use of the awesome models that [Replicate](https://replicate.com/explore) makes so easily accessible. Namely [Blip 2 from Salesforce](https://replicate.com/andreasjansson/blip-2) to pull out a description of the trick or treaters from an image. I used [Llama 2 70b chat](https://replicate.com/meta/llama-2-70b-chat) to generate text in the style of someone spooky and [Sad Talker](https://replicate.com/cjwbw/sadtalker) to put in a terrifying lip syncing movie. I cloned some voices (for experimentation only) of some popular creepy voiced villains using the amazing [ElevenLabs](https://elevenlabs.io). (You'll have to train your own).


## Installation

This requires [Python](https://python.org/downloads).

Copy [.env.example](./.env.example) to `.env` and add your values.

I use [direnv](https://direnv.net/) to laod these environment variables from .env files and I recommend it!

```bash
python -m venv venv
source ./bin/activate
python -m pip install -r requirements.txt
```

Clone your voices on ElevenLabs and update the [GREETERS](./app.py) dictionary.

## Get scAIRy

```bash
python -m streamlit run app.py
```
