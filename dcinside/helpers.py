# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import int
from future import standard_library
standard_library.install_aliases()

import re  # noqa

import requests  # noqa

from faker import Factory  # noqa


def parse_int(text):
    if text == '':
        return 0
    return int(''.join(re.findall('\d', text)))


def get_url_params_dict(params):
    key_and_values = params.split('&')
    params = [i.split('=') for i in key_and_values]
    try:
        return {k: v for k, v in params}
    except ValueError:
        return {}


def make_session():
    session = requests.session()
    session.headers['User-Agent'] = Factory.create().chrome()
    return session
