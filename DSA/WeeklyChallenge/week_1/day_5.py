
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class EvaluationResult:
    model: str
    score: float
    passed: bool
    
@dataclass
class EvaluationRequest:
    model: str
    prompt: str
    max_tokens: int
    
class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, response: str) -> bool:
        pass
    
class LengthEvaluator(Evaluator):
    def __init__(self, min_length: int):
        self.min_length = min_length
    
    def evaluate(self, response):
        return len(response) >= self.min_length

class KeywordEvaluator(Evaluator):
    
    def __init__(self, keyword: str):
        self.keyword = keyword
        
    def evaluate(self, response: str) -> bool:
        return self.keyword.lower() in response.lower()
    
    
    