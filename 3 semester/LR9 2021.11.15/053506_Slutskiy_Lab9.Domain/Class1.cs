using System;
using System.Collections;
using System.Collections.Generic;

namespace _053506_Slutskiy_Lab9.Domain
{
    public interface ISerializer
    {
        IEnumerable<HeatedBuilding> DeSerializeByLINQ(string fileName);
        IEnumerable<HeatedBuilding> DeSerializeXML(string fileName);
        IEnumerable<HeatedBuilding> DeSerializeJSON(string fileName);
        void SerializeByLINQ(IEnumerable<HeatedBuilding> xxx, string fileName);
        void SerializeXML(IEnumerable<HeatedBuilding> xxx, string fileName);
        void SerializeJSON(IEnumerable<HeatedBuilding> xxx, string fileName);
    }

    [Serializable]
    public class HeatedBuilding
    {
        public ushort PowerConsumption { get; set; }
        public HeatedBuilding(ushort a) => PowerConsumption = a;
        public HeatedBuilding() { }
    }
}



