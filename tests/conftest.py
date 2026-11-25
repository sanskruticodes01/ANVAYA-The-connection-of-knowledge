import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.database import get_db
from backend.main import app
from backend.models import Base

load_dotenv()

TEST_URL = os.getenv("DATABASE_URL").rsplit("/", 1)[0] + "/anvaya_test"
test_engine = create_engine(TEST_URL)
TestSession = sessionmaker(bind=test_engine)


@pytest.fixture()
def client():
    Base.metadata.create_all(test_engine)

    def override_get_db():
        db = TestSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
    Base.metadata.drop_all(test_engine)