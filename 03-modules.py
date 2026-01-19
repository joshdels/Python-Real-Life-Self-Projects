from my_package import greetings, status

print(greetings.say_hello("Josh"))
print(status.like(5))

# CHEAT SHEET

# Absolute import
import my_package.file

# Relative import (inside package)
from .my_package.file2 import func

# Check module path
import sys
print(sys.path)

# Special names
print(__name__)
print(__file__)
print(__package__)

#REFLECTION
# What i understand in packaging is that the folder creates __init__.py itself to create a folder one
