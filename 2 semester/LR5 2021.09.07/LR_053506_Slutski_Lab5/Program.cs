using System;
using LR_053506_Slutski_Lab5.Collections;
using LR_053506_Slutski_Lab5.Entities;


namespace LR_053506_Slutski_Lab5
{
    internal static class Program
    {
        private static void Main()
        {
            var station = new AutomaticTelephoneStation();
            
            station.AddTarrif(new Tariff());
        }
    }
}