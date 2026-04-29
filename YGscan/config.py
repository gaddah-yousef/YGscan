#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 9:57 PM
# @Author  : w8ay
# @File    : config.py

# Default setting
THREAD_NUM = 31

EXCLUDES = ["google", "lastpass", '.gov.']

RETRY = 2
TIMEOUT = 10
LEVEL = 3

PROXY_CONFIG_BOOL = False
PROXY_CONFIG = {
    # "http": "127.0.0.1:8080",
    # "https": "127.0.0.1:8080"
}
ABLE = []
DISABLE = []

XSS_LIMIT_CONTENT_TYPE = True

# DEBUG
DEBUG = False

# REVERSE
USE_REVERSE = False
REVERSE_HTTP_IP = "127.0.0.1"
REVERSE_HTTP_PORT = 9999

REVERSE_DNS = "dnslog.ygscan.hacking8.com"

REVERSE_RMI_IP = "127.0.0.1"
REVERSE_RMI_PORT = 10002

REVERSE_SLEEP = 5
