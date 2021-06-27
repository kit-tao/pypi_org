import os
import sys



# Make it run more easily outside of PyCharm
sys.path.insert(
    0
    ,os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    )

# print(sys.path)

import pypi_org
import pypi_org.data.db_session as db_session

import pypi_org.data.package as Package




# import data.db_session


# factory = None

def setup_db():
    db_file = os.path.join(os.path.dirname(__file__),'sqlite_db','pypi.sqlite')
    print(db_file)
    db_session.global_init(db_file)
    insert_a_package()

def insert_a_package():
    p = Package()
    p.id = input("Package id/name:").strip().lower()

    


if __name__ == '__main__':
    setup_db()


