using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace StandardUnmanagedLibrary
{
    internal static class ProcessInfo
    {
        private static void PrintProcessInfo(Process process) => Console.WriteLine(
            $"Name: {process.ProcessName}; ID: {process.Id}; Taken memory: {process.WorkingSet64 / 1024 / 1024} MB");

        public static IEnumerable<Process> GetRunningProcesses() => Process.GetProcesses();

        public static void PrintListOfProcesses(IEnumerable<Process> list) => list.ToList().ForEach(PrintProcessInfo);

        public static void StartNewProcess()
        {
            var menuItems = new Dictionary<string, string>
            {
                ["BROWSER"] = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
                ["EXPLORER"] = "C:/Windows/explorer.exe",
                ["NOTEPAD"] = "C:/Windows/system32/notepad.exe"
            };
            Console.WriteLine("Type process to start: ");
            foreach (var pair in menuItems)
                Console.WriteLine(pair.Key);

            var chosenVariant = Console.ReadLine();

            while (chosenVariant.ToUpper() != "EXIT" && !menuItems.ContainsKey(chosenVariant.ToUpper()))
            {
                Console.WriteLine("No such file or command. Enter correctly or type exit");
                chosenVariant = Console.ReadLine();
            }

            if (chosenVariant.ToUpper() == "EXIT")
                return;

            Process.Start(menuItems[chosenVariant.ToUpper()]);
        }

        public static void ShowCurrentProcess() => PrintProcessInfo(Process.GetCurrentProcess());
    }

    internal static class AppMenu
    {
        private static readonly string[] MenuItems =
        {
            "Show Current Process",
            "Start new Process",
            "Show list of running processes",
            "Exit"
        };

        private static void PrintMenu()
        {
            Console.Clear();
            Console.WriteLine("Type number of menu-item\n");
            byte counter = 1;
            MenuItems.ToList().ForEach(item => Console.WriteLine($"{counter++}. {item}"));
        }

        public static void Launch()
        {
            while (true)
            {
                PrintMenu();
                var input = Console.ReadLine()?.Trim();
                byte variant;
                var success = byte.TryParse(input, out variant);

                if (!success)
                    variant = 123;

                Console.Clear();

                switch (variant)
                {
                    case 1:
                        ProcessInfo.ShowCurrentProcess();
                        break;
                    case 2:
                        ProcessInfo.StartNewProcess();
                        break;
                    case 3:
                        ProcessInfo.PrintListOfProcesses(ProcessInfo.GetRunningProcesses());
                        break;
                    case 4:
                        return;
                    default:
                        Console.WriteLine("Undefined");
                        break;
                }

                Console.WriteLine("\n\nPress any key");
                Console.ReadKey(true);
            }
        }
    }
}