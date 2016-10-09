# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from pyquery import PyQuery as pq  # noqa

from api.constants import SESSION  # noqa

ROOT_URL = 'http://wstatic.dcinside.com/gallery/gallindex_iframe_new_gallery.html'  # noqa

PART = 'http://gall.dcinside.com/board/lists?id='


def get_galleries_dict_from_a_tags(a_tags):
    gall_d = {}
    for a_tag in a_tags:
        href = a_tag.get('href')
        text = a_tag.text_content().strip().replace('- ', '')

        if (not href) or (not text):
            continue
        if 'javascript:' in href:
            continue
        if PART not in href:
            continue
        href = href.replace(PART, '')
        gall_d[text] = href

    return gall_d


def get_gall_names_and_urls():
    r = SESSION.get(ROOT_URL).content
    d = pq(r)
    a_tags = d('a')
    return get_galleries_dict_from_a_tags(a_tags)
