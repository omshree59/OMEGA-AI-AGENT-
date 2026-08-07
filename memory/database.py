import sqlite3


class Database:

    def __init__(self):

        self.conn = sqlite3.connect("omega_memory.db")

        self.create_table()



    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS memories(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            information TEXT,

            category TEXT

        )
        """

        self.conn.execute(query)
        self.conn.commit()



    def add_memory(self, information, category):

        # Check duplicate memory
        check_query = """
        SELECT * FROM memories
        WHERE information = ?
        """

        existing = self.conn.execute(
            check_query,
            (information,)
        ).fetchone()


        # Already exists
        if existing:
            return



        query = """
        INSERT INTO memories(information, category)
        VALUES (?,?)
        """


        self.conn.execute(
            query,
            (
                information,
                category
            )
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
            (
                "%" + keyword + "%",
            )
        )


        return result.fetchall()



    def clear_memory(self):

        query = """
        DELETE FROM memories
        """


        self.conn.execute(query)

        self.conn.commit()