import sqlite3

# 'item #','amount','category','date','description'

def to_transaction_dict(trans_tuple):
    ''' transaction is a transaction tuple ('item #','amount','category','date','description')'''
    transaction = {'item #':trans_tuple[0], 'amount':trans_tuple[1], 'category':trans_tuple[2], 'date':trans_tuple[3], 'description':trans_tuple[4]}
    return transaction

def to_transaction_dict_list(trans_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_transaction_dict(cat) for cat in trans_tuples]

class Transaction():
    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transaction
                    (name text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    # Gabby
    def quit(self):
        return

    #Jimkelly
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
    def add_transaction(self):
        return

    # Jimkelly
    def delete_transaction(self):
        return

    # Nazari
    def summarize_transaction_by_date(self):
        return

    # Gabby
    def summarize_transaction_by_month(self):
        return

    # Jimkelly
    def summererise_transaction_by_year(self):
        return

    # Nazari
    def summarize_transaction_by_category(self):
        return

    # Tiffany
    def print_this_menu(self):
        return