# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from dcinside.constants import SESSION, URL  # noqa
from dcinside.exceptions import PostDoesNotExistError  # noqa
from dcinside.html_parsers.post import post_parser  # noqa


def main(gall_name_en, post_num):
    """글을 읽습니다."""
    url = URL.POST_READ.format(gall_name_en=gall_name_en, post_num=post_num)
    r = SESSION.get(url)
    html = r.text

    # raise error if post is deleted
    deleted_msg = '/error/deleted/{}'.format(gall_name_en)
    if deleted_msg in html:
        raise PostDoesNotExistError('Post does not exist.')

    return post_parser(html, gall_name_en, post_num)
