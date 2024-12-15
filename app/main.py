from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    result = []
    neg_count = 0
    for person in friends:
        try:
            cafe.visit_cafe(person)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            neg_count += 1

    if neg_count > 0:
        return f"Friends should buy {neg_count} masks"

    if not result:
        return f"Friends can go to {cafe.name}"

    return result
