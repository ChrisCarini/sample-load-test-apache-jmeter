import time
from datetime import datetime

from flask import Flask, request


def create_app() -> Flask:
    # Create and configure the application instance
    app = Flask(__name__)

    # Sample endpoint w/ some artificial latency added
    @app.route('/fast')
    def fast():
        """ Just a test endpoint - should be fast. """
        return 'fast'

    # Sample endpoint w/ some artificial latency added
    @app.route('/slow')
    def slow():
        """ Just a test endpoint - should be kinda slow. """
        result = '{} - start\n'.format(datetime.now())
        for x in range(1, 11):
            result += '{} - {}^2 = {}\n'.format(datetime.now(), x, get_pow_2(x))
        result += '{} - end\n'.format(datetime.now())
        return result

    # Sample endpoint w/ some parameters
    @app.route('/params')
    def params():
        """ Just a test endpoint - should accept 'ldap' parameter."""
        ldap = request.args.get('ldap')

        return f'Computing some stuff for {ldap}...\n'

    return app


def get_pow_2(num):
    """ Get the square of a number, artificially slowing it down by 1ms"""
    time.sleep(0.1)
    value1 = pow_wrapper(num, 2) / 2
    value2 = pow_wrapper(num, 2) / 2
    return value1 + value2


def pow_wrapper(num, power):
    """ Artificially slow down pow() """
    time.sleep(0.2)
    return pow(num, power)


if __name__ == '__main__':
    create_app().run()
