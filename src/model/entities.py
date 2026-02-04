from constants import *


class Cell:

    __x: int
    __y: int

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__marker = MARKER_EMPTY

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def is_empty(self) -> bool:
        return self.__marker == MARKER_EMPTY

    def set_marker(self, marker: int) -> None:
        if marker != MARKER_ZERO and marker != MARKER_CROSS:
            raise ValueError(f"Not found marker: {marker}")

        self.__marker = marker

    def reset(self) -> None:
        self.__marker = MARKER_EMPTY