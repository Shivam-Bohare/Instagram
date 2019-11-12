from django.contrib import admin
from social.models import UserInfo , Comment , CommentReply , PictureLike , Block , Follow , FollowRequest , Picture

class UserInfoInline(admin.TabularInline):
    model = UserInfo
    extra = 0

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_filter = ('time' , 'picture_user_id')

@admin.register(PictureLike)
class PictureLikeAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentReply)
class CommentReplyAdmin(admin.ModelAdmin):
    pass

@admin.register(FollowRequest)
class FollowRequestAdmin(admin.ModelAdmin):
    list_display = ('user_id' , 'request_user_id')

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user_id' , 'follow_user_id')

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('user_id' , 'block_user_id')
    
