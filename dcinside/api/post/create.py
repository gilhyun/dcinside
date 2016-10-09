# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from future import standard_library
standard_library.install_aliases()

import time  # noqa

from pyquery import PyQuery as pq  # noqa

from dcinside.constants import SESSION, URL  # noqa
from .read import main as read_post  # noqa


def _incr_view(r, gall_name_en):
    """글의 뷰 수를 1 증가 시킵니다."""
    post_num = r.text.split('||')[1]
    read_post(gall_name_en, post_num)


def _get_value_of_dom(d, css_selector):
    """DOM의 value를 얻습니다."""
    return d(css_selector)[0].get('value')


def _get_html(gall_name_en):
    """글 작성 페이지의 html을 얻습니다."""
    url = URL.POST_CREATE.format(gall_name_en=gall_name_en)
    return SESSION.get(url).text


def _get_post_data(html):
    """글 작성을 위해 필요한 data를 html에서 얻습니다."""
    d = pq(html)
    block_key = _get_value_of_dom(d, 'input#block_key')
    ci_t = _get_value_of_dom(d, 'input[name=ci_t]')
    r_key = _get_value_of_dom(d, 'input#r_key')
    return block_key, ci_t, r_key


def _get_block_key(block_key, ci_t, r_key, gall_name_en):
    """block_key를 얻습니다."""
    while 1:
        url = 'http://gall.dcinside.com/block/block/'
        SESSION.headers['X-Requested-With'] = 'XMLHttpRequest'
        SESSION.cookies['dcgame_top'] = 'Y'
        data = dict(ci_t=ci_t, id=gall_name_en, block_key=block_key)
        con = SESSION.post(url, data=data)
        if con.text != '':
            return con.text

        # 너무 빠르게 하면 값을 반환 안 해서 잠깐 쉼
        time.sleep(0.5)


def _submit(gall_name_en, ci_t, r_key, block_key,
            subject, password, name, memo):
    """글을 작성합니다."""

    url = 'http://gall.dcinside.com/forms/article_submit'

    data = dict(
        upload_status='N',
        id=gall_name_en,
        ci_t=ci_t,
        subject=subject,
        password=password,
        r_key=r_key,
        name=name,
        memo=memo,
        block_key=block_key,
        vid='',
        isMovie='',
        campus=0,
        ipt_movieCompType='',
        wiki_tag='',
        sijosae='tlwhtorororRl'
    )

    SESSION.headers['Referer'] = URL.POST_CREATE.format(
        gall_name_en=gall_name_en)
    return SESSION.post(url, data=data)


def main(gall_name_en, subject, memo, name, password):
    """글을 작성합니다."""
    html = _get_html(gall_name_en)
    block_key, ci_t, r_key = _get_post_data(html)
    block_key = _get_block_key(block_key, ci_t, r_key, gall_name_en)
    r = _submit(gall_name_en, ci_t, r_key, block_key,
                subject, password, name, memo)
    _incr_view(r, gall_name_en)
    return r
