from ulauncher.utils.icon_loader import get_themed_icon_by_name
from ulauncher.result_list.result_item.SmallResultItem import SmallResultItem
from ulauncher.result_list.item_action.ActionList import ActionList
from ulauncher.result_list.item_action.OpenAction import OpenAction


class OpenFolderItem(SmallResultItem):

    def __init__(self, path):
        """
        :param Path path:
        """
        self.path = path
        self._name = 'Open Folder'

    def set_name(self, name):
        self._name = name

    def get_name_highlighted(serlf, *args):
        pass

    def get_name(self):
        return self._name

    def get_icon(self):
        return get_themed_icon_by_name('system-file-manager', self.ICON_SIZE)

    def on_enter(self, query):
        return ActionList([OpenAction(self.path.get_abs_path())])
