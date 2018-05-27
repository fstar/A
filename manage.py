from flask_script import Manager

from app import app

manager = Manager(app)


if __name__ == "__main__":
    app.run("127.0.0.1", debug=True, threaded=True, port=6789)