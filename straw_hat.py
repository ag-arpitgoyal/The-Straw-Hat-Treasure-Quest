import crewmate
import heap
import treasure

class StrawHatTreasury:
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        self.crewmates_heap = heap.Heap(
            comparison_function=heap.compare_crewmates, 
            init_array=[crewmate.CrewMate() for _ in range(m)]
        )
        self.active_crewmates = []
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        min_load_crewmate = self.crewmates_heap.top()
        self.crewmates_heap.extract()
        
        if len(min_load_crewmate.treasures) == 0:
            self.active_crewmates.append(min_load_crewmate)

        min_load_crewmate.treasures.append(treasure)
        min_load_crewmate.load = max(min_load_crewmate.load, treasure.arrival_time) + treasure.size
        self.crewmates_heap.insert(min_load_crewmate)
        
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their ids after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        all_treasures = []  # To store treasures with updated completion times

        for crewmate in self.active_crewmates:
            current_time = 0
            treasure_heap = heap.Heap(comparison_function=heap.compare_treasures, init_array=[])
            
            for treasure in crewmate.treasures:
                diff = treasure.arrival_time - current_time

                while len(treasure_heap.heap) > 0 and diff >= treasure_heap.top()[1]:
                    completed_treasure, rem_size = treasure_heap.extract()
                    
                    completed_treasure.completion_time = current_time + rem_size
                    current_time += rem_size
                    
                    all_treasures.append(completed_treasure)
                    diff = treasure.arrival_time - current_time
                
                if len(treasure_heap.heap) == 0:
                    current_time = treasure.arrival_time
                    treasure_heap.insert((treasure, treasure.size))
                else:
                    semi_treasure, rem_size = treasure_heap.extract()
                    treasure_heap.insert((semi_treasure, rem_size-diff))
                    current_time = treasure.arrival_time
                    treasure_heap.insert((treasure, treasure.size))
                    
            
            while len(treasure_heap.heap) > 0:
                
                completed_treasure, rem_size = treasure_heap.extract()
                completed_treasure.completion_time = current_time + rem_size
                current_time += rem_size
                all_treasures.append(completed_treasure)

        all_treasures.sort(key=lambda x: x.id)
        
        return all_treasures