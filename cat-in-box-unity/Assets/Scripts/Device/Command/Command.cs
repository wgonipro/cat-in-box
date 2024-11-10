using System;
using System.Collections.Generic;
using UnityEngine;

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
    static public Dictionary<string, DeviceState> stateMap = new Dictionary<string, DeviceState> {
        { "open", DeviceState.OPEN },
        { "closed", DeviceState.CLOSED }
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
        DateTime dateTime = DateTime.ParseExact(timeString, "HH:mm", null);
        return SimTime.SetDateToDefault(dateTime);
    }

    public int GetID() {
        return id;
    }

    public virtual bool CheckTrigger(DateTime curTime, Box box) { return false; }
    public virtual void DisplayState() {}
}