from gtts import gTTS
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='1234',db="kiosk",charset="utf8")
cur = conn.cursor()

sql = "select name from product" //  SQL문   
cur.execute(sql) // 쿼리 실행 

for row in cur: 
    title = row[0] //제목
    content  = row[0] //내용
    language = "ko" //언어 (ko = 한국언어 발음) 

    tts = gTTS(t,lang=l)
    tts.save(f+".mp3")



