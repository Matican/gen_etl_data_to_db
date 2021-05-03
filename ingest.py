# User instruction:
# ---Create postgres database like [stream_test] below
# ---Create postgres table like [transaction] below 
# ---Edit line 7, optionally.
# ---First, run mock_api.  
# ---Then, run this app.


import requests
import psycopg2

# Edit the number at end of the URL to specify number of rows 
with requests.get("http://127.0.0.1:5000/spin_the_yarn/1000", stream=True) as r:

    conn = psycopg2.connect(dbname="stream_test", user="postgres", password=".")
    cur = conn.cursor()
    sql = "INSERT INTO transactions (userid, userkey, amount) VALUES  (%s, %s, %s)"

    
    buffer = ""
    for chunk in r.iter_content(chunk_size=1):
        if chunk.endswith(b"\n"):
            t = eval(buffer)
            print(t)
            if t[2] > 900:
                print("Fine customer...!")
            cur.execute(sql, (t[0], t[1], t[2]))
            conn.commit()
            buffer = ""
        else: 
            buffer += chunk.decode()






