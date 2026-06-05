"""Mallorca category providers."""

from memi_engine import CategoryProvider, ScientificNameProvider, register
from memi_engine import images

from memi_ml.categories.municipalities import (
    ALL as MUNICIPALITY_LIST,
    REGION_BY_MUNICIPALITY,
    FILTER as REGION_FILTER,
    locator_filename,
)
from memi_ml.categories.regions import (
    ALL as REGION_LIST,
    MAPS as REGION_MAPS,
)
from memi_ml.categories.monuments import (
    ALL as MONUMENT_LIST,
    WIKIPEDIA as MONUMENT_WIKI,
    STATIC_FILES as MONUMENT_STATIC,
)
from memi_ml.categories.landscapes import (
    ALL as LANDSCAPE_LIST,
    WIKIPEDIA as LANDSCAPE_WIKI,
    COMMONS_FILES as LANDSCAPE_COMMONS,
    ALTITUDES as LANDSCAPE_ALTITUDES,
)
from memi_ml.categories.animals import (
    ALL as ANIMAL_LIST,
    WIKIPEDIA as ANIMAL_WIKI,
    SCIENTIFIC_NAMES as ANIMAL_SCIENTIFIC,
)
from memi_ml.categories.plants import (
    ALL as PLANT_LIST,
    WIKIPEDIA as PLANT_WIKI,
    SCIENTIFIC_NAMES as PLANT_SCIENTIFIC,
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
    filters = {"region": REGION_FILTER}

    def get_image(self, item):
        result = images.get_commons_file_image(locator_filename(item))
        if result:
            result["name"] = item
            return result
        return None

    def get_tag(self, item):
        return REGION_BY_MUNICIPALITY.get(item)


class RegionsProvider(CategoryProvider):
    key = "geography:comarques"
    items = REGION_LIST
    override_name = True

    def get_image(self, item):
        filename = REGION_MAPS.get(item)
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
        static = MONUMENT_STATIC.get(item)
        if static:
            return {"name": item, "image": static}
        return images.get_wikipedia_image(MONUMENT_WIKI.get(item, item))


class LandscapesProvider(CategoryProvider):
    key = "nature:landscapes"
    items = LANDSCAPE_LIST
    override_name = True

    def get_image(self, item):
        commons = LANDSCAPE_COMMONS.get(item)
        if commons:
            result = images.get_commons_file_image(commons)
            if result:
                result["name"] = item
                return result
        return images.get_wikipedia_image(LANDSCAPE_WIKI.get(item, item))

    def get_tag(self, item):
        return LANDSCAPE_ALTITUDES.get(item)


class AnimalsProvider(ScientificNameProvider):
    key = "nature:animals"
    items = ANIMAL_LIST
    override_name = True
    scientific_names = ANIMAL_SCIENTIFIC

    def get_image(self, item):
        return images.get_wikipedia_image(ANIMAL_WIKI.get(item, item))


class PlantsProvider(ScientificNameProvider):
    key = "nature:plants"
    items = PLANT_LIST
    override_name = True
    scientific_names = PLANT_SCIENTIFIC

    def get_image(self, item):
        return images.get_wikipedia_image(PLANT_WIKI.get(item, item))


class FoodProvider(CategoryProvider):
    key = "culture:food"
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
register(RegionsProvider())
register(MonumentsProvider())
register(LandscapesProvider())
register(AnimalsProvider())
register(PlantsProvider())
register(FoodProvider())
register(AllHandsProvider())
