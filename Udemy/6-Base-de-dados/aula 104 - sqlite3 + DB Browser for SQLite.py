"""sqlite3 + DB Browser for SQLite"""

import sqlite3
# Usar DB Browser(S)


class ScheduleDB:  # Agenda
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, phone):  # Insere dados no DB
        query = 'INSERT OR IGNORE INTO schedule (name, phone) VALUES (?, ?)'
        self.cursor.execute(query, (name, phone))
        self.conn.commit()

    def edit(self, name, phone, id):  # Edita usando o id(índice)
        query = 'UPDATE OR IGNORE schedule SET'
        'name = ?, phone = ? WHERE id = ?'
        self.cursor.execute(query, (name, phone, id))
        self.conn.commit()

    def delete(self, id):  # Deleta usando o id(índice)
        query = 'DELETE FROM schedule WHERE id = ?'
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def lists(self):  # Itera sobre os dados do DB
        self.cursor.execute('SELECT * FROM schedule')

        for line in self.cursor.fetchall():
            print(line)

    def search(self, value):  # Exibi os dados baseado no nome
        query = 'SELECT * FROM schedule WHERE name LIKE ?'
        self.cursor.execute(query, (f'%{value}%',))

        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    schedule = ScheduleDB('schedule.db')

    # schedule.insert('Igor', '40028922')
    # schedule.insert('Michele', '123456768')
    # schedule.insert('Noah', '12332156')
    # schedule.insert('Alice', '12234441')

    # schedule.insert('Noah Freitas', '12333156')
    # schedule.insert('Noah Almeida', '12355156')
    # schedule.insert('Luiz Noah', '12399156')
    # schedule.insert('R. Noaha', '12399156')
    # schedule.search('Noah')
