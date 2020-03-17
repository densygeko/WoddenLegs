import Number
import DB_Connection
import sqlite3
class DB_Number(object):

    DB_Connection.DB_Connection.db_check()
    
    def insert_querry_all(path,identifier,id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
          """ INSERT INTO Number (path,identifier,id_rawdata) VALUES (?,?,?);
            """, (path,identifier,id_rawData))
        conn.commit()
        conn.close()

    def find_all():
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "Select * From Number"
            )
        NM_list = []
        rows = c.fetchall()
        for x in rows:
            NM = Number.Number(x[0],x[1],x[2],x[3])
            NM_list.append(NM)

        conn.close()
        return NM_list

    def find_by_ID(id):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute(
            "SELECT * FROM Number Where id= ?",(id,)
            )
        rows = c.fetchall()
        NM = Number.Number(rows[0][0], rows[0][1], rows[0][2], rows[0][3])
        conn.close()
        return NM

    def update_on_id(id, path, identifier, id_rawData):
        conn = sqlite3.connect('dbwoddenlegs.db')
        c = conn.cursor()
        c.execute("""UPDATE Number SET path= ?, identifier = ?, id_rawData= ? WHERE id= ?;""",(path, identifier, id_rawData,id,))
        conn.commit()
        conn.close()
