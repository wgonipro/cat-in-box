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
    protected Dictionary<string, State> stateMap = new Dictionary<string, State> {
        { "open", State.OPEN },
        { "closed", State.CLOSED }
    };

    protected Dictionary<string, Trigger> triggerMap = new Dictionary<string, Trigger> {
        { "time", Trigger.TIME },
        { "mass", Trigger.MASS }
    };

    protected string[] args;
    protected string helpText = "Usage:\nplease type dispenser or extractor for more info";
    public bool error = false;
    public string errorMsg;

    public Command(string args0)
    {
        args = args0.Split(" ");
    }

    public virtual void Execute() {}
    protected virtual void ParseInput() {}
    
    protected System.DateTime ParseTime(string timeArg) {
        return System.DateTime.Parse(timeArg);
    }

    public string GetHelpText() 
    {
        return helpText;
    }
}

public class DispenserCommand : Command {
    private State state;
    private Trigger trigger;
    private string weight;
    private System.DateTime time;
    private int expectedCmdLength = 4;


    public DispenserCommand(string args0) : base(args0) 
    {
        helpText = "Usage:\ndispenser {state} {trigger} {reads}";
        helpText += "\n state: open or closed";
        helpText += "\n trigger: time or mass";
        helpText += "\n reads: 00:00 or 10kg";

        ParseInput();
    }

    protected override void ParseInput()
    {
        base.ParseInput();
        
        if (args.Length != expectedCmdLength) {
            error = true;
            errorMsg = "parameters invalid";
            return;
        }

        string stateArg = args[1].ToLower();
        string triggerArg = args[2].ToLower();

        if (stateMap.ContainsKey(stateArg)) {
            state = stateMap[stateArg];
        } else {
            error = true;
            errorMsg = "state parameter invalid";
            return;
        }

        if (triggerMap.ContainsKey(triggerArg)) {
            trigger = triggerMap[triggerArg];
        } else {
            error = true;
            errorMsg = "trigger parameter invalid";
            return;
        }

        switch (trigger) {
            case Trigger.TIME:
                time = ParseTime(args[3]);
                break;
            case Trigger.MASS:
                break;
        }
    }

    public override void Execute() {
        Debug.Log("Executing Dispenser Command");
        Debug.Log($"state {state} | trigger {trigger} | time {time}");
    }
}

public class ExtractorCommand : Command {
    private State state;
    private Trigger trigger;
    private string reads;
    private int expectedCmdLength = 4;

    public ExtractorCommand(string args0) : base(args0)
    {
        helpText = "Usage:\nextractor {state} {trigger} {reads}";
        helpText += "\n state: open or closed";
        helpText += "\n trigger: time or mass";
        helpText += "\n reads: 00:00 or 10kg";

        ParseInput();
    }

    protected override void ParseInput()
    {
        base.ParseInput();
        if (args.Length != expectedCmdLength) {
            error = true;
            errorMsg = "parameters invalid";
            return;
        }

        string stateArg = args[1].ToLower();
        string triggerArg = args[2].ToLower();

        if (stateMap.ContainsKey(stateArg)) {
            state = stateMap[stateArg];
        } else {
            error = true;
            errorMsg = "state parameter invalid";
            return;
        }

        if (triggerMap.ContainsKey(triggerArg)) {
            trigger = triggerMap[triggerArg];
        } else {
            error = true;
            errorMsg = "trigger parameter invalid";
            return;
        }

        switch (trigger) {
            case Trigger.TIME:
                reads = args[3];
                break;
            case Trigger.MASS:
                reads = args[3];
                break;
        }
    }

    public override void Execute() {
        Debug.Log("Executing Extractor Command");
        Debug.Log($"state {state} | trigger {trigger} | reads {reads}");
    }
}