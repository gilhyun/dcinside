# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import zip
from future import standard_library
standard_library.install_aliases()

import re  # noqa

from pyquery import PyQuery as pq  # noqa

# re_delete
ONCLICK_PATTERN_RE = re.compile('\((.*?)\)')


def yield_delete_value(d):
    for i in d('.password_layer > div > div > p.pp_input > a'):
        onclick = i.get('onclick')
        onclick = onclick.replace('javascript:re_delete(', '')
        onclick = onclick.replace(');', '')
        onclick = onclick.replace('\'', '')
        yield onclick.split(',')


def yield_user_name(name_areas):
    for name_area in name_areas:
        yield name_area.get('user_name')


def yield_user_id(name_areas):
    for name_area in name_areas:
        yield name_area.get('user_id')


def yield_reply(reply_areas):
    for reply in reply_areas('td.reply'):
        yield reply.text.strip()


def yield_raw_reply(reply_areas):
    for reply in reply_areas('td.reply'):
        yield pq(reply).outer_html()


def yield_reply_time(found):
    for retime in found('td.retime'):
        yield retime.text.strip()


def yield_ip(reply_areas):
    for reply in reply_areas('td.reply'):
        d = pq(reply)('.etc_ip')
        yield d.text().strip()


def yield_reply_num(d):
    for detail in d('p.pp_input a'):
        onclick = detail.get('onclick')
        onclick2 = ONCLICK_PATTERN_RE.findall(onclick)[0]
        onclick3 = onclick2.replace('\'', '').split(',')
        reply_no, article_no, gall_id = onclick3[:3]
        yield reply_no


def make_list(func, *args):
    return [i for i in func(*args)]


def parse_comments(html):
    d = pq(html)

    # comments
    css_selector = '.gallery_re_contents tr.reply_line'
    found = d(css_selector)

    name_areas = found('td.user.user_layer')
    reply_areas = found('td.reply')

    user_names = make_list(yield_user_name, name_areas)
    user_IDs = make_list(yield_user_id, name_areas)
    replies = make_list(yield_reply, reply_areas)
    raw_replies = make_list(yield_raw_reply, reply_areas)
    re_times = make_list(yield_reply_time, found)
    IPs = make_list(yield_ip, reply_areas)
    reply_nums = make_list(yield_reply_num, d)
    delete_values = make_list(yield_delete_value, d)

    orgin_nums = [i[-1] for i in delete_values]

    l = []
    for i in zip(user_names, user_IDs, replies,
                 raw_replies, re_times, IPs, reply_nums, orgin_nums):
        d = {}
        d['user_name'] = i[0]
        d['user_id'] = i[1]
        d['reply'] = i[2]
        d['raw_reply'] = i[3]
        d['re_time'] = i[4]
        d['IP'] = i[5]
        d['reply_num'] = i[6]
        d['orgin_nums'] = i[7]
        l.append(d)

    return l
