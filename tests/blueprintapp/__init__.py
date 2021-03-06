from flask import Flask

app = Flask(__name__)
from moduleapp.apps.admin import admin
from moduleapp.apps.frontend import frontend
app.register_blueprint(admin)
app.register_blueprint(frontend)
