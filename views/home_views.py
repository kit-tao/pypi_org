import flask

from pypi_org.helper.view_modifiers import response
import pypi_org.services.package_service as package_service


blueprint = flask.Blueprint('home',__name__, template_folder='templates')




@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_package_list()
    return {'packages': test_packages}
    # return render_template('index.html', packages=get_package_list())


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    # return render_template('about.html', packages=get_package_list())    
    return {}