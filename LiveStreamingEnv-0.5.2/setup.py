#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: Bupt-Steven
# Mail: bupt-steven@foxmail.com
# Created Time:  2018-9-26 19:17:34
#############################################

from setuptools import setup, find_packages

setup(
    name = "LiveStreamingEnv",
    version = "0.5.2",
    keywords = ("pip", "LiveStreamingEnv","featureextraction"),
    description = "An env for livestreaming game in Tsinghua TransAI game",
    license = "MIT Licence",

    url = "https://github.com/bupt-steven/LiveStreamingEnv",
    author = "Bupt-Steven",
    author_email = "Bupt-steven@foxmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
                          "numpy",
                       ]
)
