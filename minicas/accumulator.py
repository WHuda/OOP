class Accumulator:
    """Накапливает числа и считает их среднее."""
    
    def __init__(self) -> None:
        self.values: list[float] = []
        
    @classmethod
    def from_list(cls, values: list[float]) -> "Accumulator":
        accumulator = cls()
        
        for value in values:
            accumulator.add(value)
            
        return accumulator
        
    def add(self, x: float) -> None:
        self.values.append(x)
    
    @property
    def count(self) -> int:
        return len(self.values)
    
    def mean(self) -> float:
        if not self.values:
            raise ValueError("Аккумулятор пуст")
        
        return sum(self.values) / len(self.values)