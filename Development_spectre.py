import requests
import json

def Requesting_a_token():

    url = 'https://wss.hyper-api.com/token.php'

    payload = {
        "code":"86ab8c3de2a08a96f99826f8102df6ae4a0f8a46",
        "grant_type":"authorization_code"
    }
    headers = {
          "Accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
          'Authorization': 'Basic YmM3OTVjNWQ1YTc2MzFlMGM1ZWI5YjdkZDU0NjJkZDE6NjgxMDE1NzE5ZDAyYmM0NDE2ZjE0YTg3ZjY2N2E1'
        }

    print(type(headers))
    print(type(payload))

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response)

    print(response.text.encode('utf8'))
    #print(type(response))
    
    #result = json.dumps(response)

    #print(type(result))

    #result = response.json()
    

#Requesting_a_token()

# Import WebSocket client library
# from websocket import create_connection

# # Connect to WebSocket API and subscribe to trade feed for XBT/USD and XRP/USD
# ws = create_connection("wss://wss.hyper-api.com:4443/spectreai/")
# ws.send('{"action":"userhistory","data":{"account_type":1,"start_position":0,"end_position":4},"token":"USER_TOKEN"}')

# # Infinite loop waiting for WebSocket data
# #while True:
# print(ws.recv())

#from openvpn_api import VPN
from openvpn_status import parse_status
v = VPN('wss://wss.hyper-api.com:4443/spectreai/', 7505)
v.connect()
# Do some stuff, e.g.
print(v.release)
v.disconnect()

# from websocket import create_connection
# print("before ws")
# ws = create_connection("ws://wss.hyper-api.com:4443/spectreai/")
# print("Sending 'Hello, World'...")
# jsonData = {"action":"userhistory",
#            "data":{
#                "account_type":1,
#                 "start_position":0,
#                 "end_position":4},
#             "token":"6c50fcf0e3430c04613cba7f0781c7897f9137da"}
# ws.send(json.dumps(jsonData))
# print("Sent")
# print("Receiving...")
# result =  ws.recv()
# print("Received '%s'" % result)
# ws.close()

# import websocket
# try:
#     import thread
# except ImportError:
#     import _thread as thread    
# import time

# def on_message(ws, message):
#     print(message)

# def on_error(ws, error):
#     print(error)

# def on_close(ws):
#     print("### closed ###")

# def on_open(ws):
#     def run(*args):
#         for i in range(3):
#             time.sleep(1)
#             ws.send("Hello %d" % i)
#         time.sleep(1)
#         ws.close()
#         print("thread terminating...")
#     thread.start_new_thread(run, ())


# if __name__ == "__main__":
#     websocket.enableTrace(True)
#     ws = websocket.WebSocketApp("wss://wss.hyper-api.com:4443/spectreai/",
#                               on_message = on_message,
#                               on_error = on_error,
#                               on_close = on_close)
#     ws.send('{"action":"userhistory","data":{"account_type":1,"start_position":0,"end_position":4},"token":"USER_TOKEN"}')
#     ws.on_open = on_open
#     ws.run_forever()