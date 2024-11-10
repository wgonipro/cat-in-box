using System;
using UnityEngine;

public class DispenserCommand : Command {
    private DeviceState state;
    private Trigger trigger;

    // trigger values
    private int mass = 0;
    private DateTime time = new DateTime();
    private Dispenser dispenser;


    public DispenserCommand(string state, string trigger, string reads, Dispenser dispenser) : base() 
    {
        commandName = "DISPENSER";
        this.dispenser = dispenser;

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
                mass = int.Parse(reads);
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
                cmdString += $"{time.Hour}:{time.Minute}";
                break;
            case Trigger.MASS:
                cmdString += $"{mass}";
                break;
        }

        return cmdString;
    }

    public override bool CheckTrigger(DateTime curTime, Box box)
    {
        switch (trigger) {
            case Trigger.TIME:
                if (SimTime.Equals(curTime, time))
                    return true;
                break;
            case Trigger.MASS:
                if (box.GetMass() == mass)
                    return true;
                break;
        }

        return false;
    }

    public override void Execute()
    {
        dispenser.SetDeviceState(state);
    }

    public override void DisplayState() {
        Debug.Log($"Dispenser: {state} | {trigger} | {mass} | {time}");
    }
}