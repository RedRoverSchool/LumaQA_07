from dataclasses import dataclass

from locators.base_page_locators import BasePageLocators
from locators.item_page_locators import ItemPageLocators


@dataclass
class Item:
    item_locator: tuple
    add_to_cart_locator: tuple
    nav_list_item_locator: tuple
    nav_locator: tuple


@dataclass
class GearItem(Item):
    nav_locator: tuple = BasePageLocators.LINK_GEAR


@dataclass
class GearWatchItem(GearItem):
    nav_list_item_locator: tuple = BasePageLocators.LINK_GEAR_WATCHES


@dataclass
class GearWatchClamber(GearWatchItem):
    item_locator: tuple = ItemPageLocators.LINK_CLAMBER_WATCH
    add_to_cart_locator: tuple = ItemPageLocators.ADD_TO_CART_CLAMBER_WATCH_BUTTON


@dataclass
class GearWatchEndurance(GearWatchItem):
    item_locator: tuple = ItemPageLocators.LINK_ENDURANCE_WATCH
    add_to_cart_locator: tuple = ItemPageLocators.ADD_TO_CART_ENDURANCE_WATCH_BUTTON
