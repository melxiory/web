def application(environ, start_response):
        start_response("200 OK", [
            ("Content-Type", "text/plain")
        ])
        return iter(["\n".join(environ.get('QUERY_STRING').split("&")).encode('utf-8')])
