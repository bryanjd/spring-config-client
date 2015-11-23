from flask import Flask, config
from springboot import EnableAutoConfiguration

app = Flask(__name__)

EnableAutoConfiguration(app, appname='foo', profile='production')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run()
