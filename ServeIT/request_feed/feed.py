from . import bp_reqfeed
from flask import render_template, request, flash, redirect, session, url_for, get_flashed_messages
from ServeIT.auth.auth import login_required
from ServeIT.models.dbUtils.UserRepo import UserRepo
from ServeIT.models.dbUtils.ServicesRepo import Services


@bp_reqfeed.route('/request-feed', methods=['GET'])
@login_required
def requestfeed():
    title = 'Request Feed'
    userID = session.get('user_id')
    data = UserRepo.get_current_user(userID)
    rqdata = Services.display_request()
    requestcount = Services.count_requests()
    user_request = Services.get_user_requests(userID)
    print(user_request)
    created_request = Services.count_user_requests(userID)
    return render_template("request_feed/feed.html", title=title, rq=requestcount, cr=created_request, rqlist=rqdata,  uqlist=user_request, user=data)
