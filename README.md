# Python-gTTS

DB에 저장된 텍스트 데이터를 gTTS로 텍스트를 음성 데이터(MP3)로 변환 

- DB: MySQL

### 사용법 


리포지토리 clone
```
$ git clone https://github.com/tuioe5679/Python-gTTS.git
$ cd Python-gTTS
```

라이브러리 설치 
```
$ pip install gtts
$ pip install pymysql 
```

DB 연결 코드 변경 
```python 
conn = pymysql.connect(host='localhost',user='(유저이름)',passwd='(비밀번호)',db="(스키마)",charset="utf8")
cur = conn.cursor()

sql = "select (검색 열) from (테이블 이름)" // 쿼리문 작성    

```
