from app import create_app
from config import config
import os

# Get the configuration based on the FLASK_ENV environment variable
app_config = config[os.environ.get('FLASK_ENV', 'default')]

# Create the Flask app
app = create_app(config_object=app_config)

if __name__ == '__main__':
    app.run()