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
    static int _id = 0;
    int id;
    protected string commandName = "DEFAULT";
    public HistoryItemUI histItemUI;
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
        id = ++_id;
        Debug.Log($"{commandName} has id {id} and static id is now {_id}");
    }

    public virtual void Execute() {}
    public virtual string AsString() { return ""; }
    
    protected DateTime ParseTimeString(string timeString) {
        return DateTime.ParseExact(timeString, "HH:mm", null);
    }

    public int GetID() {
        return id;
    }
}