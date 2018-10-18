"""
The `Flask <http://flask.pocoo.org/>`_ integration will add tracing to all requests to your Flask application.

This integration will track the entire Flask lifecycle including user-defined endpoints, hooks,
signals, and templating rendering.

To configure tracing::

    from ddtrace import patch_all
    patch_all(flask=True)

    from flask import Flask

    app = Flask(__name__)


    @app.route('/')
    def index():
        return 'hello world'


    if __name__ == '__main__':
        app.run()


You may also enable Flask tracing via ddtrace-run::

    DATADOG_PATCH_MODULES=flask:true ddtrace-run python app.py

"""

from ...utils.importlib import require_modules


required_modules = ['flask']

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from .middleware import TraceMiddleware
        from .patch import patch

        __all__ = ['TraceMiddleware', 'patch']
