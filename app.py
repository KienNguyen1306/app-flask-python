from appMain import *
# from __init__ import *
import appMain.untli as untli
from flask import render_template, request, url_for,redirect,jsonify,session
from flask_login import login_user,logout_user,login_required,current_user
# ==================== home =========================
import math
@app.route('/')
def home():
    return render_template('index.html')

# ====================== login =========================

@app.route('/login',methods =['GET','POST'])
def user_login():
    error=''
    if request.method == 'POST':
        name =request.form.get('name')
        password =request.form.get('password')
        user = untli.check_login(name=name,password=password)
        if user:
            login_user(user=user)
            if 'cart' == request.args.get('next'):
                return redirect(url_for('cart'))
            elif 'product' == request.args.get('next'):
                return redirect(url_for('product_detail',product_id = request.args.get('product_id')))
            else:
                return redirect(url_for('home'))
        else:
            error ='Tên đăng nhập hoặc mật khẩu không chính xác'
    
    return render_template('login.html',error = error)


# ================================================== product detail ==================================
@app.route('/product-detail/<int:product_id>',methods =['GET'])
def product_detail(product_id):
    product = untli.read_product_by_id(product_id)
    comment =untli.read_comment_by_product_id_user(product_id)
    return render_template('Product_detail.html',product = product,comment = comment)


# ======================================================= product all ==================================
@app.route('/product',methods =['GET'])
def product_all():
    page = request.args.get('page',1)
    kw =request.args.get('kw')
    caterogy_id = request.args.get('caterogy_id')
    product = untli.read_product(page=int(page),kw = kw,caterogy_id=caterogy_id)
    count = untli.read_count_product()
    return render_template('product.html',product = product,
                           start = math.ceil(count / app.config['SIZE_PRODUCT'])
                           )


# =========================== logout ========================
@app.route('/logout',methods =['GET','POST'])
def user_logout():
    logout_user()
    return redirect(url_for('home'))

@login.user_loader
def loading(user_id):
    return untli.read_user_by_id(user_id)

# ============================== register ====================

@app.route('/register',methods =['GET','POST'])
def register():
    error =''
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        email =request.form.get('email')
        repeatpass = request.form.get('repeatpass')
        user = untli.read_user_by_name(name=name)
        if user:
            error ='Tên Đăng nhập đã có người sữ dụng'
        elif not password == repeatpass:
            error ='Password không trùng khớp vui lòng kiểm tra lại'
        else:
            user_regis = untli.add_user(name=name,password=password,email=email)
            login_user(user_regis)
            return redirect(url_for('home'))
    return render_template('register.html',error = error)


# ================================== in cart ================================

@app.route('/cart',methods =['GET','POST'])
def cart():
    return render_template('cart.html')

# ================================ add to cart ===============================
@app.route('/api/in-cart',methods =['GET','POST'])
def add_cart():
    data = request.json
    id =str(data.get('id'))
    name = data.get('name')
    des = data.get('des')
    price = data.get('price')
    image = data.get('image')
    cart = session.get('cart')
    if not cart:
        cart ={}
    if id in cart:
        cart[id]['count']+=1
    else:
        cart[id] = {
            'id':id,
            'name':name,
            'des':des,
            'price':price,
            'image':image,
            'count':1
        }
        
    session['cart'] = cart
    return jsonify(untli.total_cart(cart))

# ============================================== update cart ==============================

@app.route('/api/update-cart',methods =['GET','PUT'])
def update_cart():
    data = request.json
    id =str(data.get('id'))
    count = data.get('count')
    cart = session.get('cart')
    if count and id in cart:
        cart[id]['count'] = count
        session['cart'] = cart
    return jsonify(untli.total_cart(cart))


# ============================================== delete cart ==============================
@app.route('/api/delete/<product_id>',methods =['GET','DELETE'])
def delete_cart(product_id):
    cart = session.get('cart')
    if product_id in cart:
        del cart[product_id]
        session['cart'] = cart
    return jsonify(untli.total_cart(cart))


# ==================================== thanh toán ===============================
@app.route('/api/pay',methods = ['POST'])
@login_required
def pay_cart():
    try:
        untli.add_recetail(session.get('cart'))
        del session['cart']
    except:
        return jsonify({'code':400})
    return jsonify({'code':200})


# ============================== api comment ================================

@app.route('/api/comment',methods = ['POST'])
@login_required
def add_comment():
    data = request.json
    product_id  = data.get('product_id')
    content = data.get('content')
    try:
        comment = untli.add_comment(product_id=product_id,content=content)
    except:
        return jsonify({'code':400})
    return jsonify({
        'code':200,
        'data':{
            'id':comment.id,
            'content':comment.content,
            'create_time':comment.create_time
        },
        'user':{
            'id':current_user.id,
            'name':current_user.username,
            'avatar':current_user.avatar
        }
        
    })





# ================================ dư liệu tất cả cát trang=================
@app.context_processor
def commom_responce():
    return {
        'categorys':untli.read_category1(),
        'products' :untli.read_product(),
        'products1' :untli.read_product(page=1),
        'count':untli.total_cart(session.get('cart'))
    }
    

if __name__ == '__main__':
    from appMain.admin import *
    app.run(debug=True)


