import sqlite3
from core.inf_get import getNews
from core.badge import badgeGiver

class DatabaseConfig:
    def __init__(self):
        self.db = sqlite3.connect('storage/hackmonitor.db')
        self.cursor = self.db.cursor()
    
    def run(self):
        badges = badgeGiver()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS news (
                            id INTEGER PRIMARY KEY,
                            title TEXT,
                            link TEXT,
                            time TEXT,
                            badge TEXT
                            )''')
        listOfNews = getNews()
        titles, links, times, _ = listOfNews
        for (title, link, time), badge in zip(zip(titles, links, times), badges):
            if link.startswith('item?'):
                continue        
            self.cursor.execute('SELECT * FROM news WHERE title = ?', (title,))
            if self.cursor.fetchone() is None:  # Check if the news already exists
                self.cursor.execute('''INSERT INTO news (
                                    title,
                                    link,
                                    time,
                                    badge) VALUES (?, ?, ?, ?)''', (title, link, time, badge)) 
        self.db.commit()