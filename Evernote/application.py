#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
This module defines:

    + Application class and all components

.. modeule: application.py

    :synopsis: Application class and all components

------

"""

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from Evernote.utils import get_url_by_region


class App():

    def __init__(self):
        self.view = QWebEngineView()
        self.view.setWindowTitle('Evernote')
        self.view.setGeometry(300, 300, 1280, 1080)

        svr_url = get_url_by_region()
        self.view.load(QUrl(svr_url))
        self.run()

    def run(self):
        self.view.show()
