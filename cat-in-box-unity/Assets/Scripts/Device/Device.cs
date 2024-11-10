using UnityEngine;
using TMPro;
using UnityEngine.UI;

public enum DeviceState 
{
    OPEN,
    CLOSED
}

public class Device : MonoBehaviour
{
    protected DeviceState deviceState = DeviceState.CLOSED;
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    protected void Start()
    {
        InitializeUI();
    }

    /*******************************************
    *                    UI                    *
    ********************************************/
    // Till end should be private - keeping public to debug
    public TMP_Dropdown stateDropdown;
    public TMP_Dropdown triggerDropdown;
    public TMP_InputField inputField;
    public Button submitButton;
    // end
    public TMP_InputValidator timeValidator;
    public TMP_InputValidator massValidator;

    protected void InitializeUI()
    {
        TMP_Dropdown[] dropdowns = transform.GetComponentsInChildren<TMP_Dropdown>();
        foreach(TMP_Dropdown dropdown in dropdowns) {
            // definitely not ideal to use names - will come back to fix. Maybe use tags?
            if (dropdown.name.ToLower().Contains("state"))
                stateDropdown = dropdown;

            if (dropdown.name.ToLower().Contains("trigger"))
                triggerDropdown = dropdown;
        }

        inputField = transform.GetComponentInChildren<TMP_InputField>();
        submitButton = transform.GetComponentInChildren<Button>();

        triggerDropdown.onValueChanged.AddListener(delegate {
            DropdownValueChanges(triggerDropdown);
        });

        submitButton.onClick.AddListener(delegate {
            SubmitCommand();
        });
    }

    protected virtual void SubmitCommand()
    {
        Debug.Log($"Reads section is: {inputField.text}");
        // Simulator activeSim = GameManager.instance.activeSim;
        // string state = stateDropdown.options[stateDropdown.value].text;
        // string trigger = triggerDropdown.options[triggerDropdown.value].text;
        // string reads = inputField.text;

        // Debug.Log($"{state} {trigger} {reads}");
        // DispenserCommand command = new DispenserCommand(state, trigger, reads);
        // activeSim.SubmitCommand(command);
    }

    protected void DropdownValueChanges(TMP_Dropdown change)
    {
        var options = change.options;
        string text = options[change.value].text;

        inputField.text = "";
        if (text.ToLower() == "mass")
            inputField.inputValidator = massValidator;
        
        if (text.ToLower() == "time")
            inputField.inputValidator = timeValidator;
        
    }

    public virtual void Activate(Box box, Cat cat) {
        return;
    }

    public void SetDeviceState(DeviceState state) {
        deviceState = state;
    }

    public DeviceState GetDeviceState() {
        return deviceState;
    }
}
