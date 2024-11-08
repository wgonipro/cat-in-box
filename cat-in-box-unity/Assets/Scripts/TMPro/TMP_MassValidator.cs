using UnityEngine;
using TMPro;

[CreateAssetMenu(fileName = "TMP_MassValidator", menuName = "Scriptable Objects/TMP_MassValidator")]
public class TMP_MassValidator :  TMP_InputValidator
{
    private int timeLength = 3;

    public override char Validate(ref string text, ref int pos, char ch)
    {
        if (pos >= timeLength || !char.IsNumber(ch))
            return '\0';

        pos++;
        text += ch;
        return ch;
    }
}
