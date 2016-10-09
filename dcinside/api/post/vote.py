# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from builtins import str
from future import standard_library
standard_library.install_aliases()

from dcinside.constants import SESSION, URL  # noqa


def upvote(gall_name_en, post_num, ci_t):
    """글을 개념글 추천을 합니다."""
    SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
    SESSION.headers['Referer'] = URL.POST_VOTE_UP
    SESSION.cookies[gall_name_en + str(post_num) + '_Firstcheck'] = 'Y'

    data = dict(ci_t=ci_t, id=gall_name_en, no=post_num,
                recommend=0, vote='vote', user_id='')
    return SESSION.post(url=URL.POST_VOTE_UP, data=data)


def downvote(gall_name_en, post_num, ci_t):
    """글을 비추천 합니다."""
    SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
    SESSION.headers['Referer'] = URL.POST_VOTE_DOWN
    SESSION.cookies[gall_name_en + str(post_num) + '_Firstcheck'] = 'Y'
    SESSION.cookies[gall_name_en + str(post_num) + '_Firstcheck_down'] = 'Y'

    data = dict(ci_t=ci_t, id=gall_name_en, no=post_num,
                recommend=0, vote='vote', user_id='')
    return SESSION.post(url=URL.POST_VOTE_DOWN, data=data)
