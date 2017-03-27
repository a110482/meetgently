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
    route(u"http.request", consumers.ws_connect, path=r'^new_socket/chat/$'),
    route(u"websocket.connect", consumers.ws_connect),

    # Called when WebSockets get sent a data frame
    route(u"websocket.receive", consumers.ws_receive),

    # Called when WebSockets disconnect
    route(u"websocket.disconnect", consumers.ws_disconnect),

]