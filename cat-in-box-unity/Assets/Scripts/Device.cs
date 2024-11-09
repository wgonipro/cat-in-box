using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class Device : MonoBehaviour
{
    
    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        InitializeUI();
    }



    /*******************************************
    *                    UI                    *
    ********************************************/
    private TMP_Dropdown stateDropdown;
    private TMP_Dropdown triggerDropdown;
    private TMP_InputField inputField;
    private Button submitButton;
    public TMP_InputValidator timeValidator;
    public TMP_InputValidator massValidator;

    void InitializeUI()
    {
        // Shouldn't use Find, will need a better way to correctly get dropdowns. Honestly could maybe be public?
        stateDropdown = transform.Find("StateDropdown").GetComponent<TMP_Dropdown>();
        triggerDropdown = transform.Find("TriggerDropdown").GetComponent<TMP_Dropdown>();
        inputField = transform.Find("ReadsInput").GetComponent<TMP_InputField>();
        submitButton = transform.Find("Submit").GetComponent<Button>();

        triggerDropdown.onValueChanged.AddListener(delegate {
            DropdownValueChanges(triggerDropdown);
        });

        submitButton.onClick.AddListener(delegate {
            SubmitCommand();
        });
    }

    void SubmitCommand()
    {
        Debug.Log($"Reads section is: {inputField.text}");
        Simulator activeSim = GameManager.instance.activeSim;
        string state = stateDropdown.options[stateDropdown.value].text;
        string trigger = triggerDropdown.options[stateDropdown.value].text;
        string reads = inputField.text;

        DispenserCommand command = new DispenserCommand(state, trigger, reads);
        activeSim.submitCommand(command);
    }

    void DropdownValueChanges(TMP_Dropdown change)
    {
        var options = change.options;
        string text = options[change.value].text;

        inputField.text = "";
        if (text.ToLower() == "mass")
            inputField.inputValidator = massValidator;
        
        if (text.ToLower() == "time")
            inputField.inputValidator = timeValidator;
        
    }
}
