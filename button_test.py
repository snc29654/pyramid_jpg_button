from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import signal

dbname = '../database.db'
    
def diary_world(request):
    in_data=request.params
    name=in_data["name"]
    weather=in_data["weather"]
    kind=in_data["kind"]

    f = open(r"C:\xampp\htdocs\xampp\shishu\color_code.txt", "r")

    getdata=""
    
    getdata=getdata+"<style>.example2{ border: none;}</style>"

    for i in range(8000):
        rgb=f.readline()
        print(rgb)
        getdata=getdata+"<input  type=\"button\" value=\" \" style=\"background-color:"+rgb+";\" class=\"example2\" ></input>"    
        if(i%80)==79:
            getdata=getdata+"<br>"    
                        
    return Response(str(getdata))

def from_rgb_to_colorcode(rgb):
    return "#%02x%02x%02x" % rgb

    #実行処理  python サーバーを立てています
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    with Configurator() as config:
        config.add_route('diary', '/')
        config.add_view(diary_world, route_name='diary',renderer="jsonp")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()