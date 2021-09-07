namespace LR_053506_Slutski_Lab5.Interfaces
{
    public interface ICustomCollection<TValueType> where TValueType : class
    {
        TValueType this[ushort index] { get; set; }

        void Reset();

        void Next();

        TValueType Current();

        ushort Count { get; }

        void Add(TValueType item);

        void Remove(TValueType item);

        TValueType RemoveCurrent();
    }
}