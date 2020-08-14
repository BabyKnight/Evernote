#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob, os.path, os
from distutils.core import setup
from DistUtilsExtra.command import (build_extra,
                                    build_i18n,
                                    build_help,
                                    build_icons,
                                    clean_i18n)

setup(
    name="Evernote",
    author="Vincent Hu",
    author_email="vincent.guohua.hu@gmail.com",
    maintainer="Vincent Hu",
    maintainer_email="vincent.guohua.hu@gmail.com",
    url="https://github.com/BabyKnight/Evernote",
    license="mit",
    description="Unoffical Evernote Desktop client for Linux OS",
    packages=['Evernote'],
    data_files=[
                ('share/pixmaps', glob.glob("Evernote/Resources/evernote.png")),
                ('share/applications', glob.glob('evernote.desktop')),
                ('share/evernote',glob.glob("Evernote/Resources/*"))],
    scripts=["evernote"],
)
