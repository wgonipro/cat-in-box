using UnityEngine;
using System;
using System.Security.Cryptography;

public class Dispenser : MonoBehaviour
{
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}

public class DispenserCommand : Command {
    private State state;
    private Trigger trigger;
    private int weight = 0;
    private DateTime time = new DateTime();


    public DispenserCommand(string state, string trigger, string reads) : base() 
    {
        commandName = "DISPENSER";
        if (stateMap.ContainsKey(state.ToLower())) {
            this.state = stateMap[state.ToLower()];
        } else {
            throw new Exception("state not valid");
        }

        if (triggerMap.ContainsKey(trigger.ToLower())) {
            this.trigger = triggerMap[trigger.ToLower()];
        } else {
            throw new Exception("trigger not valid");
        }
        
        switch (this.trigger) {
            case Trigger.TIME:
                try {
                    time = ParseTimeString(reads);
                } catch (Exception e) {
                    throw new Exception($"time string failed to parse + {e}");
                }
                break;
            case Trigger.MASS:
                weight = int.Parse(reads);
                break;
            default:
                throw new Exception("reads not valid");
        }
    }

    public override string AsString()
    {
        string cmdString = $"{commandName} {state} {trigger} ";

        switch (trigger) {
            case Trigger.TIME:
                cmdString += $"{time}";
                /// cmdString += $"{time.Hour}:{time.Minute}";
                break;
            case Trigger.MASS:
                cmdString += $"{weight}";
                break;
        }

        return cmdString;
    }

    public override void Execute()
    {
        base.Execute();
        Debug.Log($"Dispenser: {state} | {trigger} | {weight} | {time}");
    }
}