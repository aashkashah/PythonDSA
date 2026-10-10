

class week1_day2:
    
    def passing_models(results: list[dict]) -> list[str]:
        
        passed = []
        
        ## filter 
        for result in results:
            model = result["model"]
            score = result["score"]
            
            if score >= 0.7:
                passed.append(model)
            
        # python way [expression for item in collection if condition]
        # passed = [result[model] for result in results if result[score] >= 0.7] 
        
        
        ## sort results 
        sorted(results, key=lambda result: result["score"], reverse=True)
        
        
        return passed
    
    def top_models(results: list[dict]) -> list[str]:
        
        passed = [result for result in results if result["score"] >= 0.7]
        sorted_results = sorted(passed, key=lambda result: result["score"], reverse=True)
        
        return [result["model"] for result in sorted_results]

if __name__ == "__main__":
    sol = week1_day2()
    sol.average_scores()