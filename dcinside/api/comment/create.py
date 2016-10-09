# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from future import standard_library
standard_library.install_aliases()

from urllib.parse import unquote  # noqa
from dcinside.constants import (COMMENT_PARAMS, URL, SESSION)  # noqa
from dcinside.helpers import get_url_params_dict  # noqa


def _get_comment_referrer_url(post):
    """댓글 작성을 하는데 사용할 리퍼러 url을 얻습니다."""
    return URL.REFERRER_URL.format(
        gall_name=post['gall_name'], post_num=post['post_num'])


def _make_comment_data(post, name, password, text):
    """댓글 작성을 하는데 필요한 데이터를 얻습니다."""
    params = unquote(COMMENT_PARAMS)
    params = unquote(params)

    d = get_url_params_dict(params)
    d['ci_t'] = post['ci_t']
    d['check_6'] = post['check_6']
    d['check_7'] = post['check_7']
    d['check_8'] = post['check_8']
    d['id'] = post['gall_name']
    d['password'] = password
    d['name'] = name
    d['memo'] = text
    d['no'] = post['post_num']
    d['spam_key'] = 'rhkdrhgkwlak!'
    d['best_orgin'] = ''
    d['recommend'] = 0
    d['campus'] = 0
    return d


def main(post, name, password, text):
    """글에 댓글을 작성합니다."""
    data = _make_comment_data(post, name, password, text)
    SESSION.headers['Referer'] = _get_comment_referrer_url(post)
    SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'

    # Post comment
    r = SESSION.post(url=URL.COMMENT_SUBMIT, data=data)

    # Post comment count
    data = dict(ci_t=post['ci_t'],
                id=post['gall_name'],
                no=post['post_num'])
    SESSION.post(url=URL.COMMENT_COUNT, data=data)

    # Post view count
    data['comment_page'] = 1
    SESSION.post(url=URL.COMMENT_VIEW, data=data)
    return r
