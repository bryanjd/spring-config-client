from flask import Flask
from springboot import EnableAutoConfiguration
from os import getenv

app = Flask(__name__)

EnableAutoConfiguration(app, appname='foo', profile='production', config_server=getenv('CONFIG_SERVER', None))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.debug = True
    app.run()
