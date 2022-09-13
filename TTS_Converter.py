from gtts import gTTS
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='1234',db="kiosk",charset="utf8")
cur = conn.cursor()

sql = "select name from product"
cur.execute(sql)

try:
    for row in cur:
            f = row[0]
            t = row[0]
            l = "ko"

            tts = gTTS(t,lang=l)
            tts.save(f+".mp3")
except KeyboardInterrupt:
    pass
		


