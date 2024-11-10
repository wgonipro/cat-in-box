using UnityEngine;

public class Box : MonoBehaviour
{
    private float mass;
    public float massDisplay;
    private float foodMass;
    private float wasteMass;
    public Thing[] things;

    void Start() {
        UpdateMeasurements();
    }

    void Update() {
        if (Input.GetKeyDown(KeyCode.U))
            UpdateMeasurements();

        if (mass != massDisplay) {
            massDisplay = mass;
        }
    }

    void UpdateMeasurements() {
        things = GetComponentsInChildren<Thing>();
        foreach(Thing thing in things) {
            mass += thing.GetMass();
        }
    }

    public float GetMass() {
        return mass;
    }

    public float AddFoodMass(float mass) {
        foodMass += mass;
        this.mass += mass;
        Debug.Log($"Adding Food Mass. Food mass is now {foodMass}");
        return foodMass;
    }

    public float GetFoodMass() {
        return foodMass;
    }

    public float ConsumeFoodMass(float mass) {
        foodMass -= mass;
        if (foodMass < 0) {
            foodMass = 0;
        }
        Debug.Log($"Consuming Food Mass. Food mass is now {foodMass}");
        return foodMass;
    }

    public float ProduceWasteMass(float mass) {
        wasteMass += mass;
        Debug.Log($"Producing Waste Mass. Waste mass is now {wasteMass}");
        return wasteMass;
    }

    public float RemoveWasteMass(float mass) {
        if (wasteMass < mass) {            
            this.mass -= wasteMass;
            wasteMass = 0;
            return wasteMass;
        }
        
        wasteMass -= mass;
        this.mass -= mass;
        Debug.Log($"Removing Waste Mass. Waste mass is now {wasteMass}");
        return wasteMass;
    }
}
