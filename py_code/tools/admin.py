from django.contrib import admin

# Register your models here.
from tools import models
from tools.models import product
from tools import views
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
#Regist in
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','no','name','comment','code','updateTime')
    list_per_page = 20
    list_editable = ['name']
    list_display_links = ('id', 'no')
    ordering = ('-id',)
    search_fields =('name','id')

    #Set User Pro
    def get_readonly_fields(self, request, obj=None):
        """  READ ONLY """
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('id', 'no', 'code', 'updateTime', 'creatTime','highlighted')

    #when inner new product
    def save_model(self, request, obj, form, change):
        if change:
            pass
        else:
            nos  = views.GET_GOOD_NO()
            codes = views.GET_MD5_CODE(nos)
            obj.no = nos
            obj.code = codes
            obj.highlighted = nos + "-" +codes + ":{"+ obj.name+"}"
        super(ProductAdmin, self).save_model(request, obj, form, change)
# Register Model into admin
admin.site.site_header = 'Product Manger'
admin.site.site_title = 'Product Manger Systems'

#Regist Wechat Info :
