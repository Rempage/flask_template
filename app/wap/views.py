from . import wap

@wap.route('/')
def index():
    return '1'