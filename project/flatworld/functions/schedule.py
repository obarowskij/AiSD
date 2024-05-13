from random import randint

class Guards:
    def __init__(self,id,energy):
        self.id = id
        self.energy = energy
        self.patrol_day = 0
    def __str__(self):
        if self.patrol_day == 0:
            return f"({self.id}, {self.energy})"
        else:
            return f"({self.id}, {self.energy}, dzien: {self.patrol_day})"
    def get_energy(self):
        return self.energy
    def set_patrol_day(self,day):
        self.patrol_day = day
    __repr__ = __str__

def generate_flat_schedule(people):
    guards = [Guards(i,randint(1,100)) for i in range(1,people)]
    sorted_guards = sorted(guards, key=lambda x: x.energy, reverse=True)
    chosen_guards = [guard.id for guard in sorted_guards[:7]]
    #for _ in range(7):
    #    guard = max(guards,key=lambda x: x.energy)
    #    chosen_guards.append(guard.id)


    print(chosen_guards)
    for i in chosen_guards:
        print(guards[i-1])


    return 0
generate_flat_schedule(20)