# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import range
from future import standard_library
standard_library.install_aliases()

import string  # noqa
import random  # noqa

from dcinside.api import posts  # noqa
from .constants import GALL_NAME_EN  # noqa


def make_random_str(max_char):
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(max_char))


def _yield_gall_api_test_post():
    # Get gall 1 page
    page_num = 1
    _posts = posts.read(GALL_NAME_EN, page_num)

    # Yield api test post
    for _post in _posts:
        if _post['subject'].startswith('!@#$%^'):
            yield _post
