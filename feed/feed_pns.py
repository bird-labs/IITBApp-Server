__author__ = 'dheerendra'

from serializers import FeedEntrySerializer
from models import FeedEntry
from django.db.models import signals
from django.contrib.auth.models import User
import logging
import json
from core.globals import send_android_push_notification
from pns.models import Device
from signals import feed_entry_registered
from pns import pns

logger = logging.getLogger(__name__)


def create_message(instance, created):
    instance.refresh_from_db()
    action = 'new' if created else 'update'
    feed_entry_data = FeedEntrySerializer(instance).data
    message_dict = {
        'action': action,
        'type': 'feed',
        'item': feed_entry_data,
    }
    return json.dumps(message_dict)


def send_feed_push_notification(sender, instance, created, **kwargs):
    message = create_message(instance, created)
    send_android_push_notification(message)
    logger.info("Android push sent for feed with id %d with title %s", instance.id, instance.title)


def send_feed_to_pns(sender, instance, created, **kwargs):
    message = create_message(instance, created)
    user_queryset = User.objects.all().filter(feed_subscriptions__in=instance.categories.all())
    pns.send_pns(message, user_queryset)
    logger.info("Android push sent to feed with id %d with title %s to new devices", instance.id, instance.title)

signals.post_save.connect(send_feed_push_notification, FeedEntry)
feed_entry_registered.connect(send_feed_to_pns, FeedEntry)