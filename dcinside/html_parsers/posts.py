# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import dict
from builtins import int
from builtins import object
from future import standard_library
standard_library.install_aliases()

from datetime import datetime  # noqa

from pyquery import PyQuery as pq  # noqa

from dcinside.helpers import parse_int  # noqa


class CSS(object):
    tr = '#dgn_gallery_left > div.gallery_list > div.list_table > table > thead > tr'  # noqa


def get_number_from_lxml_elem(elem):
    text = elem.text_content()
    try:
        text = int(text)
    except:
        text = 0
    return text


def parse_td(td_list):
    post_number = get_number_from_lxml_elem(td_list[0])
    author = [i for i in td_list[2].itertext()][0]

    return dict(
        post_num=post_number,
        subject=pq(td_list[1])('a')[0].text_content(),
        reply_num=parse_int(pq(td_list[1])('em').text()),
        post_type=pq(td_list[1])('a')[0].get('class'),
        author=author,
        user_id=pq(td_list[2])[0].get('user_id'),
        date=datetime.strptime(td_list[3].text_content(), '%Y.%m.%d'),
        views=get_number_from_lxml_elem(td_list[4]),
        recommended_num=get_number_from_lxml_elem(td_list[5])
    )


def get_posts_info(tr_list):
    posts = []
    for tr in tr_list:
        tr = pq(tr)
        td_list = tr('td')
        d = parse_td(td_list)
        posts.append(d)
    return posts


def get_tr_list(d):
    return d(CSS.tr)[2:]


def posts_parser(html):
    tr_list = get_tr_list(pq(html))
    return get_posts_info(tr_list)
