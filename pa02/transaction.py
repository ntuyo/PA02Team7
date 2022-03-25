import sqlite3

# 'item #','amount','category','date','description'

def to_transaction_dict(trans_tuple):
    ''' transaction is a transaction tuple ('item #','amount','category','date','description')'''
    transaction = {'item #':trans_tuple[0], 'amount':trans_tuple[1], 'category':trans_tuple[2], 'date':trans_tuple[3], 'description':trans_tuple[4]}
    return transaction

def to_transaction_dict_list(trans_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_transaction_dict(trans) for trans in trans_tuples]

class Transaction():
    def __init__(self,dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions 
                    (amount int, category text, date Date, description text)''')

        con.commit()
        con.close()
        self.dbfile = dbfile


    def transaction_select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(tuples)

    # Gabby
    def add_transaction(self,item):
        ''' add a transaction to the transaction table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #cur.execute("INSERT INTO categories VALUES(?,?)",(item['name'],item['desc']))
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    # Jimkelly Done
    def delete_transaction(self,rowid):

        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()
        

    ###################
    # Nazari's Method #
    ###################
    def summarize_transaction_by_date(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions GROUP BY date")
        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)

    # Gabby's method
    def summarize_transaction_by_month(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* FROM transactions ORDER BY substring(date,6,8)")
        #cur.execute("SELECT rowid,* from transactions GROUP BY CAST(strftime('%m', date) AS INTEGER)")
        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)

    # Jimkelly Done
    def summererise_transaction_by_year(self):

        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()

        #cur.execute("SELECT rowid,* from transactions GROUP BY CAST(strftime('%y', date) AS INTEGER)")
        cur.execute("SELECT rowid,* FROM transactions ORDER BY substring(date,0,4)")

        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)
        
    

     ###################
    # Nazari's Method #
    ###################
    def summarize_transaction_by_category(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions order by category")
        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)

    # Tiffany
    def print_this_menu(self):
        return
