## AIO API

The only API you'll ever need to make your discord bot spicy, fun and stand out.

## About

This is an API developed to simplify the work of discord bot developers. Usually people find
various sources to get image editing, memes, funny images, and such from different sources.
This simplifies the work of the developer by binding everything in one by combining APIs, and
Some implementation of my own too.

The live version can be used and integrated, and is available at [aio-api-discord.herokuapp.com](http://aio-api-discord.herokuapp.com/).

## Installation

This is a guide to help you self host the API, and use it privately which simplifies the work, and
reduces the load on this API too.

### Docker

Docker is an easy way of containerizing and delivering your applications quickly and easily, in a
convenient way. It's really simple to get started with this, with docker handling all the installation
and other tasks.Configure the environmental variables by renaming the `.env.example` file to `.env` with the respective
values. Once you have your environmental variables and config, follow the guide below.

Docker mini guide:

- To start development environment: `docker-compose -f docker-compose.yml -f docker-compose.dev.yml up`
- To start production deployment: `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up`
- To stop the container: `docker-compose down`
- To rebuild the container: `docker-compose --build`

**NOTE**: The server runs on `127.0.0.1:8000` in dev environment, and `0.0.0.0:80` in Production environment.
You can change them as needed, in the respective docker compose files and use them. (If you're using docker 
for development or self-hosting your own instance).

### Self-hosting without docker

This is a clean and neat way of hosting without using docker. You can follow this if docker doesn't work
well on your system, or it doesn't support it. Containers are resource intensive, and your PC might not
be able to do it, this is the perfect method to get started with the self-hosting.

- Clone or fork the repository, whichever suits you better.
- Install `pipenv`, a virtual env for python. Command: **`pip install pipenv`**
- Create the virtual environment and prepare it for usage using `pipenv update`
- Configure the environmental variables by renaming the `.env.example` file to `.env` with the respective
  values for it. If you're using heroku or other platforms that have option for external environmental
  variables, use that instead of `.env`
- Configure the options and settings available in `config.py` inside the API module, according to your
  preferences.
- Run the server using `pipenv run start`

## Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you
can just submit a PR to this repo and it will be deployed once it's accepted. The contributing file can be
found
[here](https://github.com/janaSunrise/AIO-API/blob/main/CONTRIBUTING.md).

⚠️ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your commit or the PR Created.
Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before making the commit message.

## Show your support

We love people's support in growing and improving. Be sure to leave a ⭐️ if you like the project and
also be sure to contribute, if you're interested!

## Maintainers

Me and one of my really closest friends maintain this repo and we aim to provide the best, free open source API for everyone to use and deploy
their own instances to make their bot better in a certain way.

- [Sunrit Jana](https://github.com/janaSunrise)
- [Faholan](https://github.com/Faholan)
