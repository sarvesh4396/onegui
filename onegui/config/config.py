#!/usr/bin/env python3

""""
Contains config related functions and variables for the main package
"""
from configparser import RawConfigParser
from .version import __version__
from os.path import abspath, basename, dirname, exists, join


# Application name
package = "onegui"


# Base Variables
CURRENT_PLATFORM = get_os()
HOME_DIR = get_homedir(os=CURRENT_PLATFORM)
APPLICATION_DIR = join(HOME_DIR, package)
CURRENT_DIR = abspath(dirname(__file__))
ASSETS_DIR = CURRENT_DIR.replace(basename(CURRENT_DIR), "assets")


# Log and Config variables
RESULTS_DIR = join(APPLICATION_DIR, "results")
SCREENSHOT_DIR = join(APPLICATION_DIR, "screenshot")
TEMP_DIR = join(APPLICATION_DIR, "temp")
LOG_DIR = join(APPLICATION_DIR, "logs")
CONFIG_FILE = join(APPLICATION_DIR, "config.cfg")
IDEA_FILE = join(APPLICATION_DIR, "idea.log")
LOG_FILE = join(LOG_DIR, package + ".log")
ANDROMATER_DIR = join(APPLICATION_DIR, "andromater")
WEBMATER_DIR = join(APPLICATION_DIR, "webmater")

# Default Config
DEFAULT_CONFIG = {"version": __version__, "os": CURRENT_PLATFORM, "verbose": "false"}


def get_config():
    """Returns config file data"""
    config = RawConfigParser()
    make_list_dirs([APPLICATION_DIR, LOG_DIR, RESULTS_DIR])
    if not exists(CONFIG_FILE):
        config[package] = DEFAULT_CONFIG
        write_file(path=CONFIG_FILE, data=config)
    config.read(CONFIG_FILE)
    return config


def set_config_attribute(package=package, attribute="version", value=None):
    """Sets a config attribute value"""
    config = get_config()
    if value:
        config.set(package, attribute, value)
        write_file(config)


def get_config_attribute(package=package, attribute="version"):
    """Returns config attribute value"""
    config = get_config()
    return config.get(package, attribute)
