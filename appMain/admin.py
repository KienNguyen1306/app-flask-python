from appMain import *
from appMain.model import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='ADMIN', template_mode='bootstrap4')
# Add administrative views here


class ProductView(ModelView):
    # hiện khóa chính
    column_display_pk = True
    # hiện con mắt
    can_view_details=True
    # xuất file csv
    can_export = True
    # hiện tìm kiếm
    column_searchable_list = ['name','price','description']
    
    column_filters=['name','price']
    # bỏ hiện column image
    column_exclude_list=['image']
    # đổi tên sản phẩm
    column_labels = {
        'name':'Tên Sản phẩm'
    }








admin.add_view(ModelView(User, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Receipt, db.session))
admin.add_view(ModelView(ReceiptDetail, db.session))


