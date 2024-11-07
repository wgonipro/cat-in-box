using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.UIElements;

public class Terminal : MonoBehaviour
{
    public TMP_InputField cmdLine;
    public TMP_Text history;

    public class Command {
        public string helpText { set; get; }
        public Command() {

        }

        public virtual void Execute() {

        }
        
        public string PrintHelpText() {
            return helpText;
        }
    }

    public class DispenserCommand : Command {
        public override void Execute() {
            Debug.Log("Executing Dispenser Command");
        }
    }

    public class ExtractorCommand : Command {
        public override void Execute() {
            Debug.Log("Executing Extractor Command");
        }
    }


    // Start is called before the first frame update
    void OnEnable()
    {
        cmdLine.onSubmit.AddListener(SubmitCommand);
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void SubmitCommand(string arg0) {
        Debug.Log(arg0);
        history.text += "\nCONSOLE> " + arg0;
        cmdLine.text = "";

        Command command = new Command();

        string[] cmdSplit = arg0.Split(" ");
        string commandStr = cmdSplit[0];
        switch (commandStr.ToLower()) {
            case "dispenser":
                command = new DispenserCommand();
                break;
            case "extractor":
                command = new ExtractorCommand();
                break;
            default:
                command.helpText = "Usage ...";
                history.text += "\n" + command.helpText;
                break;
        }
    }
}
