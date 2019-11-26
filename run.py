from app import app
from app.tasks.views import *

if __name__== '__main__':
    app.run(debug=True)