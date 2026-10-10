from typing import List

class week1_day1:
    
    def count_statuses(statuses):
        counts = {}
        
        for status in statuses:
            if status in counts:
                counts[status] += 1
            else:
                counts[status] = 1
                
        ## replace with
        for status in status:
            counts[status] = counts.get(status, 0) + 1
                            
        return counts
    
    def average_scores(results: list[dict]) -> dict[str, float]:
        
        totals = {}
        counts = {}
        
        for result in results:
            
            if score not in result:
                continue 
            
            model = result["model"]
            score = result["score"]
            
            totals[model] = totals.get(model, 0) + score
            counts[model] = counts.get(model, 0) + 1 
            
        averages = {}
        
        for model in totals:
            averages[model] = totals.get(model) / counts.get(model)
            
        return averages


    
if __name__ == "__main__":
    sol = week1_day1()
    sol.average_scores()