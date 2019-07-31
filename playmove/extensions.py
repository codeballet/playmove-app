from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_wtf import CsrProtect

debug_toolbar = DebugToolbarExtension()
mail = Mail()
csrf = CsrfProtect()
