from boseqx.core import Vector


class Bra(Vector):
    """Represent a quantum bra ⟨ψ|."""

    def ket(self):
        """Return the corresponding Ket |ψ⟩."""
        from .ket import Ket
        return Ket(self.conjugate()._values)

    def inner(self, ket):
        """Calculate the inner product ⟨bra|ket⟩."""
        if len(self) != len(ket):
            raise ValueError("Vectors must have the same dimension.")

        return sum(
            a * b
            for a, b in zip(self._values, ket._values)
        )

    def __repr__(self):
        return f"Bra({self._values})"