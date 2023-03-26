import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()

# Get the Heroku assigned port number and use it to start the server
port = int(os.environ.get('PORT', 8000))
application.run(host='0.0.0.0', port=port)
