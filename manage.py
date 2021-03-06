
import os
import unittest

from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models

app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('./tests', pattern='*test.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def hello():
    "Just say hello"
    print('hello')


@manager.command
def create_admin():
    "create_admin"
    user =  models.User('me@matthewshirtliffe.co.uk','password1010')
    user.save()



if __name__ == '__main__':
    manager.run()