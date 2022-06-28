from flask_app import app
from flask_app.controllers import users, adventures
from flask_app.models import user, adventure

if __name__=="__main__":
    app.run(debug=True)