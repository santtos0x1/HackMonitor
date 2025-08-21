from core import inf_get, mail_sender

class App:
    def __init__(self) -> None:
        pass
    
    def run(self) -> None:
        getNews:tuple = inf_get.getNews();
        mail_sender.Send(getNews)  # Send the news via email

if __name__ == "__main__":
    app:App = App()
    app.run()  # Start the application
