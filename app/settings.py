# coding:utf-8

import os
from pydantic import BaseSettings
from .utils.log_handler import LogHandler

# Initialize a logger for the settings module
logger = LogHandler("settings", "INFO")


# Define a Settings class to manage configuration settings
class Settings(BaseSettings):
    # Database configuration
    database_name = "copy_hero"
    database_host = "127.0.0.1"
    database_port = 27017
    database_username = ""
    database_password = ""
    copy_hero_version = "1.0.6013"

    # Log configuration
    log_name = "copy-hero-log"
    log_level = "DEBUG"

    class Config:
        env_file = ".local.env"  # Specify the default environment file
        env_file_encoding = "utf-8"  # Specify the encoding of the environment file


# Define a dictionary to map environment names to their respective env files
env_list = {
    "local": "app/.local.env",
}

# Get the current environment from the OS environment variables, default to "local"
env = os.getenv("env", "local")

# Log the environment being used and the corresponding env file
logger.info("env: {} ---> load env file: {}".format(env, env_list[env]))

# Check if the specified environment is supported
if env not in env_list.keys():
    raise Exception("env: {} not supported. support env: ".format(env, env_list))

# Load settings from the specified environment file
settings = Settings(_env_file=env_list[env], _env_file_encoding="utf-8")

# Log the loaded settings
logger.debug("settings: {}".format(settings.dict()))

# Reinitialize the logger with settings from the loaded configuration
logger = LogHandler(settings.log_name, settings.log_level)


# Main function
def main():
    pass


# Entry point for the script
if __name__ == "__main__":
    main()
