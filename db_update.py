import psycopg2
import os


class DBUpdate:
    def __init__(self):
        self.server_parameters = open("server_parameters", "r").read()
        self.abs_path = os.path.dirname(os.path.abspath(__file__))

    def run(self):
        # self.replace_all()
        self.replace_data()
        pass

    def replace_all(self):
        drop_commands = self.get_commands("xwm_python_postgres_commands/xwm_drop_commands")
        create_commands = self.get_commands("xwm_python_postgres_commands/xwm_create_commands")
        import_commands = self.get_commands("xwm_python_postgres_commands/xwm_import_csv_commands")

        conn = None

        try:
            conn = psycopg2.connect(self.server_parameters)
            cur = conn.cursor()

            for command in drop_commands:
                cur.execute(command)

            for command in create_commands:
                cur.execute(command)

            for command in import_commands:
                cur.execute(command)

            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

    def replace_data(self):
        truncate_commands = self.get_commands("xwm_python_postgres_commands/xwm_truncate_commands")
        import_commands = self.get_commands("xwm_python_postgres_commands/xwm_import_csv_commands")

        conn = None

        try:
            conn = psycopg2.connect(self.server_parameters)
            cur = conn.cursor()

            for command in truncate_commands:
                cur.execute(command)

            for command in import_commands:
                cur.execute(command)

            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                conn.close()

    def get_commands(self, file_path):
        file = open(file_path, "r")
        string = file.read().rstrip().rstrip(";").replace("RELATIVE_PATH", self.abs_path)
        file.close()
        commands = string.split(";")
        return commands


if __name__ == '__main__':
    main = DBUpdate()
    main.run()
