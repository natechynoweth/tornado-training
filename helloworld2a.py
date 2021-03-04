import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class RedHandler(tornado.web.RequestHandler):
    def get(self):
        token=self.get_argument("token", 0, True)
        output=self.get_argument("output", "txt", True)
        if output.lower() != "json":
            self.write("Hello, red_fish. Your token is {0}".format(str(token)))
        else:
            json_txt = {"hello": "red_fish", "token": token}
            self.write(json_txt)


class BlueHandler(tornado.web.RequestHandler):
    def get(self):
        token=self.get_argument("token", 0, True)
        output=self.get_argument("output", "txt", True)
        if output.lower() != "json":
            self.write("Howdy, blue_fish. Your token is {0}, dupicated its {1}".format(str(token), int(token)*2))
        else:
            json_txt = {"hello": "red_fish", "token": token, "duplicatedToken": int(token)*2}
            self.write(json_txt)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/red_fish/", RedHandler),
        (r"/blue_fish/", BlueHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()