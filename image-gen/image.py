import pathlib
import matplotlib.pyplot as plt
from PIL import Image as PilImg


IMG_PATH = pathlib.Path().resolve() / "images"


class Image:
    def __init__(self, img_x: int = 800, img_y: int = 800):
        self._img = PilImg.new('RGB', [img_x, img_y], 255)
        self.file_name = None

    @staticmethod
    def get_file_name() -> str:
        """Get the number from the last file name, increments it by one and returns the full file name for an img."""
        files = list(IMG_PATH.glob("*.png"))
        next_file_num = len(files)
        return f"image{next_file_num}.png"

    def create(self) -> PilImg:
        image = self._img.load()
        for x, y in zip(range(1, self._img.width), range(self._img.height)):
            print(image[x, y])

    def display(self):
        """Display the current image on a plot."""
        plt.imshow(self._img)
        plt.show()

    def save(self) -> None:
        """Save the image to the next available file name."""
        if not IMG_PATH.exists():
            IMG_PATH.mkdir()
        self._img.save(IMG_PATH / self.get_file_name())
