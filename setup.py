# coding=utf-8
"""Setup script for the OctoPrint-PrettyGCode plugin."""

import sys
from setuptools import setup

####################################################################################################
### Plugin Information
####################################################################################################

plugin_info = dict(
    identifier="prettygcode",
    name="OctoPrint-PrettyGCode",
    version="1.2.4",
    description="Pretty GCode Visualizer",
    author="Kragrathea",
    author_email="todo@example.com",
    url="https://github.com/Kragrathea/OctoPrint-PrettyGCode",
    license="AGPLv3",
    requires=[],
    additional_data=[]
)

# The plugin's python package, should be "octoprint_<plugin identifier>", has to be unique
plugin_info["package"] = f"octoprint_{plugin_info['identifier']}"

####################################################################################################
### Entry Point
####################################################################################################

try:
    import octoprint_setuptools # type: ignore
except ImportError:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
          "the same python installation that OctoPrint is installed under?")
    sys.exit(-1)

setup(**octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_info["identifier"],
    name=plugin_info["name"],
    version=plugin_info["version"],
    description=plugin_info["description"],
    author=plugin_info["author"],
    mail=plugin_info["author_email"],
    url=plugin_info["url"],
    license=plugin_info["license"],
    requires=plugin_info["requires"],
    additional_data=plugin_info["additional_data"]
))
