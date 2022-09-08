from db import session
from model import TestUserTable

print(session.query(TestUserTable).all())
