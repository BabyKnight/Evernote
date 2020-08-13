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


class App():

    def __init__(self):
        self.view = QWebEngineView()
        self.view.setWindowTitle('Evernote')
        self.view.setGeometry(300, 300, 1280, 1080)

        url_string = "https://app.yinxiang.com/Login.action"
        self.view.load(QUrl(url_string))
        self.run()

    def run(self):
        self.view.show()
