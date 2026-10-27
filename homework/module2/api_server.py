"""Мінімальне тестове REST API для завдання 2.

Запуск:  python3 api_server.py  (слухає http://127.0.0.1:8000)

GET  /posts       -> 200, список усіх постів
GET  /posts/<id>  -> 200 або 404
POST /posts       -> 201 Created, тіло: form-urlencoded або JSON
"""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qsl

posts = [{"id": 1, "title": "hello", "body": "first post", "userId": 1}]


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, payload, extra_headers=None):
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        for name, value in (extra_headers or {}).items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        # GET лише читає дані, тому відповідь можна кешувати
        cache = {"Cache-Control": "public, max-age=60"}
        if self.path == "/posts":
            return self._send(200, posts, cache)
        if self.path.startswith("/posts/"):
            post_id = self.path.removeprefix("/posts/")
            for post in posts:
                if str(post["id"]) == post_id:
                    return self._send(200, post, cache)
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/posts":
            return self._send(404, {"error": "not found"})
        raw = self.rfile.read(int(self.headers.get("Content-Length", 0))).decode()
        if self.headers.get("Content-Type", "").startswith("application/json"):
            data = json.loads(raw or "{}")
        else:
            data = dict(parse_qsl(raw))
        post = {"id": max(p["id"] for p in posts) + 1, **data}
        posts.append(post)
        # POST змінює стан сервера: відповідь не кешуємо, у Location — адреса нового ресурсу
        self._send(201, post, {"Location": f"/posts/{post['id']}", "Cache-Control": "no-store"})


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
