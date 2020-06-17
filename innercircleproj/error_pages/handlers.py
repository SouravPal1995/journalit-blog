from flask import Blueprint, render_template

error_bp = Blueprint('error_bp', import_name = __name__)

@error_bp.app_errorhandler(404)
def error_404(error):
    
    return render_template('errors/404.html'), 404

@error_bp.app_errorhandler(403)
def error_403(error):
    
    return render_template('errors/403.html'), 403