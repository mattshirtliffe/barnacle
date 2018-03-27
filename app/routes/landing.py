from functools import wraps

from flask import render_template, request, jsonify, redirect, url_for, session, g

from app.forms import LeadForm


from flask import Blueprint

from app.models import User, Lead
from app.schema import LeadSchema

landing = Blueprint('landing', __name__)


def auth_user(f):
    @wraps(f)
    def func_wrapper(*args, **kwargs):

        try:
            auth_header = request.headers.get('Authorization')
            token = auth_header.split(" ")[1]
            user_id = User.decode_token(token)
            user = User.query.get(user_id)
            if user is None:
                bad_response = jsonify({
                    'message': user_id
                })
                bad_response.status_code = 401
                return bad_response
            g.user = user
        except Exception as e:
            print(e)
            bad_response = jsonify({
                'message': 'missing Authorization bearer token'
            })
            bad_response.status_code = 400
            return bad_response

        return f(*args, **kwargs)
    return func_wrapper


@landing.route('/', methods=['GET', 'POST'])
def index():
    form = LeadForm()
    if request.method == 'POST':

        if not form.validate_on_submit():

            # add form values to session
            session['form_data'] = form.data
            session['form_errors'] = form.errors
            return redirect(url_for('landing.index'))
        else:
            # valid form
            # add lead to database
            lead = Lead(form.email.data)
            lead.first_name = form.first_name.data
            lead.last_name = form.last_name.data
            lead.has_accepted_terms = True

            try:
                lead.save()
            except Exception as e:
                print(e)

            session['lead_created'] = True
            if 'form_data' in session:
                del session['form_data']
            if 'form_errors' in session:
                del session['form_errors']

            return redirect(url_for('landing.index'))
    else:

        if 'form_data' in session:
            form_data = session['form_data']
            form.first_name.data = form_data['first_name']
            form.last_name.data = form_data['last_name']
            form.email.data = form_data['email']
            form.phone.data = form_data['phone']

        if 'form_errors' in session:
            if 'first_name' in session['form_errors']:
                form.first_name.errors = session['form_errors']['first_name']
            if 'last_name' in session['form_errors']:
                form.last_name.errors = session['form_errors']['last_name']
            if 'email' in session['form_errors']:
                form.email.errors = session['form_errors']['email']

        return render_template('index.html', form=form)


@landing.route('/leads', methods=['GET'])
@auth_user
def get_leads():
    leads = Lead.query.all()
    schema = LeadSchema()
    results = schema.dump(leads,many=True)
    return jsonify(results)
