class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "super secret key"


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False
    SECRET_KEY = "test"
