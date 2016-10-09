# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from future import standard_library
standard_library.install_aliases()

from dcinside.constants import URL, SESSION  # noqa


def main(post, gall_name_en, comment_num, password):
    """댓글을 삭제합니다."""
    data = dict(ci_t=post['ci_t'],
                no=post['post_num'],
                id=gall_name_en,
                p_no=post['post_num'],
                re_no=comment_num,
                orgin_no=0,
                password=password,
                best_orgin='',
                check_7=post['check_7'])

    SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
    return SESSION.post(url=URL.COMMENT_DELETE_SUBMIT, data=data)
