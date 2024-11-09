using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Simulator : MonoBehaviour
{
    public GameObject history;
    public GameObject historyItemPrefab;

    List<Command> commands = new List<Command>();
    public void submitCommand(Command command) {
        Command cmd = command;
        commands.Add(cmd);
        Debug.Log(command.AsString());

        GameObject histItem = Instantiate(historyItemPrefab);
        
    }
}
