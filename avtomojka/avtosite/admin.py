from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .forms import *


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_a', 'get_p')
    save_on_top = True

    def get_a(self, object):
        a = object.date_update.strftime('%d')
        b = object.date_update.strftime('%m.%Y')
        t = object.Time.time
        if object.Time.day:
            return mark_safe(f"<p>{int(a)+1}.{b} {t}:00</p>")
        else:
            return mark_safe(f"<p>{a}.{b} {t}:00</p>")

    def get_p(self, object):
        w = object.Wash.price
        s = object.Salon.price
        h = object.HydroShine
        a = object.Avto.kooficent
        sum = (w+s)*a
        sum2 = sum+1000*a
        if h:
            if object.Wash.pk == 1 and object.Salon.pk == 3:
                return mark_safe(f"<p>{sum2*0.85}</p>")
            elif object.Wash.pk == 2 and object.Salon.pk == 2:
                return mark_safe(f"<p>{sum2*0.75}</p>")
            elif object.Wash.pk == 2 and object.Salon.pk == 3:
                return mark_safe(f"<p>{sum2*0.80}</p>")
            else:
                return mark_safe(f"<p>{sum2}</p>")
        else:
            return mark_safe(f"<p>{sum}</p>")


class WashAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    save_on_top = True


class SalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    save_on_top = True


class AvtoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'kooficent')
    save_on_top = True


class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    save_on_top = True


admin.site.register(Wash, WashAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Avto, AvtoAdmin, verbose_name="Автомобиль")
admin.site.register(Applications, ApplicationsAdmin)



