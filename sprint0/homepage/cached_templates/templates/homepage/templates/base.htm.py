# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427918367.589848
_enable_loop = True
_template_filename = '/Users/brock/sprint0/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'left', 'footer', 'header']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def left():
            return render_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n<meta charset="UTF-8">\n<head>\n\n    <title>homepage</title>\n\n')
        __M_writer('\n\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <link rel="icon" type="image/x-icon"\n          href="http://fc07.deviantart.net/fs70/f/2012/185/5/f/triforce_icon_free_to_use_by_kittyzelda64-d560tnh.png"/>\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context) ))
        __M_writer('\n\n</head>\n\n\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n</div>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left'):
            context['self'].left(**pageargs)
        

        __M_writer('\n<div class="container-fluid">\n    <div id="center" class="col-md-8">\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n<div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\n  <div class="modal-dialog">\n    <div class="modal-content">\n      <div class="modal-header">\n        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\n        <h4 class="modal-title" id="myModalLabel">Modal title</h4>\n      </div>\n      <div class="modal-body">\n        ...\n      </div>\n      <div class="modal-footer">\n\n      </div>\n    </div>\n  </div>\n</div>\n</div>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n')
        __M_writer(str( static_renderer.get_template_js(request, context) ))
        __M_writer('\n\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left():
            return render_left(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n    <div id="left side" class="col-md-2">\n        <nav>\n            <ul class="nav nav-pills nav-stacked">\n                <li><a href="/homepage/Events/">Events</a></li>\n                <li><a href="/Store/Store/">Store</a></li>\n            </ul>\n        </nav>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="jimbob">\n    <p><a href="http://localhost:8000/homepage/terms/">terms and conditions</a></p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="page-header">\n    <h1>The Colonial Heritage Foundation\n        <small>preserving history</small>\n    </h1>\n    <button id="show_modal">Log in</button>\n    <a href="/Account/logout/">Logout</a>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brock/sprint0/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "line_map": {"68": 83, "69": 85, "70": 85, "82": 58, "76": 58, "16": 4, "18": 0, "88": 44, "100": 79, "94": 44, "112": 32, "34": 2, "35": 4, "36": 5, "40": 5, "41": 15, "42": 19, "43": 19, "44": 21, "45": 21, "46": 26, "47": 26, "48": 26, "53": 40, "118": 32, "58": 54, "124": 118, "106": 79, "63": 60}, "source_encoding": "ascii"}
__M_END_METADATA
"""
