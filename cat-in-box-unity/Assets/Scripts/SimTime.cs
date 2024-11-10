using System;
using UnityEngine;

public class SimTime : MonoBehaviour
{
    static DateTime defaultDate = new DateTime(2024, 11, 01);
    static public double timeStep = 15.0d;
    static public double minInHour = 60.0d;


    public static DateTime SetDateToDefault(DateTime dateTime) {
        return new DateTime(defaultDate.Year, defaultDate.Month, defaultDate.Day, dateTime.Hour, dateTime.Minute, 0);
    }

    public static DateTime NewTime(int hour, int minute) {
        return new DateTime(defaultDate.Year, defaultDate.Month, defaultDate.Day, hour, minute, 0);
    }

    public static bool Equals(DateTime a, DateTime b) {
        if (a.Hour == b.Hour && a.Minute == b.Minute)
            return true;

        return false;
    }
}