
import unittest
from src.database import init_db, get_db_connection

class TestDatabase(unittest.TestCase):
    def test_init_db(self):
        init_db()
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Clients'")
            self.assertEqual(cursor.fetchone()[0], "Clients")

if __name__ == "__main__":
    unittest.main()
