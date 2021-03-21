# Ai Line Art Web App
A web application where a user can upload image and generate line art portrait.

## Download
```
cd && git clone https://github.com/kenxdrgn/Ai-Line-Art-Web-App && cd Ai-Line-Art-Web-App
```

## Optional (Backend)
The best practice for your project is to use a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

## Installation (Backend with virtualenv)
```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Installation (Backend without virtualenv)
```
cd backend
pip install -r requirements.txt
python app.py
```

## Installation (Frontend)
```
cd frontend
npm ci && npm run dev
```

## Credits
Almost all the backend code was from [Unpaired Portrait Drawing Generation via Asymmetric Cycle Mapping (CVPR 2020)](https://github.com/yiranran/Unpaired-Portrait-Drawing)
