using TMPro;
using UnityEngine;

public class Terminal : MonoBehaviour
{
    public TMP_InputField cmdLine;
    public TMP_Text history;


    // Start is called before the first frame update
    void OnEnable()
    {
        cmdLine.onSubmit.AddListener(SubmitCommand);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void WriteToHistory(string msg) {
        history.text += "\n" + msg;
    }

    void SubmitCommand(string arg0) {
        Debug.Log(arg0);
        history.text += "\nCONSOLE> " + arg0;
        cmdLine.text = "";

        Command command = new Command(arg0);

        string[] cmdSplit = arg0.Split(" ");
        string commandStr = cmdSplit[0];
        switch (commandStr.ToLower()) {
            case "dispenser":
                command = new DispenserCommand(arg0);
                if (command.error) {
                    WriteToHistory(command.errorMsg);
                    WriteToHistory(command.GetHelpText());
                    return;
                }
                break;
            case "extractor":
                command = new ExtractorCommand(arg0);
                if (command.error) {
                    WriteToHistory(command.errorMsg);
                    WriteToHistory(command.GetHelpText());
                    return;
                }
                break;
            default:
                WriteToHistory(command.GetHelpText());
                break;
        }

        command.Execute();
    }
}
