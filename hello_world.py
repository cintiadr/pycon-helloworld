import requests
from bs4 import BeautifulSoup
import pyfiglet
from pyfiglet import FigletFont,Figlet
import random

IMPORTANT_URL="https://cintia.me/blog/post/hello-world/"
DECENT_FONTS = ["twin_cob","alligator2", "pebbles", "xsansbi", "npn_____", "eftitalic", "pawn_ins", "clr5x8", "type_set","1943____", "nancyj-underlined", "univers", "brite", "chunky", "clr8x8", "sbooki", "demo_1__", "epic"]

class Space:
  def __init__(self):
    print("\n")
class Exclamation:
  def __init__(self):
    print(get_good_rendered().renderText('!'))
class d:
  def __init__(self):
    print(get_good_rendered().renderText("d"))
class e:
  def __init__(self):
    print(get_good_rendered().renderText("e"))
class H:
  def __init__(self):
    print(get_good_rendered().renderText("H"))
class l:
  def __init__(self):
    print(get_good_rendered().renderText("l"))
class o:
  def __init__(self):
    print(get_good_rendered().renderText("o"))
class r:
  def __init__(self):
    print(get_good_rendered().renderText("r"))
class w:
  def __init__(self):
    print(get_good_rendered().renderText("w"))

def get_good_rendered():
    font = DECENT_FONTS[random.randint(0, len(DECENT_FONTS) - 1)]
    return Figlet(font=font)

def retrieve_string_to_print():
    req = requests.get(IMPORTANT_URL)
    soup = BeautifulSoup(req.content, 'html.parser')

    return list(soup.find('h1', class_="title").get_text() + "!")


def char_factory(char):
    # special cases first
    if char == " ":
        Space()
    elif char == "!":
        Exclamation()
    else:
        eval(char)()


[char_factory(c) for c in retrieve_string_to_print()]
