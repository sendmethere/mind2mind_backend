from django.contrib import admin
from .models import Quiz, SuccessRecord, Player

admin.site.register(Quiz)
admin.site.register(Player)

@admin.register(SuccessRecord)
class SuccessRecordAdmin(admin.ModelAdmin):
    list_display = ['quiz', 'player', 'timestamp']
    search_fields = ['quiz__title', 'player__nickname'] 
    list_filter = ['timestamp'] 