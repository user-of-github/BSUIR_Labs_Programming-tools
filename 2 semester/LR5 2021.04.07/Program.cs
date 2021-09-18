using System;

namespace LR5_2021._04._07
{
    internal static class Program
    {
        private static void Main()
        {
            var myLaptop = new Laptop(2700, new string[] {"AMD", "Ryzen 7 4800H"}, new string[] {"512", "8"},
                "Windows 10", 2000,
                144);

            myLaptop.PrintInfo();
            /*  Laptop:
                OS: Windows 10
                Cost: 2700 BYN
                Vendor of CPU: AMD
                Weight is : 2000 KG
                Frequency of Updating the screen is : 144 Hz*/


            var myPhone = new Smartphone(600, new string[] {"Hisilicon", "Kirin 970"}, new string[] {"128", "4"},
                "Android 10 EMUI 10", 150,
                true);

            myPhone.PrintInfo();

            /*  Smartphone:
                OS: Android 10 EMUI 10
                Cost: 600 BYN
                Vendor of CPU: HISILICON
                Weight is : 150 KG
                Has infrared port*/
        }
    }
}