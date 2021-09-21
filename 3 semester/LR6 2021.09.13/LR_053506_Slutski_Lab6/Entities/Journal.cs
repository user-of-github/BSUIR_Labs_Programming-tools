using System;
using LR_053506_Slutski_Lab6.Collections;

namespace LR_053506_Slutski_Lab6.Entities
{
    public class Journal
    {
        private class EventRecord
        {
            public string Name { get; set; }
            public string Description { get; set; }

            public EventRecord(string name, string description) =>
                (Name, Description) = (name.Trim(), description.Trim());
        }

        private CustomCollection<EventRecord> _events;


        public Journal() => _events = new CustomCollection<EventRecord>();

        public void AddEvent(string name, string description) =>
            _events.Add(new EventRecord(name, description));

        public void PrintRegisteredEvents()
        {
            Console.WriteLine("Currently logged events: ");
            foreach (var record in _events)
                Console.WriteLine($"\t{record.Description}" +
                              $": {record.Name}");
        }
    }
}