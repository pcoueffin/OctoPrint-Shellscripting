# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class ShellscriptingPlugin(octoprint.plugin.SettingsPlugin,
                           octoprint.plugin.AssetPlugin,
                           octoprint.plugin.TemplatePlugin):

    def on_after_startup(self):
        self._logger.info("Hello World!")

__plugin_implementation__ = ShellscriptingPlugin()



