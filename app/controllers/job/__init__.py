from flask import Blueprint

jobs = Blueprint('jobs', __name__)

from .. import libs, db
from . import views
from ...models import Job