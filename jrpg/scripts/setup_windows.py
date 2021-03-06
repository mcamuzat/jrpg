#!/usr/bin/python

# Run under cmd: setup.py py2exe -b 2 -O2

from distutils.core import setup
import py2exe
import glob

setup(
  windows=["jrpg.py"],
  data_files=[
    ("maps", glob.glob("maps/*")),
    ("data", ["data/demons-kana.txt", "data/demons-kanawords.txt", "data/demons-kanji.txt", "data/hints-kanji.txt", "data/tanaka.txt", "data/tanaka_idx.txt"]),
    ("images", ["images/angband.png", "images/angel-blue.png", "images/arab-trader.png", "images/bg-blueforestroad.jpg", "images/bg-coldlava.jpg", "images/bg-desert.jpg", "images/bg-forestsunrise.jpg", "images/bg-ice.jpg", "images/bg-marsh.jpg", "images/bg-sadbluetree.jpg", "images/bg-stonewall.jpg", "images/dwarf-smith.png", "images/elf-monk.png", "images/elf-trader.png", "images/female-blue.png", "images/jrpg-icon.png", "images/king.png", "images/nurse.png", "images/soldier-axe.png", "images/soldier-elf.png", "images/wizard-gray.png"]),
    ("font", glob.glob("font/*")),
    "README",
    "DESIGN",
  ]
)
