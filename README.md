# Covid-Tracker-Madurai

A simple, lightweight Flask web app that scrapes public sources to show COVID-19 statistics for Tamil Nadu and global aggregates, and displays recent tweets from a public Twitter account. This repository contains the original project files and a small templated UI built with Jinja2 templates.

## Why this project

This project was created as a local tracker to surface COVID-19 numbers and related updates. It demonstrates a compact Flask app, HTML templating, and basic web scraping using BeautifulSoup. The code is educational and a starting point for modernizing or improving data sources (for example, replacing scraping with official APIs).

## Features

- Flask-based web server with multiple routes:
  - `/` — Home dashboard showing Tamil Nadu and global stats (scraped from Wikipedia)
  - `/news` — Recent tweets scraped from a public Twitter account (may be fragile)
  - `/about`, `/virus`, `/lol` — Additional static pages
- Simple scraping with BeautifulSoup and lxml
- Jinja2 templates in the `templates/` folder for easy UI updates

## Project structure

```
Covid-Tracker-Madurai/
├── app.py                 # Main Flask application
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .gitignore             # Common ignores for Python projects
└── templates/
	 ├── base.html
	 ├── home.html
	 ├── index.html
	 ├── about.html
	 ├── lol.html
	 └── virus.html
```

Notes:
- `app.py` performs scraping at import time; for production you should avoid long-running network calls during import and instead fetch data on demand or via background jobs.
- The `templates/` folder contains the HTML used by the routes.

## Quick demo (what you'll see)

- Home (`/`) — Latest scraped totals for Tamil Nadu and global aggregates
- News (`/news`) — A simple list of tweet texts parsed from a public Twitter timeline (scraping, not API-based)

## Installation (macOS / Linux / Windows WSL)

1. Clone the repository:

	git clone https://github.com/<your-username>/Covid-Tracker-Madurai.git
	cd Covid-Tracker-Madurai

2. Create and activate a virtual environment (recommended):

	# macOS / Linux
	python3 -m venv venv
	source venv/bin/activate

	# Windows (PowerShell)
	python -m venv venv
	.\venv\Scripts\Activate.ps1

3. Install dependencies:

	pip install -r requirements.txt

4. Run the app:

	# Option A: with Flask CLI
	export FLASK_APP=app.py
	export FLASK_ENV=development  # optional
	flask run

	# Option B: directly with Python
	python app.py

Then open http://127.0.0.1:5000/ in your browser.

## Important notes and limitations

- Scraping Twitter by parsing HTML is fragile and may break if Twitter changes its markup or restricts access. For reliable, long-lived apps, use the Twitter API or an authorized data provider.
- Scraping Wikipedia for critical numbers is also brittle. Prefer official data sources or APIs.
- `app.py` performs network calls at import time which will slow startup and may fail if network access is unavailable. Consider refactoring to lazy-load or poll in a background task.

## Security & Privacy

- This project scrapes only publicly available pages. Do not use it to access private or protected data. If you plan to deploy this app, make sure to follow rate limits and terms of service for the sites you query.

## Contributing

Small, focused improvements are welcome. Suggested next steps:

- Refactor scraping into functions and add caching
- Replace HTML scraping of Twitter with the official API
- Add unit tests around parsing logic

When contributing, open an issue first to discuss scope and approach.

## Development checklist / contract

- Input: HTTP requests to the Flask routes
- Output: Rendered HTML pages using template variables from scraped data
- Error modes: Network failures when scraping (app should handle gracefully)

Edge cases to consider:
- No network or target site unreachable
- Unexpected HTML structure causing parsing failures
- Slow scraping causing timeouts or blocking the server

## License

This repository does not include a license by default. If you want to make it open-source, add a LICENSE file (MIT is a permissive choice).

## Credits

Original author: (your original name) — this README modernizes and documents the project for easier reuse.

---

If you'd like, I can also:

- add a pinned `requirements.txt` (I will add one now),
- create a `.gitignore` (added), or
- refactor `app.py` to avoid doing network calls at import time and make the project more robust.

Tell me which of the follow-ups you'd like and I'll implement them.
