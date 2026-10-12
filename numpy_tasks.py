"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    p = matrices @ vectors
    r = np.sum(p, axis=0)
    return r


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    r = np.where(matrix > threshold, 1, 0)
    return r


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    return [np.unique(row).tolist() for row in matrix]
def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    return [np.unique(col).tolist() for col in matrix.T]


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    np.random.seed(seed)
    m = np.random.normal(mean, std, (rows, columns))
    a = np.mean(m, axis=1)
    b = np.mean(m, axis=0)
    c = np.var(m, axis=1)
    d = np.var(m, axis=0)
    return MatrixStatistics(m, a, b, c, d)


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    i, j = np.indices((rows, columns))
    r = np.where((i + j) % 2 == 0, first, second)
    return r


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    r = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)
    cy = image_height // 2
    cx = image_width // 2
    y1 = cy - height // 2
    y2 = y1 + height
    x1 = cx - width // 2
    x2 = x1 + width
    r[y1:y2, x1:x2] = shape_color
    return r


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    y, x = np.indices((image_height, image_width))
    y0 = image_height // 2
    x0 = image_width // 2
    mask = ((x - x0) ** 2) / (semi_axis_x ** 2) + ((y - y0) ** 2) / (semi_axis_y ** 2) <= 1
    r = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)
    r = np.where(mask[..., None], shape_color, r)
    return r


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    a = np.mean(values)
    b = np.var(values)
    c = np.std(values)
    d = np.where((values[1:-1] > values[:-2]) & (values[1:-1] > values[2:]))[0] + 1
    e = np.where((values[1:-1] < values[:-2]) & (values[1:-1] < values[2:]))[0] + 1
    f = np.convolve(values, np.ones(window) / window, mode='valid')
    return TimeSeriesStatistics(a, b, c, d, e, f)


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    if class_count is None:
        class_count = np.max(labels) + 1
    r = np.eye(class_count)[labels]
    return r
