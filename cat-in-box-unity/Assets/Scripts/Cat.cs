using System;
using UnityEngine;

public class Cat : Thing
{
    public float hunger = 50;
    
    void Awake() {
        mass = 10.0f;
    }
}
