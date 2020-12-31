import eel
import desktop
import numpy as np
import pandas as pd
from controller import Controller
from searcher import Searcher
from exporter import Exporter
import sys
sys.dont_write_bytecode = True

# JavaScriptから呼びたいPython関数
@eel.expose
def search_kimetsu(target_word):
    return Searcher.search(controller.characters, target_word)

@eel.expose
def export_kimetsu(filename):
    Exporter.export(controller.characters, filename)


controller = Controller()

start_dir="web"
end_point="index.html"
size=(500,600)
desktop.start(start_dir, end_point, size)