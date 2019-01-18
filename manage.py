from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask import render_template

# 测试
app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell():
    return {'app': app, 'db': db}

manager.add_command('shell', Shell(make_context=make_shell))
manager.add_command('db', MigrateCommand)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    manager.run()
