# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import range
from builtins import dict
from future import standard_library
standard_library.install_aliases()

from dcinside.constants import URL, SESSION  # noqa
from dcinside.html_parsers.comments import parse_comments  # noqa


def _yield_comment_html(post, cmt_all=True):
    """글 댓글들의 html을 yield합니다."""
    if cmt_all:
        max_pages = post['total_pages']
    else:
        max_pages = 1

    for page in range(1, max_pages + 1):
        data = dict(ci_t=post['ci_t'],
                    id=post['gall_name'],
                    no=post['post_num'],
                    comment_page=page)
        SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
        r = SESSION.post(url=URL.COMMENT_VIEW, data=data).text
        yield r


def main(post):
    """글의 댓글들을 읽습니다."""
    cmts = []
    for cmt in _yield_comment_html(post):
        cmts += parse_comments(cmt)
    return cmts
