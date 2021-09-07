using LR_053506_Slutski_Lab5.Entities;


namespace LR_053506_Slutski_Lab5.Interfaces
{
    public interface IClient
    {
        void RegisterCall(SingleCall call);

        void Rename(string surname);
    }
}