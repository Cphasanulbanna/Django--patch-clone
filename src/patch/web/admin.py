import email
from pyexpat import model
from django.contrib import admin

from web.models import Testimonial, Promoter, Faq, Subscribe


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id","name","designation","image","description"]


admin.site.register(Testimonial,TestimonialAdmin)


class PromoterAdmin(admin.ModelAdmin):
    list_display = ["id","name","image"]


admin.site.register(Promoter,PromoterAdmin)


class FaqrAdmin(admin.ModelAdmin):
    list_display = ["id","title","faq_type","description"]


admin.site.register(Faq,FaqrAdmin)


admin.site.register(Subscribe)