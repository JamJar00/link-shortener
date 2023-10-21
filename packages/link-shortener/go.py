import logging

logging.basicConfig(format="%(asctime)s %(levelname)-5s - %(name)s\t%(message)s")

ROUTES = {
  "goog": "httpsm://google.co.uk"
}

def main(args):
  name = args["http"]["path"]

  logging.info(f"Received request for '{name}'")
  redirect_url = ROUTES.get(name, "https://jread.dev")

  return {
    "statusCode": 302,
    "headers": {
      "Location": redirect_url
    }
  }
