using TMPro;
using UnityEngine;

public class Terminal : MonoBehaviour
{
    public TMP_InputField cmdLine;
    public TMP_Text history;


    // Start is called before the first frame update
    void OnEnable()
    {
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void WriteToHistory(string msg) {
        history.text += "\n" + msg;
    }

}
