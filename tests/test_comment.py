# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import pytest  # noqa

from dcinside.api import comment, post  # noqa
from dcinside.helpers import parse_int  # noqa
from .constants import GALL_NAME_EN, NAME, PASSWORD  # noqa
from .utils import make_random_str  # noqa


def test_create_comment(post_num):
    global COMMENT_NUM

    _post = post.read(GALL_NAME_EN, post_num=post_num)
    memo = make_random_str(10)
    r = comment.create(_post, NAME, PASSWORD, memo)

    COMMENT_NUM = parse_int(r.text)

    assert '[이름] 항목은 최대 12자 이하로 입력해 주시기 바랍니다.' not in r.text
    assert '[내용] 항목은 최대 400자 이하로 입력해 주시기 바랍니다.' not in r.text
    assert 'false' not in r.text


def test_read_comment(post_num):
    _post = post.read(GALL_NAME_EN, post_num=post_num)
    cmts = comment.read(_post)
    l = [True for cmt in cmts if parse_int(cmt['reply_num']) == COMMENT_NUM]
    assert any(l)


def test_delete_comment(post_num):
    _post = post.read(GALL_NAME_EN, post_num=post_num)
    comment.delete(_post, GALL_NAME_EN, COMMENT_NUM, PASSWORD)

    _post = post.read(GALL_NAME_EN, post_num=post_num)
    cmts = comment.read(_post)
    l = [True for cmt in cmts if parse_int(cmt['reply_num']) == COMMENT_NUM]
    assert not any(l)

    # Delete post
    post.delete(GALL_NAME_EN, post_num, PASSWORD)
