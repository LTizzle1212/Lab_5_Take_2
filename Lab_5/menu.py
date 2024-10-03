"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3


# TODO create database table OR set up Peewee model to create table

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')

db = 'first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:  # this will connect or create new for a database
        conn.execute('CREATE TABLE IF NOT EXISTS records (record int, name text)')
    conn.close()  # always need to close

def display_all_records():
    conn = sqlite3.connect(db)
    search_results = conn.execute('SELECT * FROM records')  # this will save the results as a variable
    print('All records ')
    conn.close()

def search_by_name():
    onn = sqlite3.connect(db)
    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')

def add_new_record():
    new_record = str(input('Enter new record: '))  # a new record needs to be added to the database
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records VALUES (?)', (new_record,))
    conn.close()

def edit_existing_record():
    record_name = input('Which record would you like to update? ')
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE records SET name = ?', (record_name,))
    conn.close()

def delete_record(record_name):  # a parameter in the function
    with sqlite3.connect(db) as conn:  # making an argument
        conn.execute('DELETE from RECORDS WHERE name = ?', (record_name,))
    conn.close()

if __name__ == '__main__':
    main()

# Need these to create the functions
create_table()
display_all_records()
search_by_name()
add_new_record()
edit_existing_record()
delete_record()