from core import inf_get, mail_sender
from storage import db_config
import logging

logging.basicConfig(filename="logs/app.log",level=logging.INFO,format="%(asctime)s - [ %(levelname)s ] - %(message)s")

class App:
    def __init__(self) -> None:
        # Initialize the database configuration
        self.dbConfig = db_config.DatabaseConfig()
        # Get the news data
        self.getNews:tuple = inf_get.getNews();

    
    def run(self) -> None:
        logging.info("Running the database configuration")
        self.dbConfig.run()  # Save news to the database
        mail_sender.Send(self.getNews)  # Send the news via email
        logging.info("Sending news via email")  

if __name__ == "__main__":
    app:App = App()
    app.run()  # Start the application
