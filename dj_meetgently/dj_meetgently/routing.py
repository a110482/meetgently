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
    route(unicode("websocket.connect"), consumers.ws_connect),
    route("websocket.receive", consumers.ws_receive),
    route("websocket.disconnect", consumers.ws_disconnect),
]