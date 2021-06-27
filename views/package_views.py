import flask

from pypi_org.helper.view_modifiers import response
import pypi_org.services.package_service as package_service


blueprint = flask.Blueprint('packages',__name__, template_folder='templates')




@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    # test_packages = package_service.get_package_list()
    return f"Package details for {package_name} "
    # return render_template('index.html', packages=get_package_list())



# syntax int:rank case value to integer.  If value is not integer, url error will be returned
@blueprint.route('/<int:rank>')
# @response(template_file='packages/details.html')
def package_list(rank: int):
    # test_packages = package_service.get_package_list()
    return f"Package details for {rank}th most popular packages "
    # return render_template('index.html', packages=get_package_list())