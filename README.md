# METAR API

This API returns the latest weather information when provided with a specific METAR station code, which also uses caching with the help of Redis.

## Installation Steps

### 1. Clone the project, and navigate to the project folder.
```bash
  git clone https://github.com/vinaysurtani/METAR_API.git
```

### 2. Create a Virtual Environment
To isolate the project dependencies, it's recommended to create a virtual environment. Run the following command to create a new virtual environment named env:

```bash
python -m venv env
```

### 3. Activate the Virtual Environment
Activate the virtual environment using the following command:

```bash
source env/bin/activate
```

### 4. Install Project Dependencies
Use pip to install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 5. Start the Server
Change the directory to the 'metar' folder and run the server:

```bash
cd metar
python manage.py runserver
```

### 6. Start Redis Server (Caching)
In order for caching to work, you'll need to run a Redis server in a separate terminal. If you don't have Redis installed, you can install it using Homebrew:

```bash
brew install redis
```

Start the Redis server:
```bash
redis-server
```

### 7. Access the Web API
With the server and Redis running, you can now access the web API and test it using the following URLs:

* Ping the server to check if it's running:
http://127.0.0.1:8000/metar/ping

* Retrieve METAR information for a specific station (replace KSGS with the desired station code):
http://127.0.0.1:8000/metar/info/?scode=KSGS&nocache=0

* To force a cache refresh and get the latest data, set nocache=1:
http://127.0.0.1:8000/metar/info/?scode=KSGS&nocache=1

**Note** : Both the scode (station code) and nocache parameters are required for the proper functionality of the API.