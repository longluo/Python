#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Send Main
# 2015-07-29 17:54:08

from email import encoders
from email.header import header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		))