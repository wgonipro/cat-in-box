using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class HistoryItemUI : MonoBehaviour
{
    public TMPro.TMP_Text t;
    public Button button;
    
    public RectTransform GetRectTransform() {
        return GetComponent<RectTransform>();
    }

    public void Delete() {
        Destroy(gameObject);
    }
}
