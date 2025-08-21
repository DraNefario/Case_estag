#run.py
from app.controllers.__init__ import create_app
from app.utils.create_db import create_db

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=False)