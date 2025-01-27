import click
import cv2
from cv2 import aruco
import numpy as np
import yaml
import os

class MarkerFactory:

    @staticmethod
    def create_marker(size, id, margin):
        aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

        # white background
        img = 255 * np.ones((size, size), dtype=np.uint8)

        # Create a marker
        img_marker = aruco.generateImageMarker(aruco_dict, id, size - 2 * margin)

        # Add marker centered
        img[margin:-margin, margin:-margin] = img_marker

        return img


class TileMap:
    _map: np.ndarray

    def __init__(self, tile_size):
        # Initialize all tiles with white (255)
        self._map = 255 * np.ones((4, 3, tile_size, tile_size), dtype=np.uint8)

    def set_tile(self, pos: tuple, img: np.ndarray, is_marker: bool = False):
        """Sets the tile at the specified position. If not a marker, keep it white."""
        if is_marker:
            assert np.all(self._map[pos[0], pos[1]].shape == img.shape)
            self._map[pos[0], pos[1]] = img

    def get_map_image(self):
        """ Merges the tile map into a single image """
        img = np.concatenate(self._map, axis=-1)
        img = np.concatenate(img, axis=-2)
        img = img.T
        return img


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--tile_size", type=int, default=100)
def main(path, tile_size):
    margin = int(0.3 * tile_size)

    marker_factory = MarkerFactory()
    tile_map = TileMap(tile_size)

    order = ['left', 'bottom', 'front', 'top', 'back', 'right']

    ids = []
    marker_id = 0

    for i in range(4):
        for j in range(3):
            if i == 1 and j == 1:  # Only the center tile is 'front'
                marker_img = marker_factory.create_marker(tile_size, marker_id, margin)
                tile_map.set_tile((i, j), marker_img, is_marker=True)
                ids.append(marker_id)
                marker_id += 1

    tile_img = tile_map.get_map_image()

    tile_img_square = np.zeros((tile_size * 4, tile_size * 4), dtype=np.uint8)
    tile_img_square[:, (tile_size // 2):(-tile_size // 2)] = tile_img

    cv2.imwrite(os.path.join(path, "marker_tile.png"), tile_img)
    cv2.imwrite(os.path.join(path, "marker_tiles_square.png"), tile_img_square)

    marker_config = dict(zip(order, ids))

    config = dict()
    config["aruco_dict"] = "6X6_250"
    config["markers"] = marker_config

    with open(os.path.join(path, "marker_info.yml"), "w") as yml_file:
        yaml.dump(config, yml_file)


if __name__ == '__main__':
    main()
