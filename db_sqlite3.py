import sqlite3

try:
    # conn = sqlite3.connect("example.db")
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute("CREATE TABLE PROCESSOR (PROCESSOR_ACR TEXT, PROCESSOR_NAME TEXT)")
    c.execute("CREATE TABLE CLIENT (PROCESSOR_ACR TEXT, CLIENT_ACR TEXT, CLIENT_NAME TEXT)")
    c.execute("INSERT INTO PROCESSOR (PROCESSOR_ACR, PROCESSOR_NAME) VALUES (?,?)", ('SIX', 'SIX Group'))
    c.execute("INSERT INTO CLIENT (PROCESSOR_ACR, CLIENT_ACR, CLIENT_NAME) VALUES (?,?,?)", ('SIX', 'ZKB', None))
    c.execute("INSERT INTO CLIENT (PROCESSOR_ACR, CLIENT_ACR) VALUES (?,?)", ('SIX', 'BCV'))
    c.execute("select * from processor pr inner join client cli on pr.PROCESSOR_ACR = cli.PROCESSOR_ACR order by cli.CLIENT_ACR desc")
    print(c.description)
    while True:
        rec = c.fetchone()

        if not rec:
            break

        print(rec)

    c.close()
finally:
    conn.close()