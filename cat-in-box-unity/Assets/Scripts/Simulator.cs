using System;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class Simulator : MonoBehaviour
{
    List<Command> commands = new List<Command>();
    // might need to live on gamemanager
    public Cat cat;
    public Box box;
    // to here
    public List<Device> devices;
    public Button runBtn;
    public DateTime startTime { get; } = SimTime.NewTime(0, 0);
    public int cycles = 96;
    void Awake() {
        runBtn.onClick.AddListener(delegate {
            runBtn.enabled = false;
            RunSimulation();
            runBtn.enabled = true;
        });

        GameObject[] devicesObj = GameObject.FindGameObjectsWithTag("Device");
        foreach(GameObject d in devicesObj) {
            devices.Add(d.GetComponent<Device>());
        }
    }

    void Start() {
        cat = GameManager.instance.cat;
        box = GameManager.instance.box;
    }

    void RunSimulation() {
        Debug.Log("Running Simulation");
        DateTime curTime = startTime;

        for(int i = 0; i < cycles; i++) {
            foreach(Command cmd in commands) {
                if (cmd.CheckTrigger(curTime, box))
                    Debug.Log($"Executing Command - {cmd}");
                    cmd.Execute();
            }

            foreach(Device device in devices) {
                device.Activate(box, cat);
            }

            cat.ProcessTime(box);

            curTime.AddMinutes(SimTime.timeStep);
        }
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
