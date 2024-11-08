using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class CommandUI : MonoBehaviour
{
    private TMP_Dropdown stateDropdown;
    private TMP_Dropdown triggerDropdown;
    private TMP_InputField inputField;
    public TMP_InputValidator timeValidator;
    public TMP_InputValidator massValidator;
    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        stateDropdown = transform.Find("StateDropdown").GetComponent<TMP_Dropdown>();
        triggerDropdown = transform.Find("TriggerDropdown").GetComponent<TMP_Dropdown>();
        inputField = transform.Find("ReadsInput").GetComponent<TMP_InputField>();

        triggerDropdown.onValueChanged.AddListener(delegate {
            DropdownValueChanges(triggerDropdown);
        });
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
