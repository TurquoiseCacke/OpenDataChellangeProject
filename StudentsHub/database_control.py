import sqlite3


def main():
    database = sqlite3.connect('database.db')
    cursor = database.cursor()
    cursor.execute('create table if not exists users(user_id text, action text, lang text, karma int)')
    cursor.execute('create table if not exists fill_q(user_id text, institution text, task text, photo text, '
                   'type_q text, category text, difficulty text)')
    cursor.execute('create table if not exists questions(q_id int, user_id text, institution text, task text, '
                   'photo text, type_q text, category text, difficulty text)')
    cursor.execute('create table if not exists fill_a(user_id text, institution text, answer text, '
                   'a_photo text, type_a text)')
    cursor.execute('create table if not exists stat(institution text, q_num int, a_num int)')
    cursor.execute('create table if not exists bad_quest(user_id text, q_id text)')
    cursor.execute('delete from users')
    # cursor.execute("insert into users values('390084519', 'action', 'lang', 13)")
    cursor.execute('select sql from sqlite_master')
    print(''.join(str(i)+'\n' for i in cursor.fetchall()))
    cursor.execute('select * from users')
    print(cursor.fetchall())
    database.commit()
    database.close()


if __name__ == '__main__':
    main()
