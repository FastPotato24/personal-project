import json
import os

from rich import print
from rich.console import Console

console = Console()

id_cache = {
  "entities": {},
  "items": {},
}

class Item:
  def __init__(self, id=None, data=None):
    if data is not None:
      self.data = data
    if id is not None:
      self.id = id
      self.load(id)
    self.name = self.data["info"]["name"]

  def load(self, id):
    if ":" not in id:
      self.id = "main:" + id
    if self.id in id_cache["items"]:
      self.data = id_cache["items"][self.id]
      return
    datapack, id = self.id.split(":")
    with open(f"datapacks/{datapack}/items/{id}.json") as file: # Change file to something more readable
      self.data = json.load(file)