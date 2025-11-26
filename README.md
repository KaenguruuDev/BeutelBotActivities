# BeutelBotActivities

A tiny Flask application that supplies dynamic status text for my discord bot: [**BeutelBot**](https://bot.kaenguruu.dev) by serving it on [`https://activity.kaenguruu.dev/status`](https://activity.kaenguruu.dev/status).

Please note that this code is written to "just work". No effort was made to make this more modular than it had to be and is therefore not designed to be adopted for other users.


## Overview

* **Flask** serves a single endpoint: `/status`
* Every 5 minutes a background thread  
  * reloads all static status snippets from `VALUE`
  * executes any Python scripts in `dynamic-updaters/` (used to generate dynamic snippets in `dynamic/` that require calculations or API calls)
  * reads any one‑line files in `dynamic/`
  * randomly picks one snippet as the current status

## Project Structure

```
BeutelBotActivities/
├─ main.py               # The Flask app                 
├─ dynamic-updaters/     # Python scripts that add/remove snippets
│   └─ example.py        # CWD is the same as main.py; any packages must be inside same venv as `main.py`
├─ dynamic/              # One‑line files containing a single status
|   └─ EXAMPLE           # Dynamic files should be named according to the dynamic-updaters/ directory
└─ VALUE                 # Plain‑text file: one status per line
```

---


## License

This project is licensed under the **MIT License**. You can copy, distribute or modify this code in any way you need, as long as you credit me as the original author.

For more information, see [License](https://github.com/KaenguruuDev/BeutelBotActivities/blob/main/LICENSE).

## Author

**KaenguruuDev** – [Website](https://kaenguruu.dev) – [LinkedIn](https://www.linkedin.com/in/kaenguruu/) – <kaenguruu.dev@gmail.com>
