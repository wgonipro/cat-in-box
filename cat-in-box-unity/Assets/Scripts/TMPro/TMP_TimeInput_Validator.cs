using System;
using TMPro;
using UnityEngine;

[Serializable]
[CreateAssetMenu(fileName = "TMP_TimeInput_Validator", menuName = "Scriptable Objects/TimeInputValidator", order = 1)]
public class TimeInput_Validator : TMP_InputValidator
{
    private int timeLength = 5;
    private int colonIndex = 2;

    public override char Validate(ref string text, ref int pos, char ch)
    {
        Debug.Log($"Text = {text}; pos = {pos}; chr = {ch}");
        if (pos >= timeLength)
            return '\0';
        
        if (pos == colonIndex && ch != ':') {
            if (!char.IsNumber(ch)) {
                return '\0';    
            }
            pos++;
            text += ":";
        }

        if (pos != colonIndex && !char.IsNumber(ch)) {
            return '\0';
        }

        pos++;
        text += ch;
        return ch;
    }
}
