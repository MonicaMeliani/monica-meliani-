#!/usr/bin/env python
# coding: utf-8

# In[2]:


def conv_reamur(celcius):
    convert_reamur = 4 * celcius / 5
    return convert_reamur

def conv_farenheit(celcius):
    convert_farenheit = 9 * celcius / 5 + 32
    return convert_farenheit

def main():
    temperature = int(input('Masukan Skala Celcius: '))

    print(f'Hasil Konnversi Suhu {temperature} C adalah {conv_reamur(temperature)} Reamur')
    print(f'Hasil Konversi Suhu {temperature} C adalah {conv_farenheit(temperature)} Farenheit')

 
if __name__ =='__main__':
    main()


# In[6]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
if db.is_connected():
        print("Berhasil terhubung ke database")


# In[11]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE db_film")

print("Database berhasil dibuat!")


# In[22]:


import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = """CREATE TABLE tblfilm (
    kode_id INT AUTO_INCREMENT PRIMARY KEY,
    judulfilm VARCHAR(255),
    jenis_film varchar(255)
    
)
"""
cursor.execute(sql)
print("tabel film berhasil dibuat")


# In[24]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "INSERT INTO tblfilm (JudulFilm, Jenis_Film) VALUES (%s, %s)"
val = ("X-Men: Dark Phoenix", "Action")
cursor.execute(sql,val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[26]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "INSERT INTO tblfilm (JudulFilm, Jenis_Film) VALUES (%s, %s)"
values = [
    ("Aladdin", "Fantasy"),
    ("Godzilla II: King of the Monsters","Fantasy"),
    ("John Wick: Chapter 3 - Parabellum","Action")
]
     
for val in values:
    cursor.execute(sql,val)
    db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[28]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "SELECT * FROM tblfilm"
cursor.execute(sql)
     
results = cursor.fetchall()

for data in results:
    print(data)


# In[29]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "SELECT * FROM tblfilm"
cursor.execute(sql)
     
results = cursor.fetchone()

print(result)


# In[30]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "UPDATE tblfilm SET JudulFilm=%s, Jenis_Film=%s WHERE Kode_id=%s"
val = ("X-Men: Dark Phoenix", "Fantasy Action", 1)
cursor.execute(sql,val)

db.commit()

print("{} data diubah".format(cursor.rowcount))


# In[31]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)
cursor= db.cursor()
sql = "DELETE FROM tblfilm WHERE Kode_id=%s"
val = (1, )
cursor.execute(sql,val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))


# In[ ]:




