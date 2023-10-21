import logging
import json

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)-5s - %(name)s\t%(message)s")

with open("routes.json") as f:
    routes = json.load(f)["routes"]

def main(args):
  name = args["http"]["path"]

  logging.info(f"Received request for '{name}'")
  redirect_url = routes.get(name, "https://jread.dev")

  return {
    "statusCode": 302,
    "headers": {
      "Location": redirect_url
    }
  }
