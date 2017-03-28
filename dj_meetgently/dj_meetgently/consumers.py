import re
import json
import logging
from channels import Group
from channels.sessions import channel_session
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
    # Extract the room from the message. This expects message.path to be of the
    # form /chat/{label}/, and finds a Room if the message path is applicable,
    # and if the Room exists. Otherwise, bails (meaning this is a some othersort
    # of websocket). So, this is effectively a version of _get_object_or_404.
    print message.reply_channel


@channel_session
def ws_receive(message):
    # Look up the room from the channel session, bailing if it doesn't exist
    print "==socket=="
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
    except KeyError:
        log.debug('no room in channel_session')
        return
    except Room.DoesNotExist:
        log.debug('recieved message, buy room does not exist label=%s', label)
        return

    # Parse out a chat message from the content text, bailing if it doesn't
    # conform to the expected message format.
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return

    if set(data.keys()) != set(('handle', 'message')):
        log.debug("ws message unexpected format data=%s", data)
        return

    if data:
        log.debug('chat message room=%s handle=%s message=%s',
                  room.label, data['handle'], data['message'])
        m = room.messages.create(**data)

        # See above for the note about Group
        Group('chat-' + label, channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})


@channel_session
def ws_disconnect(message):
    print "==socket=="
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group('chat-' + label, channel_layer=message.channel_layer).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass