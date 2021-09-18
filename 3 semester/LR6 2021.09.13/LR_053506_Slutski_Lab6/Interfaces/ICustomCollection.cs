using System.Collections.Generic;

namespace LR_053506_Slutski_Lab6.Interfaces
{
    public interface ICustomCollection<TValueType> : IEnumerable<TValueType> where TValueType : class
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