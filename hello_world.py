import requests
from bs4 import BeautifulSoup
import pyfiglet

IMPORTANT_URL="https://cintia.me/blog/post/hello-world/"


class Space:
  def __init__(self):
    print("\n")
class Exclamation:
  def __init__(self):
    print(pyfiglet.figlet_format("!"))
class d:
  def __init__(self):
    print(pyfiglet.figlet_format("d"))
class e:
  def __init__(self):
    print(pyfiglet.figlet_format("e"))
class H:
  def __init__(self):
    print(pyfiglet.figlet_format("H"))
class l:
  def __init__(self):
    print(pyfiglet.figlet_format("l"))
class o:
  def __init__(self):
    print(pyfiglet.figlet_format("o"))
class r:
  def __init__(self):
    print(pyfiglet.figlet_format("r"))
class w:
  def __init__(self):
    print(pyfiglet.figlet_format("w"))


def retrieve_chars():
    req = requests.get(IMPORTANT_URL)
    soup = BeautifulSoup(req.content, 'html.parser')

    return list(soup.find('h1', class_="title").get_text() + "!")


def printable_char(char):
    # special case
    if char == " ":
        Space()
    elif char == "!":
        Exclamation()
    else:
        eval(char)()


all_chars = [printable_char(c) for c in retrieve_chars()]
