import pg8000

conn = pg8000.connect(host='192.168.0.105', user='prin', password='Cisc0123', database='dev_info')
cursor = conn.cursor()
cursor.execute("create table config_md5(ip varchar(40), config varchar(99999), md5 varchar(999))")

conn.commit()