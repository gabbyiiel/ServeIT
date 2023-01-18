from flask import render_template, request, flash, redirect, session, url_for, get_flashed_messages
from . import bp_dashboard
from ServeIT import s3, S3_BUCKET, UPLOAD_FOLDER
from ServeIT.auth.auth import login_required
from ServeIT.models.dbUtils.UserRepo import UserRepo
from ServeIT.models.dbUtils.ServicesRepo import Services
from ServeIT.Services.forms.ServicesForm import PrintForm, GcashForm
import cloudinary, cloudinary.uploader
from cloudinary.uploader import upload
import boto3, logging, os, tempfile
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename


@bp_dashboard.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    print(get_flashed_messages())
    rqdata = Services.display_request()
    print(rqdata)
    userID = session.get('user_id')
    data = UserRepo.get_current_user(userID)
    requestcount = Services.count_requests()
    created_request = Services.count_user_requests(userID)
    user_request = Services.get_user_requests(userID)
    print(user_request)
    title = 'Dashboard'
    fname = UserRepo.get_fname(userID)
    pform = PrintForm()
    gform = GcashForm()
    if data:
        return render_template("dashboard/dashboard.html", rqlist=rqdata, title=title, fname=fname, pform=pform, gform=gform,user=data, rq=requestcount, crequest=created_request, urequest=user_request)
    else:
        return "Error: Could not retrieve user data"
    
@bp_dashboard.route('/dashboard/accept', methods=['POST'])
@login_required
def accept_request():
    userID = session.get('user_id')
    if request.method == 'POST':
        request_id = request.form.get('accept')
        print(request_id)
        if request.form.get('accept'):
            Services.accept_request(request_id, userID)
        return redirect(url_for('bp_dashboard.dashboard'))
    

@bp_dashboard.route('/dashboard/add-print', methods=['GET', 'POST'])
@login_required
def add_print_request():
    userID = session.get('user_id')
    if request.method == 'POST':
        form = PrintForm()
        if form.validate_on_submit():
            num_copies = form.num_copies.data
            description = form.description.data
            location = form.location.data
            mop = request.form.get('MOP')
            order_status = "Listing"
            print(num_copies, description, location,  mop)
            if form.printfile.data:
                printfile_result = allowed_file(form.printfile.data.filename)
                if printfile_result and printfile_result['code'] == 1:
                    print(get_flashed_messages())
                    filename = secure_filename(form.printfile.data.filename)
                    form.printfile.data.save(os.path.join(UPLOAD_FOLDER, filename))
                    filepath = os.path.join(UPLOAD_FOLDER, filename)

                    if filepath:
                        upload_FileS3(filepath)
                        fileURL = os.path.basename(filepath)
                        os.remove(filepath)
                    Services.add_service("PR")
                    Services.get_payment(mop)
                    result = Services.add_printing(fileURL,num_copies,description)
                    Services.add_request(userID, order_status, location)
                    if result is not None and result['code'] == -1:
                        flash(result['message'])
                    else:
                        redirect('bp_dashboard.dashboard')

                elif printfile_result:
                    flash(printfile_result['message'])
            return redirect(url_for('bp_dashboard.dashboard'))
        else:
            flash("You are trying to access a forbidden URL.", "error")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field {field}: {error}")
        return redirect(url_for('bp_dashboard.dashboard'))
    
@bp_dashboard.route('/food-services', methods=['GET', 'POST'])
@login_required
def add_food_request():
    title = 'Food Services'
    userID = session.get('user_id')
    
    return render_template("dashboard/S_food.html", title=title)

    
@bp_dashboard.route('/dashboard/add-gcash', methods=['GET', 'POST'])
@login_required
def add_gcash_request():
    userID = session.get('user_id')
    if request.method == 'POST':
        form = GcashForm()
        gcash_type = request.form['selectedValue']
        if form.validate_on_submit():
            amount = int(form.amount.data)
            phone_number = form.phone_number.data
            location = form.location.data
            mop = "COD"
            order_status = "Listing"
            Services.add_service("GC")
            result = Services.add_gcash(gcash_type, amount, phone_number)
            Services.add_request(userID, order_status, location)
            Services.get_payment(mop)
            if result is not None and result['code'] == -1:
                flash(result['message'])
            else:
                return redirect(url_for('bp_dashboard.dashboard'))
        else:
            flash("You are trying to access a forbidden URL.", "error")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Error in field {field}: {error}")
        return redirect(url_for('bp_dashboard.dashboard'))
    
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'pptx'}
def allowed_file(filename):
    try:
        if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            return {
                'code': 1,
                'message': 'File Accepted'
            }
        else:
            return {
                'code': 0,
                'message': 'File not allowed! Only .docx, .pptx, .pdf files are allowed.'
            }
    except Exception as e:
        print(e)
        return {
            'code': -1,
            'message': f'{e}'
        }

# def uploadFile(file): #cloudinary uploader
#     uploadResult = cloudinary.uploader.upload(file, folder="StudenDiri/Print_files", resource_type = "raw")
#     return uploadResult['secure_url']


def upload_FileS3(S3file):
    upload_success = upload_file(S3file, S3_BUCKET)
    if upload_success:
        url = create_presigned_url(S3_BUCKET, S3file)
        print(f'URL: {url}')
        return url
    else:
        print("Failed to upload file to S3.")

#Boto S3 Upload File Function
def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
    
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False, print("S3 Not Uploaded")
    return True, print("S3 Uploaded")
    

#Boto S3 Create URL File Function
def create_presigned_url(bucket_name, object_name, expiration=3600):
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response