# HackMonitor – Daily Cybersecurity News Digest

HackMonitor is an automated tool that collects the latest technology and cybersecurity news from Hacker News and sends a daily email digest. The system tracks which links have already been sent, ensuring you only receive fresh and relevant content.

## Features

- **Web Scraping**: Automatically fetches top news articles from Hacker News.
- **Dynamic HTML Emails**: Generates visually appealing email summaries.
- **Local Storage**: Keeps track of already sent links to avoid duplicates.
- **Secure Credentials**: Uses environment variables for email login.
- **Scalable**: Ready for templates, asynchronous sending, and analytics.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/santtos0x1/HackMonitor.git
cd HackMonitor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set environment variables for your email credentials:

```bash
export EMAIL_USER="your_email@example.com"
export EMAIL_PASS="your_email_password"
```

## Usage

Run the application:

```bash
python __init__.py
```

The application will:

1. Fetch the latest news.
2. Generate an HTML digest.
3. Send the email to your configured address.
4. Update the local storage to avoid sending duplicates.
   
## File Structure

* `core/badge.py` – Provides badges for news items.
* `core/inf_get.py` – Fetches news from Hacker News.
* `core/mail_sender.py` – Sends emails with the digest.
* `storage/collector.py` – Stores sent links locally in `local_storage.json`.
* `template/digest.py` – Generates the HTML digest for emails.
* `docs/` – Documentation files (optional).
* `README.md` – Project README file.
* `main.py` – Entry point of the application.


## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for details.

## Contributing

Feel free to submit issues, fork the repository, or open pull requests. Suggestions to improve functionality or add new features are welcome!
