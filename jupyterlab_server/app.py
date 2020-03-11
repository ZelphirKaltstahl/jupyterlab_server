# coding: utf-8
"""JupyterLab Server"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from traitlets import Unicode, Integer

from .server import ServerApp
from .handlers import add_handlers, LabConfig


class LabServerApp(ServerApp):

    default_url = Unicode('/lab',
                          help='The default URL to redirect to from `/`')

    blacklist_uri = Unicode('', config=True,
        help="The default URI to get the black list")

    whitelist_uri = Unicode('', config=True,
        help="The default URI to get the white list")

    listings_refresh_ms = Integer(1000 * 60, config=True,
        help="The interval time in milliseconds to refresh the lisings")

    lab_config = LabConfig()

    def start(self):
        add_handlers(self.web_app, self.lab_config)
        super().start()


main = LabServerApp.launch_instance
