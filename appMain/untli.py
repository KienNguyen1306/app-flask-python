from appMain import *
from appMain.model import *

from flask_login import current_user

# ==================================== read category =======================================

def read_category1():
    return Category.query.all()


# ================================== read product ================================
def read_product(page = 1 ,kw=None,caterogy_id = None):
    product  = Product.query.all()
    
    if kw:
        product = Product.query.filter(Product.name.contains(kw)).all()
    if caterogy_id:
        product = Product.query.filter(Product.category_id == caterogy_id).all()
    
    size = app.config['SIZE_PRODUCT']
    start = (page -1) * size
    end = start + size
    # return comment[start:end]
    return product[start:end]

# ================================== read  count product ================================
def read_count_product():
    product  =Product.query.count()
    return product



# ============================ read_product by id ===================================
def read_product_by_id(product_id):
    return Product.query.filter(Product.id == product_id).first()


# =============================== đăng nhập ==========================================
def check_login(name,password):
    return User.query.filter(User.username == name ,User.password == password).first()

# ================================== read User by id ==============================
def read_user_by_id(user_id):
    return User.query.filter(User.id == user_id).first()

# =================================== read user by name ============================
def read_user_by_name(name):
    return User.query.filter(User.username == name).first()
# ====================================== đăng kí ===================================

def add_user(name,password,email):
    user = User(username = name,password = password,email = email)
    db.session.add(user)
    db.session.commit()
    return user
# ================================ đếm số luông tiền in cart ====================
def total_cart(carts):
    sum_count=0
    sum_price = 0
    if carts:
        for cart in carts.values():
            sum_count+=int(cart['count'])
            sum_price+=int(cart['count']) * int(cart['price'])
    return {
        'sum_count':sum_count,
        'sum_price':sum_price
    }
# ========================================= add thanh toán ===========================

def add_recetail(cart):
    if cart:
        receipt = Receipt(user = current_user)
        db.session.add(receipt)
        for c in cart.values():
            d =ReceiptDetail(receipt = receipt,
                             product_id = c['id'],
                             sum_count = c['count'],
                             sum_price = c['price'])

            db.session.add(d)
        db.session.commit()





# ========================================= add comment ==================================

def add_comment(product_id,content):
    comment = Comment(user = current_user,product_id = product_id,content = content)
    db.session.add(comment)
    db.session.commit()
    return comment


# ============================================ đọc commetn theo product id ====================

def read_comment_by_product_id(product_id):
    comment = Comment.query.filter(Comment.product_id == product_id).order_by(-Comment.id).all()
    return comment

def read_comment_by_product_id_user(product_id,page = 1):
    comment = db.session.query(Comment,User).filter(Comment.user_id == User.id,Comment.product_id== str(product_id)).order_by(-Comment.id).all()
    
    # size = app.config['SIZE_COMMENT']
    # start = (page -1) * size
    # end = start + size
    # return comment[start:end]
    return comment



   