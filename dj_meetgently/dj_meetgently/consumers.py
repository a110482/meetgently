import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
from asgi_redis.local import RedisLocalChannelLayer

#from chat.models import Room

from channels.auth import channel_session_user_from_http, channel_session_user

log = logging.getLogger(__name__)


@channel_session_user_from_http
@channel_session
def ws_connect(message):
    print "==socket=="
    message.reply_channel.send({
        'accept': True
    })
    print message.reply_channel
    message.channel_session['rome'] = "001"
    Group('chat').add(message.reply_channel)
    Group('chat-001').send({"test": "tttt"})






@channel_session
def ws_receive(message):
    print "==socket_res=="


@channel_session
def ws_disconnect(message):
    print "==socket_dis=="
