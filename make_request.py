import requests
import hashlib
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import sys

def make_request(url: str) -> str:
    s = requests.Session()

    retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])

    s.mount('http://', HTTPAdapter(max_retries=retries))

    response = s.get(f'http://{url}')
    return response


def write_content_to_file(filename: str, content) -> None:

    with open(filename, "w+") as f:
        f.write(content)


if __name__=="__main__":
    url = sys.argv[1]
    r = make_request(url)
    write_content_to_file("sum", hashlib.md5(r.content).hexdigest())
