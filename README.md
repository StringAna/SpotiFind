# SpotiFind

Get paired with users who vibe to the same songs as you. Whether it’s that catchy pop hit or a soulful indie track, find friends who share your music taste instantly.

## Overview

SpotiFind is a web application that helps users find friends based on their music taste using Spotify data. It analyzes user listening habits and recommends potential connections with similar musical preferences.

**Note:** This project is currently under development. The current version serves as a frontend prototype to demonstrate the planned user interface and core functionality.

## Current Status

✅ Implemented:

- Spotify OAuth Authentication
- Basic Navigation System
- Homepage Layout
- User Session Management
- Frontend Prototype

🚧 In Development:

- Music Taste Analysis Algorithm
- Friend Recommendation System
- User Profile Dashboard
- Social Connection Features

## Features

- OAuth 2.0 authentication with Spotify
- User profile visualization
- Music taste analysis
- Friend recommendations
- Real-time music data synchronization

## Tech Stack

- Python 3.8+
- Streamlit
- Spotify Web API
- SQLite/PostgreSQL (for user data storage)
- SDV (for synthetic data generation)

## Project Structure

```
SpotiFind/
├── README.md
├── requirements.txt
├── app.py                    # Main application entry point
├── components/              # UI components
│   ├── __init__.py
│   ├── login.py            # Login handling
│   └── home_page.py        # Home page layout
├── services/               # Business logic
│   ├── __init__.py
│   └── spotify.py          # Spotify API integration
├── models/                 # Data models
│   └── user.py            # User data structures
├── assets/                # Static resources
│   └── user_data_hardcoded.json  # Sample data
└── tests/                 # Unit tests
    └── __init__.py
```

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/SpotiFind.git
cd SpotiFind
```

2. **Create Virtual Environment**

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure Spotify API**

- Create a Spotify Developer account
- Register your application
- Add callback URL, for example: `http://localhost:8501`
- Copy Client ID and Secret to environment variables

5. **Run the Application**

```bash
streamlit run app.py
```

## Environment Variables

```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:8501
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License

## Contact

Developers - Ankit Kumar, Antara Tewary, Lingyun Dai

Project Link: https://stringana.github.io/SpotiFind/
