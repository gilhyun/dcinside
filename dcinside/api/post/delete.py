# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from future import standard_library
standard_library.install_aliases()

from pyquery import PyQuery as pq  # noqa
from dcinside.constants import SESSION, URL  # noqa


def _parse_ci_t(html):
    """csrf_token을 html에서 파싱합니다."""
    d = pq(html)
    for i in d('input'):
        if i.get('name') == 'ci_t':
            ci_t = i.get('value')
            return ci_t


def _delete_post_step4(ci_t, key, gall_name_en, post_num):
    SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
    data = dict(ci_t=ci_t, key=key, id=gall_name_en, no=post_num)
    return SESSION.post(url=URL.DELETE_POST4, data=data)


def _delete_post_step3(key, gall_name_en, post_num):
    del SESSION.headers['X-Requested-With']
    full_delete_url = URL.DELETE_POST3.format(
        gall_name=gall_name_en, post_num=post_num, key=key)

    con = SESSION.get(full_delete_url)
    ci_t = _parse_ci_t(con.text)
    return ci_t


def _get_key(ci_t, gall_name_en, password, post_num):
    """key를 얻습니다."""
    SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
    data = dict(ci_t=ci_t, password=password, id=gall_name_en, no=post_num)
    con = SESSION.post(url=URL.DELETE_POST2, data=data)
    key = con.text.split('||')[1]
    return key


def _get_ci_t(gall_name_en, post_num):
    """csrf_token을 얻습니다."""
    delete_url = URL.DELETE_POST1.format(
        gall_name=gall_name_en, post_num=post_num)
    con = SESSION.get(delete_url)
    return _parse_ci_t(con.text)


def main(gall_name_en, post_num, password):
    """글을 지웁니다."""
    ci_t = _get_ci_t(gall_name_en, post_num)
    key = _get_key(ci_t, gall_name_en, password, post_num)
    ci_t = _delete_post_step3(key, gall_name_en, post_num)
    r = _delete_post_step4(ci_t, key, gall_name_en, post_num)
    return r
