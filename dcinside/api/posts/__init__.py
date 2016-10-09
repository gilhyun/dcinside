# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import int
from future import standard_library
standard_library.install_aliases()

import re  # noqa

from pyquery import PyQuery as pq  # noqa
from dcinside.constants import (CSS, PAGE_PATTERN,
                                               SESSION, URL)  # noqa
from dcinside.html_parsers.posts import posts_parser  # noqa


def get_html(url):
    return SESSION.get(url).text


def _make_url(gall_name_en, page_num):
    return URL.POSTS.format(gall_name_en=gall_name_en, page_num=page_num)


def _is_page_num_ok(page_num, last_page_num):
    if page_num >= 1:
        return True
    elif page_num > last_page_num:
        return False
    return False


def get_last_page_num(gall_name_en):
    """갤러리의 마지막 페이지 숫자를 얻습니다."""
    url = _make_url(gall_name_en, page_num=1)
    html = get_html(url)
    last_page_num = pq(html)(CSS.LAST_PAGE)[0].get('href')
    last_page_num = re.findall(PAGE_PATTERN, last_page_num, re.DOTALL)[0]
    return int(last_page_num)


def read(gall_name_en, page_num):
    """갤러리의 주어진 페이지 숫자의 글 목록을 얻습니다."""
    url = _make_url(gall_name_en, page_num)
    html = get_html(url)
    return posts_parser(html)
