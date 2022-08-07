from logic.study.sqlalchemy.Database import Database
from ui.Window import Window

def main():
    database = Database()
    window = Window(database)
    window.run()

if __name__ == '__main__':
    main()