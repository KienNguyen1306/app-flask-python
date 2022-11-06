from appMain import *
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    products =db.relationship('Product', backref='Category', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    image = db.Column(db.String)
    active =db.Column(db.Boolean,default =True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    receiptDetails = db.relationship('ReceiptDetail', backref='product', lazy=True)
    products = db.relationship('Comment', backref='product', lazy=True)

class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

avata ='data:image/jpeg;base64,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'

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    avatar = db.Column(db.String,default = avata)
    active =db.Column(db.Boolean,default =True)
    user_role = db.Column(db.Enum(UserRole),default = UserRole.USER)
    receipts = db.relationship('Receipt', backref='user', lazy=True)
    comments =db.relationship('Comment', backref='user', lazy=True)

class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    details = db.relationship('ReceiptDetail', backref='receipt', lazy=True)
    
class ReceiptDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receipt_id =db.Column(db.Integer, db.ForeignKey('receipt.id'), nullable=False)
    product_id =db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    sum_count = db.Column(db.Integer)
    sum_price =db.Column(db.Float)
    creat_time = db.Column(db.DateTime,default = datetime.now())



class Comment(db.Model):
    id =db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String,nullable = False)
    create_time = db.Column(db.DateTime,default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id =db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)






with app.app_context():
    # c1 = Category(name = 'Điện thoại')
    # c2 = Category(name = 'Máy tính')
    # c3 = Category(name = 'Chuột')
    # c4 = Category(name = 'Tai nghe')

    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.add(c3)
    # db.session.add(c4)
    # db.session.commit()
    
    
    # p1 = Product(name = 'Chuột gaming Logitech G300S' ,description='OLED6.7"Super Retina XDR 3 camera 12 MP',price = '2000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/gearvn/dm8xxy_633efb36a8b44c89bdc6a1acd0e7efea-220x220.jpg',category_id = 3)
    # p3 = Product(name = 'Chuột gaming Logitech G300' ,description='OLED6.7"Super Retina XDR 3 camera 12 MP',price = '4000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/gearvn/dm8xxy_633efb36a8b44c89bdc6a1acd0e7efea-220x220.jpg',category_id = 3)
    # p4 = Product(name = 'Chuột gaming Logitech G3001' ,description='OLED6.7"Super Retina XDR 3 camera 12 MP',price = '5000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/vmart/san_pham/Logitech-M331-220x220.png',category_id = 3)
    
    # p5 = Product(name = 'Điện thoại OPPO Reno5' ,description='OLED6.7"Super Retina XDR 3 camera 12 MP',price = '8000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/vmart/san_pham/OPPO-Reno-5-220x220.png',category_id = 1)
    # p6 = Product(name = 'Điện thoại OPPO Reno6' ,description='OLED6.7"Super Retina XDR 3 camera 12 MP',price = '8000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/evo/637170935875912528-ss-s20-ultra-den-1-220x220.jpg',category_id = 1)
    
    # p7 = Product(name = 'Laptop Dell XPS 13 9310 i5' ,description='1135G7/8GB/256GB/13.4 inch',price = '12000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/evo/xps-13-9310-220x220.jpg',category_id = 2)
    # p8 = Product(name = 'Laptop Dell XPS 13 9310 i6' ,description='1135G7/8GB/256GB/13.4 inch',price = '12000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/evo/f0a3bf16c58311fe86ae3695df95ae4d-220x220.jpg',category_id = 2)
    
    # p9 = Product(name = 'Tai nghe không dây Huawei1' ,description='Freebuds Pro',price = '4000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/evo/gr-3-4-220x220.jpg',category_id = 3)
    # p10 = Product(name = 'Tai nghe không dây Huawei2' ,description='Freebuds Pro',price = '4000000',image = 'https://vmartplus.w2.exdomain.net/image/cache/catalog/vmart/san_pham/Wf-1000Mx3-220x220.png',category_id = 3)
    # db.session.add(p1)
    # db.session.add(p3)
    # db.session.add(p4)
    # db.session.add(p5)
    # db.session.add(p6)
    # db.session.add(p7)
    # db.session.add(p8)
    # db.session.add(p9)
    # db.session.add(p10)
    
    
    # db.session.commit()
    
    db.create_all()
    
    # pass