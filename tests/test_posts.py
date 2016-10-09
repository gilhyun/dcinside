# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

import datetime as dt  # noqa

from dcinside.api import posts  # noqa
from tests.constants import POSTS_GALL_NAME_EN  # noqa


POSTS_COUNT = 29


def test_posts_read():
    last_page_num = posts.get_last_page_num(POSTS_GALL_NAME_EN)
    _posts = posts.read(POSTS_GALL_NAME_EN, page_num=last_page_num)
    for i in _posts:
        print(i)

    assert len(_posts) == POSTS_COUNT
