# Game Mechanics Document: 

**Version:** 1.0  
**Date:** February 7, 2026  
**Designer:** Goniprow  
**Document Purpose:** Explain how different elements of the game should function.

---

## 1. Animal Metabolism

**Eating**  
Each animal needs to eat in order to maintain energy to survive. This can be broken
down into four containers: stomach, energy, bowel. When the animal has an empty 
stomach, then they will want to eat. The animal will then eat until satiated, stomach 
is full or food is unavailable. Satiated is the threshold for when animal is no longer 
hungry. This value may equal stomach size but is intended to parameterize overeating. 
Each animal needs a parameter for stomach size, satiated, and consumption rate, i.e. 
the amount of food consumed per tick.  
   
In the simulation, when animal is "hungry" (i.e. stomach reaches zero), at each tick food 
mass will be deprecated by the minimum of the consumption rate, remaining food mass, 
and stomach space, i.e. stomach size - stomach contents. Food mass should never be less 
than 0 and stomach contents should never be greater than stomach size. Stomach contents 
increments by the same amount. Total box mass is unchanged.  

```
if cat.stomach == 0:
    cat.hungry = True
    
if cat.stomach == cat.SATIATED:
    cat.hungry = False

if cat.hungry:
    box.food_mass = box.food_mass - min(cat.CONSUMPTION_RATE, box.food_mass)
    cat.stomach = cat.stomach + min(cat.CONSUMPTION_RATE, box.food_mass, cat.STOMACH_SIZE-cat.stomach) 
    if box.food_mass < 0 or cat.stomach > cat.STOMACH_SIZE:
        ERROR
```

**Digesting**
Within the simulation, this should happen before eating to avoid digesting food
that was consumed on the same tick.  

Food in the stomach needs to be digested into energy. A fraction of the food will
become energy and the remainder will become waste. Each food will have a corresponding
energy fraction. Each animal needs a parameter for digestion rate, i.e. the amount of 
food converted to energy and waste per tick. When the animal has a full bowel, then 
they will want to defecate. Depending on box actuators, this waste may be removed 
immediately or sit until waste extractor is opened. Extracting waste is one way that
mass is removed from the box.  

```
if cat.stomach > 0:
    cat.stomach = cat.stomach - min(cat.DIGESTION_RATE, cat.stomach)
    cat.energy = cat.energy + food.ENERGY_DENSITY * min(cat.DIGESTION_RATE, cat.stomach)
    cat.bowel = cat.bowel + (1 - food.ENERGY_DENSITY) * min(cat.DIGESTION_RATE, cat.stomach)

if cat.bowel > cat.BOWEL_SIZE:
    box.waste_mass = box.waste_mass + cat.bowel
    cat.bowel = 0
```

Note: unless we explicitly prohibit digestion from occuring on the same tick that
the animal ate, digestion rate will be competing with consumption rate. In order for
the animal to ever reach satisfied, digestion rate needs to be less than consumption
rate.  

**Metabolizing**
To stay alive, the animal needs energy to maintain bodily functions. Every tick the 
animal should expend energy, the metabolic rate. When the animal is unable to support
the metabolic rate, the animal dies.  

Each animal has a container for energy. Each animal has a limit for a health amount
of energy. Energy above this limit is considered as stored fat. Too much stored fat
can cause problems for the animal (TBD).  

Every tick, energy is deprecated by the metabolic rate. However, if there is
insufficient energy, then the animal dies. Spending energy is one way that mass 
is removed from the box.  

*Old Idea*
_Each animal has two containers of energy, cat.energy which is fast energy and
cat.fat which is stored energy. Each animal has a limit for healthy amount of fast
energy. If this energy is exceeded it will convert excess energy into stored energy._  

_Every tick, the fast energy is deprecated by the metabolic rate. However, if there is
insufficient fast energy, then stored energy will be deprecated. If there is insufficient
stored energy, then the animal dies._  

```
if cat.energy <= 0:
    cat.alive = False

cat.energy = cat.energy - cat.METABOLIC_RATE
```

**Mass Accounting**
Accounting for mass throughout this metabolic process is important. We may want to
adjust the mass totals during each step or reassert the totals by summing the individual
parts at the end of the simulation cycle.  

'''
box.total_mass = cat.total_mass + box.food_mass + box.waste_mass + ...

cat.total_mass = cat.stomach + cat.energy + cat.bowel
'''
---