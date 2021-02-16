class PointMutations:
    """Compute the point mutation with Hamming method"""
    
    positions = list()
    
    def __init__(self, seq_one, seq_two):
        self.seq_one = seq_one
        self.seq_two = seq_two
        
    def mutated_positions(self):
        for i in range(len(self.seq_one)):
            if self.seq_one[i] != self.seq_two[i]:
                self.positions.append(i)
        return self.positions
    
    def percent_mutate(self):
        return (len(self.positions)/len(self.seq_one))*100


# Sequence 01
seq1 = 'GAGCCTACTAACGGGAT'

# Sequence 01
seq2 = 'CATCGTAATGACGGCCT'

muta = PointMutations(seq1, seq2)

muta.mutated_positions()

## OUTPUT ##  
## [0, 2, 4, 7, 9, 14, 15] ##  

muta.percent_mutate()    

## OUTPUT ##  
## 41.17647058823529 ##  