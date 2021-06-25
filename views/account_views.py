import flask

from pypi_me.helper.view_modifiers import response
import pypi_me.services.package_service as package_service


blueprint = flask.Blueprint('account',__name__, template_folder='templates')




@blueprint.route('/account/login', methods = ['GET'])
@response(template_file='account/login.html')
def login_user():
    return {}




@blueprint.route('/account/register', methods = ['GET'])
@response(template_file='account/register.html')
def register_get():
    return {}

@blueprint.route('/account/register', methods = ['POST'])
@response(template_file='account/register.html')
def register_post():
    return {}