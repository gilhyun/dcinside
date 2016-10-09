# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from builtins import dict
from builtins import int
from future import standard_library
standard_library.install_aliases()

import math  # noqa
from datetime import datetime  # noqa

from pyquery import PyQuery as pq  # noqa

from dcinside.helpers import parse_int  # noqa


def _parse_mandu(d):
    text = d('a.btn_md_spt').text()
    return parse_int(text)


def _parse_downvote(d):
    text = d('#recommend_vote_down').text()
    return parse_int(text)


def _parse_upvote(d):
    text = d('#recommend_vote_up').text()
    return parse_int(text)


def _parse_delete_values(d):
    return [i.get('href') for i in d('p.pp_input > a')]


def _parse_check_8(d):
    return d('input#check_8')[0].get('value')


def _parse_check_7(d):
    return d('input#check_7')[0].get('value')


def _parse_check_6(d):
    return d('input#check_6')[0].get('value')


def _parse_imgs1(d):
    css_selector = 'ul.appending_file li a'
    found = d(css_selector)
    return [i.get('href') for i in found]


def _parse_title(d):
    css_selector = 'dl.wt_subject dd'
    found = d(css_selector)
    return found.text()


def _parse_author(d):
    css_selector = 'div.w_top_left dl:nth-child(2) span'
    found = d(css_selector)
    return found[0].get('user_name')


def _parse_author_id(d):
    css_selector = 'div.w_top_left dl:nth-child(2) span'
    found = d(css_selector)
    return found[0].get('user_id')


def _parse_views_count(d):
    css_selector = 'div.w_top_left dd.dd_num'
    found = d(css_selector)
    views = found.text()
    _ = views.split(' ')[0]
    return parse_int(_)


def _parse_comments_count(d):
    css_selector = 'div.w_top_left dd.dd_num'
    found = d(css_selector)
    views = found.text()
    _ = views.split(' ')[1]
    return parse_int(_)


def _parse_imgs2(d):
    css_selector = 'div.s_write img'
    found = d(css_selector)
    return [i.get('src') for i in found]


def _parse_text_content(d):
    # css_selector = 'div.s_write td p'
    css_selector = 'div.s_write td'
    found = d(css_selector)
    content = [i.text_content() for i in found]
    return '\n'.join(content)


def _parse_html_content(d):
    css_selector = 'div.s_write'
    return d(css_selector).outer_html()


def _parse_ci_t(d):
    css_selector = 'input[name=ci_t]'
    found = d(css_selector)
    return found[0].get('value')


def _parse_datetime(d):
    css_selector = 'div.w_top_right b'
    found = d(css_selector).text()
    return datetime.strptime(found, '%Y-%m-%d %H:%M:%S')


def _parse_ip(d):
    css_selector = 'div.w_top_right .li_ip'
    found = d(css_selector)
    return found.text()


def make_post_data(ci_t, gall_name, post_num, comment_page=1):
    d = {}
    d['ci_t'] = ci_t
    d['id'] = gall_name
    d['no'] = post_num
    d['comment_page'] = comment_page
    return d


def _parse_total_pages(comments_count):
    return math.ceil(int(comments_count) / 40)


def post_parser(html, gall_en_name, post_num):
    d = pq(html)
    gall_name, post_num = gall_en_name, post_num
    comments_count = _parse_comments_count(d)

    post = dict(
        gall_name=gall_name,
        post_num=post_num,
        imgs1=_parse_imgs1(d),
        imgs2=_parse_imgs2(d),
        title=_parse_title(d),
        author=_parse_author(d),
        views=_parse_views_count(d),
        comments_count=comments_count,
        content=_parse_text_content(d),
        html_content=_parse_html_content(d),
        datetime=_parse_datetime(d),
        IP=_parse_ip(d),
        user_id=_parse_author_id(d),
        ci_t=_parse_ci_t(d),
        total_pages=_parse_total_pages(comments_count),
        check_6=_parse_check_6(d),
        check_7=_parse_check_7(d),
        check_8=_parse_check_8(d),
        delete_values=_parse_delete_values(d),
        upvote=_parse_upvote(d),
        downvote=_parse_downvote(d),
        mandu=_parse_mandu(d),
    )

    return post
