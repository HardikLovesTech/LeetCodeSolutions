"""
Calculates the minimum time required to visit all given points on a 2D plane in the specified order.

Each move can be:
- 1 unit vertically (up or down) in 1 second,
- 1 unit horizontally (left or right) in 1 second,
- or 1 unit diagonally (both vertically and horizontally by 1 unit) in 1 second.

You must visit the points in the order provided by the input list. Passing through other points is allowed, but only visiting them in order counts.

Args:
    points (List[List[int]]): A list of points, where each point is represented as [x, y] with integer coordinates.

Returns:
    int: The minimum time in seconds required to visit all the points in the given order.
"""