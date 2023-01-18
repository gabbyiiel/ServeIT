from . import bp_reqfeed
from flask import render_template, request, flash, redirect, session, url_for, get_flashed_messages
from ServeIT.auth.auth import login_required
from ServeIT.models.dbUtils.UserRepo import UserRepo

@bp_reqfeed.route('/request-feed', methods=['GET'])
@login_required
def requestfeed():
    title = 'Request Feed'
    userID = session.get('user_id')
    return render_template("request_feed/feed.html", title=title)
