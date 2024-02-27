import math
import sqlite3


class AlgorithmDatabase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database/algorithms.db")
        self.cursor = self.connection.cursor()

    def append_database(self, algorithm, time_complexity, grid_size, sorting_time):
        self.cursor.execute(f"INSERT INTO algorithms VALUES ('{algorithm}', '{time_complexity}', {grid_size}, {sorting_time})")
        self.connection.commit()

    def clear_database(self):
        self.cursor.execute("DELETE FROM algorithms")
        self.connection.commit()

    def get_results(self):
        self.cursor.execute("SELECT * FROM algorithms")
        self.results = self.cursor.fetchall()
        self.connection.commit()
        return self.results

    def get_time_data(self):
        self.cursor.execute("SELECT algorithm, grid_size, sorting_time FROM algorithms WHERE sorting_time = (SELECT MAX(sorting_time) FROM algorithms)")
        slowest_algorithm = self.cursor.fetchall()

        self.cursor.execute("SELECT algorithm, grid_size, sorting_time FROM algorithms WHERE sorting_time = (SELECT MIN(sorting_time) FROM algorithms)")
        fastest_algorithm = self.cursor.fetchall()

        return slowest_algorithm + fastest_algorithm

    def get_avg_sorting_time(self, algorithm, grid_size):
        self.cursor.execute("SELECT AVG(sorting_time) FROM algorithms WHERE algorithm = ? AND grid_size = ?", (algorithm, grid_size),)
        average_sorting_time = self.cursor.fetchone()[0]
        self.connection.commit()
        return average_sorting_time


testdb = AlgorithmDatabase()

print(testdb.get_time_data())
