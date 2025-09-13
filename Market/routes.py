from Market import app,db
from flask import render_template, redirect
from Market.models import Item, User
from Market.form import register, Login_form, purchaseitemform,sellitemform
from flask import  redirect ,url_for,flash,request
from flask_login import login_user, logout_user,login_required,current_user
# when there is no username it doesnot show that informing message
@app.route("/")
@app.route("/home") 
def home_page():
    items=Item.query.all()
    return render_template("home.htm",items=items)
@app.route("/market",methods=["post","get"])
@login_required
def market_page():
    purchase_item=purchaseitemform()
    sell_item=sellitemform()
    if request.method=="POST":
        purchased_item=request.form.get("purchased_item")
        p_item_object=Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            p_item_object.owner=current_user.id
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"congratulations, You bought {current_user.budget} for {p_item_object.price}",category="success")
            else:
                flash(f"Sorry, Your budget is {current_user.budget} and the price is {p_item_object.price}",category="danger")
        sold_item=request.form.get("sold_item")
        s_item_object=Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"congratulations, You sold {current_user.budget} for {s_item_object.price}",category="success")
            else:
                flash(f"Sorry, try another time. You can't sell {current_user.budget} right now",category="danger")

        return redirect(url_for('market_page'))
    elif request.method=="GET":
        items=Item.query.filter_by(owner=None)
        owned_items=Item.query.filter_by(owner=current_user.id)
        return render_template("market.html",items=items,purchase_item=purchase_item,owned_items=owned_items,sell_item=sell_item)
def count(entities):
    count=0
    for _ in entities:
        count+=1
    return count
@app.route("/dashboard")
@login_required
def dashboard():
    items=Item.query.filter_by(owner=None)
    item_count=count(items)
    users=count(User.query.all())
    user_count=users
    total_balance=0
    for item in items:
        total_balance+=item.price
    return render_template("dashboard.html",items=items,count=item_count,users=user_count,total_balance=total_balance)
@app.route("/dashboard/products")
def dashboard_products():
    items=Item.query.filter_by(owner=None)
    return render_template("products.html",items=items)
@app.route("/dashboard/users")
def dashboard_users():
    users=User.query.all()
    return render_template("users.html",users=users)

@app.route("/contact_us")
def contact_us():
    return render_template("contactus.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/reigster",methods=["get",'post'])
def register_page():
    form=register()
    if form.validate_on_submit():
        user_account = User(username=form.username.data,
                    email=form.email.data,
                    )
        user_account.password = form.password1.data
        db.session.add(user_account)
        db.session.commit()
        login_user(user_account)
        flash(f"You're welcom {user_account.username}",category="success")
        return redirect(url_for("market_page"))
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f"{"".join(err_msg)}", category = 'danger')
    return render_template("register.html",form=form)
@app.route('/login', methods=["get","post"])
def login():
    form=Login_form()
    # when there is no username it doesnot show that informing message

    if form.validate_on_submit():
        attempted_user= User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            if form.username.data=="Basem Mohammed Al-Hersh":
                login_user(attempted_user)
                return redirect(url_for("dashboard"))
            else:
                login_user(attempted_user)
                flash("Welcome! You're logged in!",category="success")
                return redirect(url_for("market_page"))
        else:
            flash("Sorry, there is no username found. Try again",category="danger")
    return render_template('login.html',form=form)
@app.route('/logout')
def Logout_page():
    logout_user()
    flash("You got logged out",category="info")
    return redirect(url_for("home_page"))
@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy_policy.html")
@app.route("/terms-of-service")
def terms_of_service():
    return render_template("terms_of_service.html")