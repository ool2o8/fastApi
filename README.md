# foodiary ๐๐๐๐๐ญ

## 1. ํ๋ก์ ํธ ์ ์
   ### ๐ง ์ธ๋ ฅ๊ตฌ์ฑ
  + ๊ฐ์ธํ๋ก์ ํธ
  ### ๐ช ํ๋ก์ ํธ ๋ชฉ์ 
   + ์์์ ๋จน๊ธฐ ์  ์ฌ์ง ํ์์ ํ๋ ์ฌ๋๋ค์ด ๋ง๋ค. <br>
     ํ์ง๋ง ์ด๋ ์ดฌ์ํ ์ฌ์ง์ ๋งค๋ฒ ๊ฒ์ํ๋ ๊ฒฝ์ฐ๋ ๋๋ฌผ๊ณ  ์คํ ๋ฆฌ์ ์ฌ๋ฆฐ ์ฌ์ง์ ํ๋ฃจ๋ฉด ๋ด๋ ค๊ฐ๋ค.<br>
     ๋ํ ๊ฐค๋ฌ๋ฆฌ ์ ๋ฆฌ์ ๋ถ์ง๋ฐํ์ง ์์ ์ฌ๋๋ค์ ๊ฐค๋ฌ๋ฆฌ์์ ๋ค์ ์ฐพ์๋ณด๊ธฐ๋ ํ๋ค๋ค. <br>
     ์ธ์คํ๊ทธ๋จ๊ณผ ๊ฐ์ ์์ ๊ธฐ๋ฅ์ด ๋ค์ด๊ฐ์ง ์์ ๊ธฐ๋ก์ฉ ์ฑ์ด ํ์ํ๋ค๊ณ  ์๊ฐํ๋ค. <br>
   ### โ๏ธ ํ๊ฒฝ
   + ``` python3.10 ```
   + **Framework** : FastAPI
   + **Database** : Mysql + Pymysql + Sqlalchemy + alembic
   + **OS** : window

## 2. ๊ธฐ๋ฅ
- ๋ก๊ทธ์ธ & ๋ก๊ทธ์์
- ์์ ์ฌ์ง ์ผ๊ธฐ์ฅ

## 3. ์ฌ์ฉ ๊ธฐ์  
### 3.1   stack ๐ง
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=black"/><img src="https://img.shields.io/badge/SQlite-003B57?style=flat&logo=SQLite&logoColor=white"/><img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/>

### 3.2  tool โ
<img src="https://img.shields.io/badge/VisualStudio-5C2D91?style=flat&logo=VisualStudio&logoColor=white"/><img src="https://img.shields.io/badge/Github-181717?style=flat&logo=Github&logoColor=white"/>

## 4. ๊ฐ๋ฐ์ผ์ง

- 2022-11-03 fast api project start
- 2022-11-04 JWT ํ ํฐ ์ฟ ํค๋ก ๋ฐ์์ค๋ ๋ฐฉ๋ฒ ์ฐพ๊ธฐ
- 2022-11-05 ์ฟ ํค์ ๋ด๊ณ , ๋ก๊ทธ์ธ ์ ์ง๊ฐ dependency ์ถ๊ฐ, refactoring
- 2022-11-16 post ๋ชจ๋ธ, ์คํค๋ง ์ถ๊ฐ
- 2022-11-17 post list, retrieve ์ถ๊ฐ
- 2022-11-22 food ์ด๋ฏธ์ง ์๋ก๋ ๊ธฐ๋ฅ ์ถ๊ฐ + cors issue
- 2022-11-23 food ์ด๋ฏธ์ง ๊ธฐ๋ฅ post๋ก ์ด๋, ์ด๋ฏธ์ง ์๋ก๋, ์ด๋ฏธ์ง response ์ถ๊ฐ
- 2022-11-24 food & post ๋ณํฉ, url ์์ 

## 5. URL

### 5.1 auth_router URL
|CRUD|HTTP|URL|
|---|---|---|
|ํ ํฐ ๋ฐํ|POST|/auth/token|
|๋ก๊ทธ์ธ|POST|/auth/login|
|๋ก๊ทธ์์|GET|/auth/logout|
|์ ์  ์กฐํ|GET|/auth/users|
|์ ์  ์์ฑ|POST|/auth/users|
|๋ด ์ ๋ณด ์กฐํ|GET|/auth/me|

### 5.2 food_router URL
|CRUD|HTTP|URL|
|---|---|---|
|๊ฒ์๊ธ ์ ์ฒด ์กฐํ|GET|/food|
|๊ฒ์๊ธ ์์ฑ|POST|/food|
|ํน์  ๊ฒ์๊ธ ์กฐํ|GET|/food/{food_id: int}|
|์ด๋ฏธ์ง ๋ฑ๋ก|POST|/food/img|
|๊ฒ์๊ธ ์ด๋ฏธ์ง ์กฐํ|GET|/food/img/{post_id: int}|

## 6. UML

### 6.1 ๊ฒ์๊ธ ๋ฑ๋ก ์ํ์ค ๋ค์ด์ด๊ทธ๋จ
<img src="https://user-images.githubusercontent.com/59391473/203673635-b713ffbb-410f-48b7-b2cb-1f19928afcbb.png" width="700" height="500"/>



### 6.2 ๋ก๊ทธ์ธ ์ํ์ค ๋ค์ด์ด๊ทธ๋จ
<img src="https://user-images.githubusercontent.com/59391473/203673658-9ffdeb63-9db1-44d5-a536-2e61ae4c8a7d.png" width="700" height="500"/>


## 7. Database
### 7.1 Mysql DB ์ฌ์ฉ
### 7.2 Alembic 
- model ๋ณํ๋ฅผ Alembic์ผ๋ก DB์ ์ ์ฉ

## 8.Trouble Shooting

### 8.1 ๊ฒ์๊ธ ๋ฑ๋ก ์ ์ด๋ฏธ์ง ์๋ก๋ ๋ฌธ์ 
- PostBase ์คํค๋ง์ ์ด๋ฏธ์ง ํ์ผ๊ณผ ํ์คํธ๋ฅผ ๋์์ ์๋ ฅ ํ  ๋์ ์ค๋ฅ ๋ฐ์
- ๊ฒ์๊ธ์ ๋ฑ๋ก ํ  ๋์ title, description ์๋ ฅ๊ณผ ์ด๋ฏธ์ง ๋ฑ๋ก ๋ถ๋ฆฌ
- url ์์ฒญ์ ํตํด ์ด๋ฏธ์ง ์๋ก๋  

```python
@router.post("/img")
async def upload_img(request: Request, post_id: int, file: UploadFile, db: Session = Depends(get_db), dependencies=Depends(AuthProvider())):
   
    contents = await file.read()
    with open(os.path.join(IMG_URL, file.filename), "wb") as fp:
        fp.write(contents)
    return post_crud.update_img(request=request, db=db, post_id=post_id, img_url=file.filename)
    
```
