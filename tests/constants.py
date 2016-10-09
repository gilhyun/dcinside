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


def make_random_str(max_char):
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits) for _ in range(max_char))


GALL_NAME_EN = 'lee0e'
SUBJECT = '!@#$%^' + make_random_str(10)
MEMO = make_random_str(10)
NAME = '이름'
PASSWORD = 'apassword'


POSTS_GALL_NAME_EN = 'etc_entertainment1'
