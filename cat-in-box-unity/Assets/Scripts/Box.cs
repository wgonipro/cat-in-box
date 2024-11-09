using UnityEngine;

public class Box : MonoBehaviour
{
    public float mass; 
    public int foodUnitsAvailable;
    public Thing[] things;

    void Start() {
        UpdateMeasurements();
    }

    void Update() {
        if (Input.GetKeyDown(KeyCode.U))
            UpdateMeasurements();
    }

    void UpdateMeasurements() {
        things = GetComponentsInChildren<Thing>();
        foreach(Thing thing in things) {
            mass += thing.GetMass();
        }
    }

}
