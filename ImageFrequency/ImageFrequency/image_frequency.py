import numpy as np
from PIL import Image
from FFT import FFT_image_max


class image_frequency:
    def __init__(self, image):
        self.img = Image.open(image).convert("L")
        self.numpy_img_row = np.array(self.img)
        self.numpy_img_column = np.array(self.img).T
        self.cc_row = []
        self.cc_column = []
        self.m = self.numpy_img_row.shape[0]
        self.n = self.numpy_img_row.shape[1]

    def correlation_coefficient_row(self):
        for r in range(0, self.m-1):
            if np.std(self.numpy_img_row[r]) == 0.0 or np.std(self.numpy_img_row[r+1]) == 0.0:
                continue
            else:
                coef = np.corrcoef(
                    self.numpy_img_row[r], self.numpy_img_row[r+1])
                self.cc_row.append(coef[0][1])
        return (FFT_image_max(self.cc_row))

    def correlation_coefficient_column(self):
        for r in range(0, self.n-1):
            if np.std(self.numpy_img_column[r]) == 0.0 or np.std(self.numpy_img_column[r+1]) == 0.0:
                continue
            else:
                coef = np.corrcoef(
                    self.numpy_img_column[r], self.numpy_img_column[r+1])
                self.cc_column.append(coef[0][1])
        return (FFT_image_max(self.cc_column))

    def __del__(self):
        pass
