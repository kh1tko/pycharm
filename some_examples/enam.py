from enum import Enum


class TrafficLight(Enum):
    RED = 'Stop'
    GREEN = 'Go'
    YELLOW = 'Wait'


def allowed_action(traffic_light: TrafficLight) -> str:
    return traffic_light.value


if __name__ == '__main__':
    print(allowed_action(TrafficLight.YELLOW))
