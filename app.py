from app import create_app
from config import config
import os

app_config = config[os.environ.get('FLASK_ENV', 'default')]

app = create_app(config_object=app_config)

if __name__ == '__main__':
    app.run()