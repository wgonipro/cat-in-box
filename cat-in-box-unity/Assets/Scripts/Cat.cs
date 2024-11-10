using System;
using System.Collections.Generic;
using UnityEngine;

public class Cat : Thing
{
    public float desiredFoodMass { get; } = 180f;
    public double minToStarve { get; } = 72d * SimTime.minInHour / SimTime.timeStep;
    public double minForDigestion { get; } = 1d * SimTime.minInHour / SimTime.timeStep;
    public float numOfMeals { get; } = 3;
    public float mealSize;
    bool isAlive = true;
    private float hunger;
    public float massConsumed = 0;
    public int cyclesPassed = 0;
    public int firstAte = 0;
    
    void Awake() {
        mass = 4500.0f;
        hunger = desiredFoodMass;
        mealSize = desiredFoodMass / numOfMeals;
    }

    float Eat(float foodMass) {
        float massToEat = Mathf.Min(foodMass, mealSize);
        massConsumed += massToEat;

        if (massToEat > 0 && firstAte == 0) {
            firstAte = cyclesPassed;
        }

        hunger = Mathf.Max(hunger + massConsumed, desiredFoodMass);

        return massToEat;
    }

    float Shit() {
        float shitMass = massConsumed;
        massConsumed = 0;
        return shitMass;
    }

    public void ProcessTime(Box box) {
        if (!isAlive) {
            return;
        }

        hunger -= desiredFoodMass / (float)minToStarve;
        // eat if one full meal is hungry for
        if (hunger <= desiredFoodMass - mealSize) {
            float massConsumed = Eat(box.GetFoodMass());
            box.ConsumeFoodMass(massConsumed);
        }

        // time math - get minutes pasth
        if (firstAte * SimTime.timeStep >= minForDigestion) {
            float shitMass = Shit();
            box.ProduceWasteMass(shitMass);
        }

        if (hunger <= 0) {
            Debug.Log("Cat has died");
            isAlive = false;
            return;
        }
    }
}
