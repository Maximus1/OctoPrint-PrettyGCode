# coding=utf-8
"""OctoPrint-PrettyGCode Plugin."""
from __future__ import absolute_import

import octoprint.plugin  # type: ignore # pylint: disable=import-error


class PrettyGCodePlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    """Plugin to add a 3D GCode visualizer tab in Octoprint."""

    def __init__(self):
        """Initialize the plugin."""
        # pylint: disable=invalid-name
        self._logger = None
        self._plugin_version = "0.0.0"

    def on_after_startup(self):
        """Called after the plugin has been started."""
        self._logger.info("Pretty GCode.")

    def get_settings_defaults(self):
        """Return the default settings for the plugin."""
        return {}

    def get_template_configs(self):
        """Return the template configurations for the plugin."""
        return []

    def get_assets(self):
        """Return the assets for the plugin."""
        return dict(
            js=[
                "js/prettygcode.js", "js/three.min.js",
                "js/LineSegmentsGeometry.js", "js/LineGeometry.js", "js/OBJLoader.js",
                "js/LineMaterial.js", "js/LineSegments2.js", "js/Line2.js",
                "js/camera-controls.js", "js/Lut.js", "js/dat.gui.js"
            ],
            css=["css/prettygcode.css"]
        )

    # -- Softwareupdate hook
    def get_update_information(self):
        """Return the update information for the plugin."""
        return dict(
            prettygcode=dict(
                displayName="PrettyGCode",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="Marcus",
                repo="OctoPrint-PrettyGCode",
                current=self._plugin_version,
                pip="https://github.com/Maximus1/OctoPrint-PrettyGCode/archive/{target_version}.zip"
            )
        )

# If you want your plugin to be registered within OctoPrint under a different
# name than what you defined in setup.py, you may define that here.
# Same goes for the other metadata derived from setup.py that can be
# overwritten via __plugin_xyz__ control properties.
# See the documentation for that.
__plugin_name__ = "PrettyGCode"
__plugin_pythoncompat__ = ">=2.7,<4"


__plugin_implementation__ = None
__plugin_hooks__ = None

def __plugin_load__():
    """Load the plugin."""
    # pylint: disable=global-statement
    global __plugin_implementation__
    __plugin_implementation__ = PrettyGCodePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
