import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    pict_filename = random_hex + f_ext
    pict_path = os.path.join(current_app.root_path, "static/profile_pics", pict_filename)

    image = Image.open(form_picture)
    if (
        image.height < image.width
    ):  # if height make it 125 and rescale width to correct aspect ratio
        ratio = 125 / image.height
        output_size = (ratio * image.width // 1, 125)  # (width, height)
    else:  # else resize so that the width = 125 and height is correct aspect ratio
        ratio = 125 / image.width
        output_size = (125, ratio * image.height // 1)

    image.thumbnail(output_size)
    image.save(pict_path)

    return pict_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                sender='noreply@demo.com',
                recipients=[user.email])
    msg.body = f'''To reset your password, visty the following link:
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request simply ignore this email and no changes will be made
    unless your email has been hacked
    '''
    mail.send(msg)