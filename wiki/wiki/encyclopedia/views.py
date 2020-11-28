from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    converter = Markdown()
    return render(request, "encyclopedia/entry.html", {
        "entry": converter.convert(util.get_entry(entry))
    })