# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

import pytest  # noqa

from dcinside import api  # noqa
from dcinside.exceptions import PostDoesNotExistError  # noqa

from tests.utils import _yield_gall_api_test_post  # noqa
from tests.constants import GALL_NAME_EN, SUBJECT, MEMO, NAME, PASSWORD  # noqa


def test_write_post():
    # TODO:Find better solution!
    global POST_NUM
    # Write post
    r = api.post.create(GALL_NAME_EN, SUBJECT, MEMO, NAME, PASSWORD)
    POST_NUM = r.text.replace('true||', '')

    assert '[제목] 항목은 최대 40자 이하로 입력해 주시기 바랍니다' not in r
    assert '[제목] 항목은 필수입니다.' not in r
    assert '[내용] 항목은 필수입니다.' not in r
    assert 'false' not in r

    # Test write post is ok
    is_subject_in_posts = any([post for post in _yield_gall_api_test_post()])
    assert is_subject_in_posts


def test_read_post():
    _post = api.post.read(GALL_NAME_EN, POST_NUM)
    assert _post['author'] == NAME
    assert _post['title'] == SUBJECT
    assert _post['content'] == MEMO


def test_upvote():
    _post = api.post.read(GALL_NAME_EN, POST_NUM)
    r = api.post.upvote(GALL_NAME_EN, POST_NUM, _post['ci_t'])
    assert '정상 접근이 아닙니다.' not in r.text
    assert '개념글 추천은 1일 1회 만 가능합니다.' not in r.text
    assert 'false' not in r.text


def test_downvote():
    _post = api.post.read(GALL_NAME_EN, POST_NUM)
    r = api.post.downvote(GALL_NAME_EN, _post['post_num'], _post['ci_t'])
    assert '정상 접근이 아닙니다.' not in r.text
    assert '비추천은 한 게시물 당 1일 1회 만 가능합니다.' not in r.text
    assert 'false' not in r.text


def test_delete_post():
    # Delete post
    r = api.post.delete(GALL_NAME_EN, POST_NUM, PASSWORD)

    # Check post is deleted
    assert '비밀번호 인증에 실패하였습니다. 다시 시도해주세요' not in r.text
    assert 'false' not in r.text

    with pytest.raises(PostDoesNotExistError):
        api.post.read(GALL_NAME_EN, post_num=POST_NUM)
