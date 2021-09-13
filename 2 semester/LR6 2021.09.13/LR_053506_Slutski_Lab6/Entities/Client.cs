using System;
using LR_053506_Slutski_Lab6.Collections;
using LR_053506_Slutski_Lab6.Interfaces;


namespace LR_053506_Slutski_Lab6.Entities
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

        public ushort GetAllCallsCost()
        {
            ushort response = 0;
            _calls.Reset();
            var call = _calls.Current();
            while (call != null)
            {
                response += call.TotalCost;
                _calls.Next();
                call = _calls.Current();
            }

            _calls.Reset();
            return response;
        }

        public string GetInformation() =>
            $"{Surname}, calls: {CallsCount}, total spent: {GetAllCallsCost()}";
    }
}