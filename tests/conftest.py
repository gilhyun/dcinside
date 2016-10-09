# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import pytest  # noqa

from dcinside.api import post  # noqa
from .constants import GALL_NAME_EN, NAME, PASSWORD  # noqa
from .utils import make_random_str  # noqa

POST_NUM = None
POST_CREATED = False


@pytest.fixture
def post_num(scope='session'):
    global POST_CREATED, POST_NUM
    subject = '!@#$%^' + make_random_str(10)
    memo = make_random_str(10)

    if not POST_CREATED:
        _post = post.create(GALL_NAME_EN, subject, memo, NAME, PASSWORD)
        POST_CREATED = True
        POST_NUM = _post.text.replace('true||', '')

    return POST_NUM
