import redis as redis
from website import create_app

# Make the WSGI interface available at the top level so wfastcgi can get it.
app = create_app()  # create_app est declarer dans le fichier __init__.py
cache = redis.Redis(host='redis', port=6379)
wsgi_app = app.wsgi_app

if __name__ == '__main__':
    import os

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)
