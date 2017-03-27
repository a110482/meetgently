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
    route("websocket", consumers.ws_connect),
    route("websocket.connect", consumers.ws_connect),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", consumers.ws_receive),

    # Called when WebSockets disconnect
    route("websocket.disconnect", consumers.ws_disconnect),
    route()
]