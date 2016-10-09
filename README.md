===============================
Unofficial Dcinside API
===============================


디시인사이드 비공식 API입니다.

============
Installation
============


```bash
    $ pip install git+https://github.com/carcdrcons/dcinside
```

============
Usage
============

```python
    # -*- coding:utf-8 -*-
    import random
    import string
    import webbrowser
    from pprint import pprint

    from dcinside import api


    def make_random_str(max_char):
        return ''.join(random.SystemRandom().choice(
            string.ascii_letters + string.digits) for _ in range(max_char))


    # 갤 영문명
    # 갤 주소 'http://gall.dcinside.com/board/lists/?id=lee0e' 에서 lee0e 부분
    GALL_NAME_EN = 'lee0e'  # 이영애 갤러리

    # 제목
    SUBJECT = 'test_' + make_random_str(10)

    # 본문
    MEMO = 'test_' + make_random_str(10)

    # 이름
    NAME = 'test'

    # 패스워드
    PASSWORD = 'password'

    # 게시글 주소 템플릿
    URL_TMPL = 'http://gall.dcinside.com/board/view/?id={gall_name_en}&no={post_num}'

    # 글 작성을 합니다.
    r = api.post.create(GALL_NAME_EN, SUBJECT, MEMO, NAME, PASSWORD)

    # 글 번호를 파싱합니다.
    # 예) r.text = 'true||28030'
    # true는 글 작성 성공 여부, 28030는 글 번호
    post_num = r.text.split('||')[1]

    # 글을 읽습니다.
    post = api.post.read(GALL_NAME_EN, post_num=post_num)
    print('글 정보')
    pprint(post, indent=4)

    # 글 추천을 합니다.
    api.post.vote.upvote(GALL_NAME_EN, post['post_num'], post['ci_t'])

    # 글 비추천을 합니다.
    api.post.vote.downvote(GALL_NAME_EN, post['post_num'], post['ci_t'])

    # 글에 댓글을 작성합니다.
    api.comment.create(post, NAME, PASSWORD, MEMO)

    # 댓글을 작성했기 때문에 글을 다시 읽습니다.
    post = api.post.read(GALL_NAME_EN, post_num=post_num)

    # 댓글들을 읽습니다.
    print('댓글들')
    comments = api.comment.read(post)
    for comment in comments:
        pprint(comment, indent=4)

    # 댓글들을 삭제합니다.
    for comment in comments:
        api.comment.delete(post, GALL_NAME_EN,
                           comment['reply_num'], PASSWORD)

    # 작성한 글을 브라우저에서 보여줍니다.
    url = URL_TMPL.format(gall_name_en=GALL_NAME_EN, post_num=post_num)
    webbrowser.open(url)

    # 글을 지웁니다.
    # api.post.delete(GALL_NAME_EN, post['post_num'], PASSWORD)
```

* Free software: MIT license

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

* Cookiecutter: (https://github.com/audreyr/cookiecutter)
* `audreyr/cookiecutter-pypackage`: (https://github.com/audreyr/cookiecutter-pypackage)
