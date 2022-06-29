import numpy as np
import cv2 as cv


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]),
                                                None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv.cvtColor(img_array[x][y], cv.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]),
                                         None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv.cvtColor(img_array[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


def color2gray(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


def gray2color(frame):
    return cv.cvtColor(frame, cv.COLOR_GRAY2BGR)


def minmax_normalize(frame, norm_min=0, norm_max=255):
    return frame
    # out = None
    # out = cv.normalize(frame, out, norm_min, norm_max, cv.NORM_MINMAX)
    # return out


def adjust_contrast(frame, contrast=1):
    return cv.convertScaleAbs(frame, alpha=contrast, beta=0)


def create_conv_kernel(kernel_size, theta):
    return cv.getGaborKernel((kernel_size, kernel_size), sigma=5,
                             theta=theta, lambd=11, gamma=0.9,
                             ktype=cv.CV_32F)


def apply_conv_filter(frame, kernel):
    return cv.filter2D(frame, cv.CV_8UC3, kernel)


def binary_threshold(frame):
    _, out = cv.threshold(frame, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return out


def create_dilate_kernel(kernel_size):
    return np.ones((kernel_size, kernel_size), np.uint8)


def dilate(frame, d_kernel, iteration=2):
    return cv.dilate(frame, d_kernel, iterations=iteration)


def dilate_morphology_ex(frame, kernel, iteration=1):
    return cv.morphologyEx(frame, cv.MORPH_OPEN, kernel, iterations=iteration)


def unsharp_mask(frame, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv.GaussianBlur(frame, kernel_size, sigma)
    sharpened = float(amount + 1) * frame - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(frame - blurred) < threshold
        np.copyto(sharpened, frame, where=low_contrast_mask)
    return sharpened
