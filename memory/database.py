import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("omega_memory.db")
        self.create_table()


    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS memories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            information TEXT NOT NULL,
            category TEXT NOT NULL
        )
        """

        self.conn.execute(query)
        self.conn.commit()



    def add_memory(self, information, category):

        # Check if memory already exists
        check_query = """
        SELECT * FROM memories
        WHERE information = ?
        AND category = ?
        """

        existing = self.conn.execute(
            check_query,
            (information, category)
        ).fetchone()


        # Save only if memory is new
        if existing is None:

            query = """
            INSERT INTO memories(information, category)
            VALUES (?, ?)
            """

            self.conn.execute(
                query,
                (information, category)
            )

            self.conn.commit()



    def get_memories(self):

        query = """
        SELECT information, category
        FROM memories
        ORDER BY id DESC
        """

        result = self.conn.execute(query)

        return result.fetchall()



    def search_memory(self, keyword):

        query = """
        SELECT information, category
        FROM memories
        WHERE information LIKE ?
        """

        result = self.conn.execute(
            query,
            (f"%{keyword}%",)
        )

        return result.fetchall()



    def get_memories_by_category(self, category):

        query = """
        SELECT information, category
        FROM memories
        WHERE category = ?
        """

        result = self.conn.execute(
            query,
            (category,)
        )

        return result.fetchall()



    def delete_memory(self, memory_id):

        query = """
        DELETE FROM memories
        WHERE id = ?
        """

        self.conn.execute(
            query,
            (memory_id,)
        )

        self.conn.commit()



    def clear_memory(self):

        query = """
        DELETE FROM memories
        """

        self.conn.execute(query)
        self.conn.commit()



    def close(self):

        self.conn.close()