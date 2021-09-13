using LR_053506_Slutski_Lab6.Entities;


namespace LR_053506_Slutski_Lab6.Interfaces
{
    public interface IClient
    {
        void RegisterCall(SingleCall call);

        void Rename(string surname);

        ushort GetAllCallsCost();
    }
}