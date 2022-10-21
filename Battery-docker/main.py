from http.server import BaseHTTPRequestHandler, HTTPServer
import psutil,json,socket


hostName = socket.gethostbyname(socket.gethostname())
serverPort = 80


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.battery = psutil.sensors_battery()
        self.plugged = self.battery.power_plugged
        self.percent = str(self.battery.percent)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps({"level":self.battery.percent},ensure_ascii=False),"utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    try:
        webServer.serve_forever()

    except KeyboardInterrupt:
        pass

    webServer.server_close()