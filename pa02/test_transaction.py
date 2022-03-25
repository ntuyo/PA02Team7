'''
test_transaction runs unit and integration tests on the transaction module
'''

from cgitb import small
import pytest
from transaction import Transaction, to_transaction_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat0 = {'amount':'400','category':'loan','date':'2022-01-10','description':'loan for car'}
    cat1 = {'amount':'500','category':'bank','date':'2023-02-20','description':'loan for bank'}
    cat2 = {'amount':'600','category':'money','date':'2024-03-30','description':'loan for money'}
    id1=empty_db.add_transaction(cat0)
    id2=empty_db.add_transaction(cat1)
    id3=empty_db.add_transaction(cat2)
    yield empty_db
    empty_db.delete_transaction(id3)
    empty_db.delete_transaction(id2)
    empty_db.delete_transaction(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={'amount':100+i,
               'category':'categorya',
               'date':'202'+s+'-01-01',
                'description':'testing'}
        rowid = small_db.add_transaction(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete_transaction(rowids[j])

@pytest.mark.nazari
def test_nazaris_summary_date(small_db):
    rowids = []
    for i in range(10):
        s = str(i)
        cat ={'amount':100+i,
               'category':'categorya',
               'date':'202'+s+'-01-01',
                'description':'testing'}
        rowid = small_db.add_transaction(cat)
        rowids.append(rowid)
    sorted_date = small_db.summarize_transaction_by_date()
    trans1 = sorted_date[len(sorted_date)-1]
    assert trans1['date'] == "2029-01-01"
    trans2 = sorted_date[0]
    assert trans2['date'] == "2020-01-01"

@pytest.mark.nazari
def test_nazaris_summary_category(small_db):
    rowids = []
    for i in range(10):
        s = str(i)
        cat ={'amount':100+i,
               'category':'category'+s,
               'date':'2020-01-01',
                'description':'testing'}
        rowid = small_db.add_transaction(cat)
        rowids.append(rowid)
    for i in range(10):
        s = str(i)
        cat ={'amount':100+i,
               'category':'category'+s,
               'date':'2020-01-01',
                'description':'testing'}
        rowid = small_db.add_transaction(cat)
        rowids.append(rowid)
    sorted_date = small_db.summarize_transaction_by_category()
    trans1 = sorted_date[len(sorted_date)-2]
    assert trans1['category'] == "loan"
    trans2 = sorted_date[0]
    assert trans2['category'] == "bank"
    trans3 = sorted_date[1]
    assert trans3['category'] == "category0"
