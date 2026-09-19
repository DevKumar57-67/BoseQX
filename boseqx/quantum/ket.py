from boseqx.core import Vector


class Ket(Vector):
    """Represent a quantum ket |ψ⟩."""

    def bra(self):
        """Return the corresponding Bra ⟨ψ|."""
        from .bra import Bra
        return Bra(self.conjugate()._values)

    def __repr__(self):
        return f"Ket({self._values})"