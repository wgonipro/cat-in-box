using UnityEngine;

public class Extractor : Device
{
    public float flowRate = 200; // mass per 15 min
    protected override void SubmitCommand()
    {
        Debug.Log($"Reads section is: {inputField.text}");
        Simulator activeSim = GameManager.instance.activeSim;
        string state = stateDropdown.options[stateDropdown.value].text;
        string trigger = triggerDropdown.options[triggerDropdown.value].text;
        string reads = inputField.text;

        Debug.Log($"{state} {trigger} {reads}");
        ExtractorCommand command = new ExtractorCommand(state, trigger, reads, this);
        activeSim.SubmitCommand(command);
    }

    public override void Activate(Box box, Cat cat) {
        if (deviceState == DeviceState.OPEN)
            box.RemoveWasteMass(flowRate);
        return;
    }
}

