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
                    ('item #' int, amount int, category text, date Date, description text)''')

        con.commit()
        con.close()
        self.dbfile = dbfile

    # Gabby
    def quit(self):
        return

    #Jimkelly Done already
    def show_categories(self):
        return

    # Tiffany
    def add_category(self):
        return

    # Nazari
    def modify_category(self):
        return

    # Tiffany
    def show_transaction(self):
        return

    # Gabby
    def add_transaction(self,item):
        ''' add a transaction to the transaction table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        #cur.execute("INSERT INTO categories VALUES(?,?)",(item['name'],item['desc']))
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item #'],item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    # Jimkelly
    def delete_transaction(self,tranID):

        # go to the sql table based on the transaction ID 
        # find transID and remove ot from the SQL table 
       
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("DELETE FROM transactions WHERE 'item #'=(?)",(tranID,))
        con.commit()
        con.close()
        #cur.execute('''DELETE FROM categories WHERE rowid=(?); ''',(rowid,))
        

        # this things in the parenthesis is the actual sql code that deletes the transaction based on the ID
        # the code should go into the data base and based on the trans ID delete the whole row( each row is one transaction)
        

    # Nazari
    def summarize_transaction_by_date(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions GROUP BY date")
        # cur.execute('''SELECT
        #             date AS date,
        #             EXTRACT(date FROM transaction_date) AS Date,
        #             SUM(money) OVER(PARTITION BY EXTRACT(year FROM transaction_date)) AS money_earned
        #             FROM data''')
        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)

    # Gabby
    def summarize_transaction_by_month(self):
        return

    # Jimkelly
    def summererise_transaction_by_year(self,yearID):

        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions GROUP BY date")
        # cur.execute('''SELECT
        #             date AS date,
        #             EXTRACT(date FROM transaction_date) AS Date,
        #             SUM(money) OVER(PARTITION BY EXTRACT(year FROM transaction_date)) AS money_earned
        #             FROM data''')
        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)
        
    

    # Nazari
    def summarize_transaction_by_category(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT 'item #',* from transactions groupby category")
        rows = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(rows)

    # Tiffany
    def print_this_menu(self):
        return