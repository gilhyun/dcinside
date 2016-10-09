# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

from .helpers import make_session  # noqa


# Init session
USER_AGENT = 'Unofficial Dcinside Python API'
SESSION = make_session()
SESSION.headers['User-Agent'] = USER_AGENT


# ETC
PAGE_PATTERN = 'page=(.*?)$'
COMMENT_WRONG_PASS_MSG = 'false||비밀번호가 틀립니다.'


# Comment params
COMMENT_PARAMS = "ci_t=db95b769b07fce60a6166ec8140aeff3&name=%E3%85%87%E3%85%87%E3%85%87&password=ddd&memo=%E3%85%8E&id=mystery&no=970353&best_orgin=&check_6=a17f35ad2222b45bba3506559c08d9b640d1&check_7=7d&check_8=a14724aa2527&campus=0&recommend=0"  # noqa
COMMENT_DELETE_SUBMIT_PARAMS = 'ci_t=96dd5fc972008454501ee132b8950a2b&no=27419&id=lee0e&p_no=27419&re_no=71575&orgin_no=1725397&password=1111&best_orgin=&check_7=7cea8273b68b6f'  # noqa


class CSS(object):
    LAST_PAGE = '#dgn_btn_paging > a:nth-child(22)'


class URL(object):
    ROOT = 'http://gall.dcinside.com'

    # Post
    POST_READ = ROOT + '/board/view/?id={gall_name_en}&no={post_num}'  # noqa
    POST_CREATE = ROOT + '/board/write/?id={gall_name_en}'
    DELETE_POST1 = ROOT + '/board/delete/?id={gall_name}&no={post_num}'  # noqa
    DELETE_POST2 = ROOT + '/forms/delete_password_submit'
    DELETE_POST3 = ROOT + '/board/delete/?id={gall_name}&no={post_num}&key={key}'  # noqa
    DELETE_POST4 = ROOT + '/forms/delete_submit'
    POST_VOTE_UP = ROOT + '/forms/recommend_vote_up'
    POST_VOTE_DOWN = ROOT + '/forms/recommend_vote_down'

    # Comment
    COMMENT_SUBMIT = ROOT + '/forms/comment_submit'
    COMMENT_COUNT = ROOT + '/comment/count'
    COMMENT_VIEW = ROOT + '/comment/view'
    COMMENT_DELETE_SUBMIT = ROOT + '/forms/comment_delete_submit'  # noqa

    # Posts
    POSTS = ROOT + '/board/lists/?id={gall_name_en}&page={page_num}'  # noqa

    # ETC
    REFERRER_URL = ROOT + '/board/view/?id={gall_name}&no={post_num}'
