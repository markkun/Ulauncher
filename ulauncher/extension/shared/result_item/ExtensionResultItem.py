import os
import sys
from ulauncher.helpers import load_image
from ulauncher.result_list.result_item.ResultItem import ResultItem
from ulauncher.result_list.item_action.BaseAction import BaseAction


class ExtensionResultItem(ResultItem):

    def __init__(self, *args, **kw):
        super(ExtensionResultItem, self).__init__(*args, **kw)
        self._highlightable = False
        self.extension_path = os.path.dirname(sys.argv[0])
        if self._on_enter and not isinstance(self._on_enter, BaseAction):
            raise Exception("Incorrect type of on_enter argument")

    def get_icon(self):
        if isinstance(self._icon, str):
            icon_path = self._icon

            if not icon_path.startswith('/'):
                icon_path = os.path.join(self.extension_path, icon_path)

            return load_image(icon_path, self.ICON_SIZE)
        else:
            # assuming it's Pixbuf
            return self.icon

    def on_enter(self, query):
        if self._on_enter:
            self._on_enter.run()
