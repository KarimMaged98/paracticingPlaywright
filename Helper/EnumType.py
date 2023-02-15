from enum import StrEnum


class TheEnum(StrEnum):
    siteProduction = "https://www.floward.com"
    hubProduction = "https://hub.floward.io/"
    siteStage = "https://webcom.staging.floward.io/"
    hubStage = "https://hub.staging.floward.io"


def navigation(type: TheEnum) -> StrEnum:
    if type == TheEnum.siteProduction:
        return TheEnum.siteProduction

    elif type == TheEnum.hubProduction:
        return TheEnum.hubProduction

    elif type == TheEnum.siteStage:
        return TheEnum.siteStage

    elif type == TheEnum.hubStage:
        return TheEnum.hubStage

