# -*- coding: utf-8 -*-
from channels.staticfiles import StaticFilesConsumer
from . import consumers
from channels import route

# channel_routing = {
#     'http.request': StaticFilesConsumer(),
#     'websocket.connect': consumers.ws_connect,
#     'websocket.receive': consumers.ws_receive,
#     'websocket.disconnect': consumers.ws_disconnect,
# }

channel_routing = [
    # route(u"websocket.connect", consumers.ws_connect),
    # route(u"websocket.receive", consumers.ws_receive),
    # route(u"websocket.disconnect", consumers.ws_disconnect),
]