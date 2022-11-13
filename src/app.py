from flask import Flask
from config import config


#Routes
from routes import movieroutes

app = Flask(__name__)


def page_notfound(error):
    return "<h1>Not foung page</h1>"

if __name__=='__main__':
    app.config.from_object(config['development'])
    
    #Blueprints
    app.register_blueprint(movieroutes.main, url_prefix= '/api/movies')
    #Error handlers
    app.register_error_handler(404, page_notfound)
    app.run()
