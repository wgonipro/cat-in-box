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
    public Simulator activeSim;

    private void Awake()
    {
        _instance = this;
    }


    private Dialog dialog = new Dialog();
    public TMP_Text dialogue;
    public TextAsset dialogFile;
    private int dialogue_index = 0;

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
        }
    }

    string GetNextDialogue() {
        dialogue_index += 1;
        if (dialogue_index >= dialog.intro.Length) {
            return "";
        }
        return dialog.intro[dialogue_index];
    }
}
