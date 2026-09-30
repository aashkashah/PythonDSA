from typing import List

class week1:
    # lists, dicts from memory
    # create an empty list
    
    def printList(self) -> None:
        
        my_list: List[int] = []
        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.append(4)
        my_list.append(5)
        
        print(my_list[4])
        
    def printDict(self) -> None:
        
        my_dict: dict[int, str] = {}
        my_dict[1] = "apple"
        my_dict[2] = "orange"
        
        for (k,v) in my_dict.items():
            print(v)
    
    def find_user(users: list[dict], user_id: int) -> dict | None:
        for user in users:
            if user["id"] == user_id:
                return user
            
        return None

    def group_by_team(employees):
        my_dict = {}
        
        for employee in employees:
            team = employee["team"]
            name = employee["name"]
            
            if team not in my_dict:
                my_dict[team] = 0
                
            my_dict[team] += 1

            #my_dict[team] = my_dict.get(team, 0) + 1
            
        return my_dict
    
    def learn_sets() -> None:
        skills = {"python", "sql", "python"}
        
        print(skills)

    
if __name__ == "__main__":
    sol = week1()
    sol.printDict()