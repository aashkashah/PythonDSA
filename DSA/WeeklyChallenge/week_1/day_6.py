


# exceptions, generators, async/await
import asyncio


class week1_day6:
    
    def parse_score(value: str | None) -> float | None:
        try:
            result = float(value)
        except(ValueError, TypeError):
            return None
            
    def passing_scores(results):
        for result in results:
            score = result["score"]
            
            if score >= 0.7: 
                yield score
                
    async def evaluate(model: str):
        await asyncio.sleep(2)
        return f"{model} evaluated" 
    
    async def main():
        models = ["gpt-a", "gpt-b", "gpt-c"]
        
        tasks = [week1_day6.evaluate(model) for model in models]
        
        results = await asyncio.gather(*tasks)
        print(results)
        
    
    asyncio.run(main())