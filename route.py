#!/bin/usr/env python3
"""
This module is routing for app
"""
import handler
route_handler = [
    (r"/", handler.IndexHandler),
    (r"/index", handler.IndexHandler),
    (r"/login", handler.LoginHandler),
]

# class Route(tornado.routing.Router):
#     def __init__(self):
#         pass
