import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-5s - %(name)s\t%(message)s")

ROUTES = {
  "/goog": "https://google.co.uk"
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
