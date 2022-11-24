# foodiary 📔🍕🍔🍟🌭

## 1. 프로젝트 정의
- 음식을 먹기 전 사진촬영을 하는 사람들이 많다.
- 하지만 대부분이 올렸다가 하루 후 사라지고 저장공간만 차지하는 역할을 한다.
- 이 과정이 의미가 있어지도록
- 음식 사진 하나와 간단한 설명만 게시하는 서비스이다.

## 2. 기능
- 로그인 & 로그아웃
- food 게시글
- tag를 통한 메뉴추천 (필터링)


## 3. 사용 기술 
### 3.1   stack 🔧
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=black"/><img src="https://img.shields.io/badge/Mysql-4479A1?style=flat&logo=Mysql&logoColor=white"/><img src="https://img.shields.io/badge/SQlite-003B57?style=flat&logo=SQLite&logoColor=white"/>
<img src="https://img.shields.io/badge/AmazonEC2-FF9900?style=flat&logo=AmazonEC2&logoColor=white"/><img src="https://img.shields.io/badge/Gunicorn-499848?style=flat&logo=Gunicorn&logoColor=white"/><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/><img src="https://img.shields.io/badge/NGINX-009639?style=flat&logo=NGINX&logoColor=white"/>

### 3.2  tool ⚙
<img src="https://img.shields.io/badge/VisualStudio-5C2D91?style=flat&logo=VisualStudio&logoColor=white"/><img src="https://img.shields.io/badge/Github-181717?style=flat&logo=Github&logoColor=white"/>

## 4. 개발일지

- 2022-11-03 fast api project start
- 2022-11-04 JWT 토큰 쿠키로 받아오는 방법 찾기
- 2022-11-05 쿠키에 담고, 로그인 유지가 dependency 추가, refactoring
- 2022-11-16 post 모델, 스키마 추가
- 2022-11-17 post list, retrieve 추가
- 2022-11-22 food 이미지 업로드 기능 추가 + cors issue
- 2022-11-23 food 이미지 기능 post로 이동, 이미지 업로드, 이미지 response 추가
- 2022-11-24 food & post 병합, url 수정

## 5. URL

### 5.1 auth_router URL
|CRUD|HTTP|URL|
|---|---|---|
|토큰 발행|POST|/auth/token|
|로그인|POST|/auth/login|
|로그아웃|GET|/auth/logout|
|유저 조회|GET|/auth/users|
|유저 생성|POST|/auth/users|
|내 정보 조회|GET|/auth/me|

### 5.2 food_router URL
|CRUD|HTTP|URL|
|---|---|---|
|게시글 전체 조회|GET|/food|
|게시글 생성|POST|/food|
|특정 게시글 조회|GET|/food/{food_id: int}|
|이미지 등록|POST|/food/img|
|게시글 이미지 조회|GET|/food/img/{post_id: int}|

## 6. UML

### 6.1 게시글 등록 시퀀스 다이어그램
<img src="https://user-images.githubusercontent.com/59391473/203673635-b713ffbb-410f-48b7-b2cb-1f19928afcbb.png" width="700" height="500"/>



### 6.2 로그인 시퀀스 다이어그램
<img src="https://user-images.githubusercontent.com/59391473/203673658-9ffdeb63-9db1-44d5-a536-2e61ae4c8a7d.png" width="700" height="500"/>


## 7. Database
### 7.1 Mysql DB 사용
### 7.2 Alembic 
- model 변화를 Alembic으로 DB에 적용

## 8.Trouble Shooting

### 8.1 게시글 등록 시 이미지 업로드 문제
- PostBase 스키마에 이미지 파일과 텍스트를 동시에 입력 할 때에 오류 발생
- 게시글을 등록 할 때에 title, description 입력과 이미지 등록 분리
- url 요청을 통해 이미지 업로드  

```python
@router.post("/img")
async def upload_img(request: Request, post_id: int, file: UploadFile, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
   
    contents = await file.read()
    with open(os.path.join(IMG_URL, file.filename), "wb") as fp:
        fp.write(contents)
    return post_crud.update_img(request=request, db=db, post_id=post_id, img_url=file.filename)
    
```
