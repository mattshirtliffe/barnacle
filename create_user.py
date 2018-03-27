import os

import click

from app import create_app, models

app = create_app(config_name=os.getenv('APP_SETTINGS'))

@click.command()
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def create_admin(email, password):
    "create_admin user"
    with app.app_context():
        user = models.User(email, password)
        user.save()


if __name__ == '__main__':
    create_admin()
