import asyncio
from asgiref.sync import sync_to_async
from .models import Notification, UsersNotifications
import threading


def send_notification_to_user(user_to_notify, text: str) -> None:
    #print('SENDING')
    if len(UsersNotifications.objects.filter(user=user_to_notify)) == 0:
        UsersNotifications.objects.create(user=user_to_notify)

    new_notification = Notification.objects.create(message=text)

    UsersNotifications.objects.filter(user=user_to_notify)[0].notifications.add(new_notification)


def send_notifications_to_users_inner(users_list, message: str):
    for user in users_list:
        send_notification_to_user(user, message)


def send_notifications_to_users(users, message: str) -> None:
    #print('sending notifications to other users')
    threading.Thread(target=send_notifications_to_users_inner, args=(users, message)).start()
