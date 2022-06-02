from django.contrib import admin

from .models import Movie, MovieTheater, CinematicUniverse, UsersFavourites, Comment, UsersNotifications, Notification


class MovieAdmin(admin.ModelAdmin):
    readonly_fields=('visits_count', 'comments')


class MovieTheaterAdmin(admin.ModelAdmin):
    readonly_fields=('visits_count', )


class UserFavouritesAdmin(admin.ModelAdmin):
    readonly_fields=('user', 'favourites')


class UserNotificationsAdmin(admin.ModelAdmin):
    readonly_fields=('user', 'notifications')


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieTheater, MovieTheaterAdmin)
admin.site.register(CinematicUniverse)
admin.site.register(UsersFavourites, UserFavouritesAdmin)
admin.site.register(Comment)
admin.site.register(UsersNotifications, UserNotificationsAdmin)
admin.site.register(Notification)
