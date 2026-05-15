"""Mallorca category providers."""

from memi_engine import CategoryProvider, register
from memi_engine import images

from memi_ml.categories.municipalities import (
    ALL as MUNICIPALITY_LIST,
    COMARCA_BY_MUNICIPALITY,
    FILTER as COMARCA_FILTER,
    locator_filename,
)
from memi_ml.categories.comarques import (
    ALL as COMARCA_LIST,
    MAPS as COMARCA_MAPS,
)
from memi_ml.categories.monuments import (
    ALL as MONUMENT_LIST,
    WIKIPEDIA as MONUMENT_WIKI,
    COMMONS_FILES as MONUMENT_COMMONS,
)
from memi_ml.categories.beaches import (
    ALL as BEACH_LIST,
    WIKIPEDIA as BEACH_WIKI,
)
from memi_ml.categories.food import (
    ALL as FOOD_LIST,
    WIKIPEDIA as FOOD_WIKI,
)
from memi_ml.categories.all_hands import (
    ALL as ALL_HANDS_LIST,
    IMAGES as ALL_HANDS_IMAGES,
)


class MunicipalitiesProvider(CategoryProvider):
    key = "geography:municipalities"
    items = MUNICIPALITY_LIST
    override_name = True
    filters = {"comarca": COMARCA_FILTER}

    def get_image(self, item):
        result = images.get_commons_file_image(locator_filename(item))
        if result:
            result["name"] = item
            return result
        return None

    def get_tag(self, item):
        return COMARCA_BY_MUNICIPALITY.get(item)


class ComarquesProvider(CategoryProvider):
    key = "geography:comarques"
    items = COMARCA_LIST
    override_name = True

    def get_image(self, item):
        filename = COMARCA_MAPS.get(item)
        if not filename:
            return None
        result = images.get_commons_file_image(filename)
        if result:
            result["name"] = item
            return result
        return None


class MonumentsProvider(CategoryProvider):
    key = "culture:monuments"
    items = MONUMENT_LIST
    override_name = True

    def get_image(self, item):
        commons = MONUMENT_COMMONS.get(item)
        if commons:
            result = images.get_commons_file_image(commons)
            if result:
                result["name"] = item
                return result
        return images.get_wikipedia_image(MONUMENT_WIKI.get(item, item))


class BeachesProvider(CategoryProvider):
    key = "nature:beaches"
    items = BEACH_LIST
    override_name = True

    def get_image(self, item):
        return images.get_wikipedia_image(BEACH_WIKI.get(item, item))


class FoodProvider(CategoryProvider):
    key = "food:dishes"
    items = FOOD_LIST
    override_name = True

    def get_image(self, item):
        return images.get_wikipedia_image(FOOD_WIKI.get(item, item))


class AllHandsProvider(CategoryProvider):
    key = "all hands"
    items = ALL_HANDS_LIST
    override_name = True

    def get_image(self, item):
        path = ALL_HANDS_IMAGES.get(item)
        if not path:
            return None
        return {"name": item, "image": path}


register(MunicipalitiesProvider())
register(ComarquesProvider())
register(MonumentsProvider())
register(BeachesProvider())
register(FoodProvider())
register(AllHandsProvider())
