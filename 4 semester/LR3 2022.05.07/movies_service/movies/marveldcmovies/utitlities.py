import asyncio
from asgiref.sync import sync_to_async
from .models import Notification, UsersNotifications


@sync_to_async
def send_notification_to_user(user_to_notify, text: str) -> None:
    if len(UsersNotifications.objects.filter(user=user_to_notify)) == 0:
        UsersNotifications.objects.create(user=user_to_notify)

    new_notification = Notification.objects.create(message=text)

    UsersNotifications.objects.filter(user=user_to_notify)[0].notifications.add(new_notification)


async def send_notifications_to_users_inner(users_list, message: str):
    for user in users_list:
        await asyncio.gather(send_notification_to_user(user, message))


def send_notifications_to_users(users, message: str) -> None:
    asyncio.run(send_notifications_to_users_inner(users, message))
