import os
import sys
import flask
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

# print(folder)
# print(sys.path)




app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)



def register_blueprints():
    from pypi_me.views import home_views
    from pypi_me.views import package_views
    from pypi_me.views import account_views
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(account_views.blueprint)



if __name__=='__main__':
    main()

