import psycopg2

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="etl_demo",
            user="postgres",
            password="postgres"
        )
        self.cursor = self.connection.cursor()

    def get_diagnosis(self, year):
        consulta = "SELECT diagnostico, COUNT(diagnostico) FROM diagnosis WHERE year=%s GROUP BY diagnostico;"
        self.cursor.execute(consulta, (year,))
        diagnosis = self.cursor.fetchall()
        return diagnosis

    def get_years(self):
        consulta = "SELECT  year FROM diagnosis GROUP BY year ORDER BY year;"
        self.cursor.execute(consulta)
        years = self.cursor.fetchall()
        years_list = []
        for year in years:
            years_list.append(year[0])
        return years_list

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()
