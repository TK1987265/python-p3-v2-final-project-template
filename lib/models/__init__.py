import sqlite3
# lib/models/__init__.py
from .base import Base, Session  # Adjust these imports as necessary
from .wrestlers import Wrestler
from .team_model import Team

__all__ = ['Base', 'Session', 'Wrestler', 'Team']

# from team_model import Wrestler, Team, SessionLocal
CONN = sqlite3.connect('wrestling.db')
CURSOR = CONN.cursor()
