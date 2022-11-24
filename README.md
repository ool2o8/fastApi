<img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=black"/><img src="https://img.shields.io/badge/Mysql-4479A1?style=flat&logo=Mysql&logoColor=white"/><img src="https://img.shields.io/badge/SQlite-003B57?style=flat&logo=SQLite&logoColor=white"/>
<img src="https://img.shields.io/badge/AmazonEC2-FF9900?style=flat&logo=AmazonEC2&logoColor=white"/><img src="https://img.shields.io/badge/Gunicorn-499848?style=flat&logo=Gunicorn&logoColor=white"/><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/><img src="https://img.shields.io/badge/NGINX-009639?style=flat&logo=NGINX&logoColor=white"/>


# fastApi

- 2022-11-03 fast api project start
- 2022-11-04 JWT 토큰 쿠키로 받아오는 방법 찾기
- 2022-11-05 쿠키에 담고, 로그인 유지가 dependency 추가, refactoring
- 2022-11-16 post 모델, 스키마 추가
- 2022-11-17 post list, retrieve 추가
- 2022-11-22 food 이미지 업로드 기능 추가 + cors issue
- 2022-11-23 food 이미지 기능 post로 이동, 이미지 업로드, 이미지 response 추가


###auth_router URL
|CRUD|HTTP|URL|
|---|---|---|
|토큰 발행|POST|/auth/token|
|로그인|POST|/auth/login|
|로그아웃|GET|/auth/logout|
|유저 조회|GET|/auth/users|
|유저 생성|POST|/auth/users|
|내 정보 조회|GET|/auth/me|

###blog_router URL
|CRUD|HTTP|URL|
|---|---|---|
|게시글 전체 조회|GET|/post/post|
|게시글 생성|POST|/post/post|
|특정 게시글 조회|GET|/post/post/{post_id: int}|
|이미지 등록|POST|/img|
|게시글 이미지 조회|GET|/post/post/img/{post_id: int}|




### 게시글 등록 시퀀스 다이어그램
<img src="https://user-images.githubusercontent.com/59391473/203673635-b713ffbb-410f-48b7-b2cb-1f19928afcbb.png" width="400" height="400"/>
![Untitled](https://user-images.githubusercontent.com/59391473/203673635-b713ffbb-410f-48b7-b2cb-1f19928afcbb.png)


### 로그인 시퀀스 다이어그램
<img src="https://user-images.githubusercontent.com/59391473/203673658-9ffdeb63-9db1-44d5-a536-2e61ae4c8a7d.png" width="400" height="400"/>
![Untitled (1)](https://user-images.githubusercontent.com/59391473/203673658-9ffdeb63-9db1-44d5-a536-2e61ae4c8a7d.png)
