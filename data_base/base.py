import sqlite3
from pathlib import Path


class DB:
    def __init__(self):
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT ,
            age INTEGER,
            genre TEXT,
            favorite TEXT,
            recommendation TEXT
        )
        ''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        genre TEXT
        )
        ''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        author TEXT NOT NULL,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        description TEXT NOT NULL DEFAULT none,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES categories(id) 
        )
        ''')


    def populate_tables(self):
        self.cursor.execute('''
        INSERT INTO info (name, age, genre, favorite, recommendation) VALUES 
        ("Bek", 21, "классика", "1984", "Над пропостью во ржи"),
        ("Сергей", 45, "психология", "Кант", "Мысли. Как побеждать в спорах")
        '''),
        self.cursor.execute('''INSERT INTO categories (genre) VALUES ("романтика")'''),
        self.cursor.execute('''INSERT INTO categories (genre) VALUES ("триллер")'''),
        self.cursor.execute('''INSERT INTO categories (genre) VALUES ("фэнтези")'''),
        self.cursor.execute('''INSERT INTO categories (genre) VALUES ("утопия")'''),
        self.cursor.execute('''
        INSERT INTO books (author, name, year, description, genre_id) VALUES
        ("Джейн Остин", "Гордость и предубеждение", 1813, "Романтическая история о развитии отношений между Элизабет Беннет и мистером Дарси в английском обществе начала 19 века.", 1),
        ("Лев Толстой", "Анна Каренина", 1877, "Эпическая история о женщине, по имени Анна Каренина, которая сталкивается с моральными дилеммами, любовными треугольниками и внутренним конфликтом.", 1),
        ("Уэлли Ламб", "Она все равно меня любит", 1992, "Поиск самоопределения и любви Долли Долорес Прайс, женщины, борющейся с депрессией и стремящейся найти свое место в мире.", 1 ),
        ("Джейн Остин", "Эмма", 1815, "Роман о молодой женщине, которая становится 'выдумщицей' и пытается сыграть сваху для своих друзей.", 1),
        ("Томас Харрис", "Молчание ягнят", 1988, "Классический триллер о агенте ФБР Клариссе Старлинг и психопате-убийце, Ганнибале Лекторе.", 2),
        ("Дж. Финн", "Девушка в поезде", 2015, "Роман о женщине, ставшей свидетелем преступления во время своего ежедневного путешествия на поезде.", 2),
        ("Гиллиан Флинн", "Исчезнувшая", 2012, "Психологический триллер о женщине, чья сестра исчезает, и ее попытках раскрыть правду.", 2 ),
        ("Гиллиан Флинн", "Жена", 2012, "Психологический триллер о женщине, которая вступает в игру с мужем, когда он становится главным подозреваемым в пропаже женщины.", 2),
        ("Дж. Р. Р. Толкин", "Властелин Колец", 1954, "Эпическая сага о путешествии фродо бэггинса, чтобы уничтожить Кольцо Всевластья.", 3),
        ("Джордж Мартин", "Песнь Льда и Огня", 1996, "Серия книг, на которой основан сериал 'Игра престолов', о борьбе за престол Железного трона.", 3),
        ("Питер С. Бретт", "Волшебный рассвет", 2008, "Первая книга серии 'Цикл Заката', о борьбе человечества с существами, выходящими из тьмы.", 3),
        ("Сьюзен Коэн", "Словно звезды", 2008, "Серия книг, в которой рассказывается о семье, обладающей способностью путешествовать в другие миры и изучать разные магические способности.", 3),
        ("Джордж Оруэлл", "1984", 1949, "Роман о мире, где правительство полностью контролирует общество, историю и человеческие мысли.", 4),
        ("Алдоус Хаксли", "О дивный новый мир", 1932, "Утопический роман о будущем, где люди рождаются и выращиваются в лабораториях, а общество разделено на касты.", 4),
        ("Рэй Брэдбери", "451 градус по Фаренгейту", 1953, "Роман о мире, где книги запрещены, и пожарные гасят огонь не пожаром, а книгами.", 4),
        ("Маргарет Этвуд", "Слепая крепость", 2003, "Роман о мире, где женщины подвергаются грубому обращению и лишаются всех прав, а главная героиня борется за свою свободу.", 4)
        ''')
        self.connection.commit()

    def get_recomendation(self):
        self.cursor.execute('SELECT * FROM info')
        return self.cursor.fetchall()


    def get_genre(self):
        self.cursor.execute('''
        SELECT * FROM categories 
        ''')
        return self.cursor.fetchall()

    def books_by_cat(self, cat_id):
        self.cursor.execute('''SELECT * FROM books WHERE genre_id = :cat_id''',
                            {cat_id : 'cat_id'})
        return self.cursor.fetchall()






if __name__ == "__main__":
    db = DB()
    db.create_table()
    db.populate_tables()
    db.get_recomendation()
