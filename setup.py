# coding=utf-8
"""Setup script for the OctoPrint-PrettyGCode plugin."""

import sys
from setuptools import setup

####################################################################################################
### Plugin Information
####################################################################################################

PLUGIN_INFO = dict(
    identifier="prettygcode",
    name="OctoPrint-PrettyGCode",
    version="1.2.4.2",
    description="Pretty GCode Visualizer",
    author="Marcus",
    author_email="todo@example.com",
    url="https://github.com/Maximus1/OctoPrint-PrettyGCode",
    license="AGPLv3",
    requires=[],
    additional_data=[]
)

# The plugin's python package, should be "octoprint_<plugin identifier>", has to be unique
PLUGIN_INFO["package"] = f"octoprint_{PLUGIN_INFO['identifier']}"

####################################################################################################
### Entry Point
####################################################################################################

try:
    import octoprint_setuptools  # type: ignore
except ImportError:
    print(
        "Could not import OctoPrint's setuptools, are you sure you are running that under "
        "the same python installation that OctoPrint is installed under?"
    )
    sys.exit(-1)

setup(
    **octoprint_setuptools.create_plugin_setup_parameters(
        identifier=PLUGIN_INFO["identifier"],
        name=PLUGIN_INFO["name"],
        version=PLUGIN_INFO["version"],
        description=PLUGIN_INFO["description"],
        author=PLUGIN_INFO["author"],
        mail=PLUGIN_INFO["author_email"],
        url=PLUGIN_INFO["url"],
        license=PLUGIN_INFO["license"],
        requires=PLUGIN_INFO["requires"],
        additional_data=PLUGIN_INFO["additional_data"],
    )
)
