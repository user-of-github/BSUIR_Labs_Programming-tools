using LR_053506_Slutski_Lab5.Collections;
using LR_053506_Slutski_Lab5.Interfaces;


namespace LR_053506_Slutski_Lab5.Entities
{
    public class Client : IClient
    {
        private readonly CustomCollection<SingleCall> _calls;

        public string Surname { get; private set; }

        public Client(string surname) =>
            (Surname, _calls) = (surname, new CustomCollection<SingleCall>());

        public void RegisterCall(SingleCall call) => _calls.Add(call);

        public ushort CallsCount => _calls.Count;

        public void Rename(string surname) =>
            Surname = surname.Trim() != "" ? surname.Trim() : Surname;
    }
}