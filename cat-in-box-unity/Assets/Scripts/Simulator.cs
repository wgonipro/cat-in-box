using System;
using System.Collections.Generic;
using System.Linq;
using Unity.VisualScripting;
using UnityEditor.Search;
using UnityEngine;
using UnityEngine.UI;

public class Simulator : MonoBehaviour
{
    List<Command> commands = new List<Command>();
    public Cat cat;
    public Box box;
    public Button runBtn;
    public DateTime startTime { get; } = SimTime.NewTime(9, 0);
    public DateTime endTime { get; } = SimTime.NewTime(21, 0);
    public double timeStep = 30.0d;
    void Awake() {
        runBtn.onClick.AddListener(delegate {
            runBtn.enabled = false;
            RunSimulation();
        });
    }

    void RunSimulation() {
        Debug.Log("Running Simulation");
        // DateTime curTime = startTime;
        // while(curTime != endTime) {
        //     if (curTime.Minute == 0)
        //         cat.hunger += 10;

        //     curTime.AddMinutes(timeStep);
        // }
    }

    // UI + more

    public GameObject history;
    public GameObject historyItemPrefab;
    public float offset = 15.0f;

    
    public void SubmitCommand(Command command) {

        GameObject histItem = Instantiate(historyItemPrefab, history.transform);
        command.histItemUI = histItem.GetComponent<HistoryItemUI>();
        
        commands.Add(command);
        command.histItemUI.button.onClick.AddListener(delegate {
            DeleteCommand(command);
        });
        SetItemPosition(command.histItemUI);

        // TODO: Resize the history window when we need to scroll more + handle deletion space fixes

        command.histItemUI.t.text = command.AsString().ToUpper();
        histItem.SetActive(true);
    }

    public void DeleteCommand(Command command) {
        int j = 0;
        foreach(Command cmd in commands) {
            int id = cmd.GetID();
            cmd.Execute();
            Debug.Log($"{id} is located at {j}");
            j++;
        }
        int index = commands.IndexOf(command);

        // TODO figure out if we should delete the command since now it is dangling
        commands.Remove(command);
        command.histItemUI.Delete();

        for (int i = index; i < commands.Count; i++) {
            RectTransform transform = commands[i].histItemUI.GetRectTransform();
            float height = transform.rect.height;
            transform.position = new Vector3(transform.position.x, transform.position.y + (height + offset));
        }
    }

    public void SetItemPosition(HistoryItemUI histItemUI) {
        RectTransform histItemTransform = histItemUI.GetRectTransform();
        float yPos = histItemTransform.position.y;
        float height = histItemTransform.rect.height;

        yPos -= (height + offset) * (commands.Count - 1);
        histItemTransform.position = new Vector3(histItemTransform.position.x, yPos);
    }
}
