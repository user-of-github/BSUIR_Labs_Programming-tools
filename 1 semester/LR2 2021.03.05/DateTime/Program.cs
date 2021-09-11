﻿using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

namespace DateTime
{ 
    static class Program
    {
        private static void Main()
        {
            Console.WriteLine("Enter your language. In case you enter english or some unknown language, program will launch in english");
            var requestedCulture = DetectCulture(Console.ReadLine());
            var response = GetMonthsInLanguage(ref requestedCulture);
            response.ForEach(Console.WriteLine);
        }

        private static CultureInfo DetectCulture(string language)
        {
            var format = "";
            language = language.ToLower();
            if (language.Contains("rus"))
                format = "ru-RU";
            else if (language.Contains("bel"))
                format = "be-BY";
            else if (language.Contains("french") || language.Contains("france"))
                format = "fr-FR";
            else if (language.Contains("span") || language.Contains("esp") || language.Contains("spain"))
                format = "es-ES";
            else if (language.Contains("germ"))
                format = "de-DE";
            else if (language.Contains("ital"))
                format = "it-IT";
            else
                format = "en-US";

            return new CultureInfo(format);
        }

        private static List<string> GetMonthsInLanguage(ref CultureInfo culture) =>
            culture.DateTimeFormat.MonthNames.ToList();
    }
}