from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 5555


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    name_server = "site_page.html"

    def open_file(self):
        """
        Метод открывающий файл html содержащий страничку сайта
        :return info: возвращает прочитанный файл html
        """
        with open(self.name_server, "r", encoding="utf-8") as file:
            info = file.read()
        return info

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(self.open_file(), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
