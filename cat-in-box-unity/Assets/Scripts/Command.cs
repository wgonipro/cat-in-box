using System;
using System.Collections.Generic;
using System.Globalization;
using UnityEngine;

public enum State 
{
    OPEN,
    CLOSED
}

public enum Trigger
{
    TIME,
    MASS
}

public class Command 
{
    static public Dictionary<string, State> stateMap = new Dictionary<string, State> {
        { "open", State.OPEN },
        { "closed", State.CLOSED }
    };

    static public Dictionary<string, Trigger> triggerMap = new Dictionary<string, Trigger> {
        { "time", Trigger.TIME },
        { "mass", Trigger.MASS }
    };

    public Command()
    {
    }

    public virtual void Execute() {}
    public virtual string AsString() { return ""; }
    
    protected DateTime ParseTimeString(string timeString) {
        return DateTime.ParseExact(timeString, "HH:mm", null);
    }
}

public class DispenserCommand : Command {
    private string commandName = "DISPENSER";
    private State state;
    private Trigger trigger;
    private int weight = 0;
    private DateTime time = new DateTime();


    public DispenserCommand(string state, string trigger, string reads) : base() 
    {
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

public class ExtractorCommand : Command {
    private State state;
    private Trigger trigger;
    private string reads;
    private int expectedCmdLength = 4;

    public ExtractorCommand(string args0) : base()
    {
    }

    public override void Execute() {
        Debug.Log("Executing Extractor Command");
        Debug.Log($"state {state} | trigger {trigger} | reads {reads}");
    }
}