import math


class Vector:
    """A mathematical vector supporting real and complex numbers."""

    def __init__(self, values):
        self._values = list(values)

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension.")

        return Vector(
            a + b
            for a, b in zip(self._values, other._values)
        )

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension.")

        return Vector(
            a - b
            for a, b in zip(self._values, other._values)
        )

    def __mul__(self, scalar):
        return Vector(
            value * scalar
            for value in self._values
        )

    def __rmul__(self, scalar):
        return self * scalar

    def norm(self):
        return math.sqrt(
            sum(abs(value) ** 2 for value in self._values)
        )

    def normalize(self):
        magnitude = self.norm()

        if magnitude == 0:
            raise ValueError("Cannot normalize the zero vector.")

        return self * (1 / magnitude)
    

    def inner(self, other):
        """Return the complex inner product <self|other>."""
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension.")

        return sum(
        a.conjugate() * b
        for a, b in zip(self._values, other._values)
    )

    def conjugate(self):
        """Return the component-wise complex conjugate."""
        return Vector(
        value.conjugate()
        for value in self._values
    )

    def __repr__(self):
        return f"Vector({self._values})"