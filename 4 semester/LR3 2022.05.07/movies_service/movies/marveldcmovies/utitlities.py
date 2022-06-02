from .models import Notification, UsersNotifications


def send_notification_to_user(user_to_notify, text: str) -> None:
    if len(UsersNotifications.objects.filter(user=user_to_notify)) == 0:
        UsersNotifications.objects.create(user=user_to_notify)

    new_notification = Notification.objects.create(message=text)

    UsersNotifications.objects.filter(user=user_to_notify)[0].notifications.add(new_notification)
