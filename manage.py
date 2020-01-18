from app import creat_app, db
from flask_script import Manager, Server


from app.models import Users,  post
from flask_migrate import Migrate, MigrateCommand

app = create_app()


manager = Manager(app)


migrate = Migrate(app, db)


# Create manager instance 
manager = Manager(app)

# Create migrate instance
migrate = Migrate(app, db)

manager.add_command('server', Server)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """
    Run the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post)


if __name__ == '__main__':
    manager.run()