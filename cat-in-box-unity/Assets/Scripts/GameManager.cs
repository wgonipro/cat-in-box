using System;
using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using System.IO;

public class GameManager : MonoBehaviour
{
    private static GameManager _instance;
    public static GameManager instance
    {
        get
        {
            if(_instance is null)
                Debug.LogError("GameManager is NULL");
            
            return _instance;
        }
    }

    public TMP_Text dialogue;
    public TextAsset dialogFile;
    public GameObject terminal;
    private bool isTerminalActive = false;
    private int dialogue_index = 0;
    Dialog dialog = new Dialog();

    private void Awake()
    {
        _instance = this;
    }

    // Start is called before the first frame update
    void Start()
    {
        dialog = JsonUtility.FromJson<Dialog>(dialogFile.text);
        dialogue.text = dialog.intro[0];   
    }

    // Update is called once per frame
    void Update()
    {
        if (dialogue_index < dialog.intro.Length) {
            if (Input.GetKeyDown(KeyCode.Return)) {
                dialogue.text = GetNextDialogue();
            }
        } else if (!isTerminalActive) {
            isTerminalActive = true;
            terminal.SetActive(isTerminalActive);
        }
    }

    string GetNextDialogue() {
        dialogue_index += 1;
        if (dialogue_index >= dialog.intro.Length) {
            Debug.Log(dialog.intro.Length);
            return dialog.intro[dialog.intro.Length - 1];
        }
        return dialog.intro[dialogue_index];
    }
}
