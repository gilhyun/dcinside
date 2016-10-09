# -*- coding:utf-8 -*-
# from func import comment

from tests.utils import _yield_gall_api_test_post
from dcinside.api import comment, post, posts
from tests.constants import *


def _vote():
    # gall_name_en = 'hit'
    # post_num = 13611
    # post_num = 13644

    gall_name_en = 'lee0e'
    post_num = 27782
    _post = post.read(gall_name_en, post_num)

    from pprint import pprint
    pprint(_post)

    result = post.upvote(gall_name_en, post_num, _post['ci_t'])
    print(result.text)

    result = post.downvote(gall_name_en, post_num, _post['ci_t'])
    print(result.text)


def _delete_test_comment():
    GALL_NAME_EN = 'lee0e'
    TEXT = '!@#$%^'
    NAME = '이름'
    PASSWORD = 'password'
    POST_NUM = 27833

    _post = post.read(GALL_NAME_EN, post_num=POST_NUM)
    cmts = comment.read(_post)
    for cmt in cmts:
        r = comment.delete(_post, GALL_NAME_EN, cmt['reply_num'], PASSWORD)


def _posts_read():
    r = posts.read(GALL_NAME_EN, page_num=1)
    print(r)


def _post_read():
    for _post in _yield_gall_api_test_post():
        _post = post.read(GALL_NAME_EN, post_num=_post['post_num'])
        return _post


def _post_create():
    r = post.create(GALL_NAME_EN, SUBJECT, MEMO, NAME, PASSWORD)
    print(r.text)


def _post_delete():
    for _post in _yield_gall_api_test_post():
        print(_post)
        r = post.delete(GALL_NAME_EN, _post['post_num'], PASSWORD)
        print(r.text)


def _main():
    _post_create()
    _post = _post_read()

    comment.create(_post, NAME, PASSWORD, MEMO)

    cmts = comment.read(_post)

    for cmt in cmts:
        comment.delete(_post, GALL_NAME_EN, cmt['reply_num'], PASSWORD)

    _post_delete()


if __name__ in ['__main__', '__console__']:
    _main()
