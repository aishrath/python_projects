import requests
import argparse

if __name__ == "__main__":
    print(requests.get("http://httpbin.org/get"))

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", default='GET')
    parser.add_argument("-u", "--url", default="http://httpbin.org/get")
    parser.add_argument("-d", "--data")
    parser.add_argument("-x", "--chatty", default=False)

    args = parser.parse_args()

    METHOD = args.method.upper()
    URL = args.url
    DATA = args.data

    if METHOD in 'GET':
        print(requests.get(URL))
    elif METHOD in 'POST':
        print(requests.post(url=URL, data=DATA))
    elif METHOD in 'DELETE':
        print(requests.delete(URL))
    elif METHOD in 'PUT':
        print(requests.put(URL))

    print(args.method)
