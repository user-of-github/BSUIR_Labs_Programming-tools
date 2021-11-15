using System;
using System.Collections.Generic;
using _053506_Slutskiy_Lab9.Domain;
using System.Xml.Serialization;
using System.IO;
using System.Text.Json;
using System.Xml.Linq;
using System.Linq;

namespace Serializer
{
    public class Serializer : ISerializer
    {
        public void SerializeXML(IEnumerable<HeatedBuilding> xxx, string fileName)
        {
            XmlSerializer formatter = new(typeof(List<HeatedBuilding>));
            using (FileStream fs = new(fileName, FileMode.OpenOrCreate))
                formatter.Serialize(fs, xxx);
        }
        public IEnumerable<HeatedBuilding> DeSerializeByLINQ(string fileName)
        {
            XDocument xdoc = XDocument.Load(fileName);
            var items = from xe
                        in xdoc.Element("ArrayOfHeatedBuilding").Elements("HeatedBuilding")
                        select new HeatedBuilding(Convert.ToUInt16(xe.Element("PowerConsumption").Value));

            return items;
        }
        public IEnumerable<HeatedBuilding> DeSerializeXML(string fileName)
        {
            using FileStream fs = new(fileName, FileMode.OpenOrCreate);
            var read = (List<HeatedBuilding>)(new XmlSerializer(typeof(List<HeatedBuilding>))).Deserialize(fs);
            return read;
        }
        public IEnumerable<HeatedBuilding> DeSerializeJSON(string fileName)
        {
            using StreamReader sr = new(fileName);
            var json = sr.ReadToEnd();
            var restored = JsonSerializer.Deserialize<List<HeatedBuilding>>(json);
            return restored;
        }
        public void SerializeByLINQ(IEnumerable<HeatedBuilding> xxx, string fileName)
        {
            List<XElement> xElements = new();

            xxx.ToList().ForEach(
                item => xElements.Add(new XElement(
                    "HeatedBuilding",
                    new XElement("PowerConsumption", item.PowerConsumption)
                    ))
                );

            XDocument xDoc = new(new XElement("ArrayOfHeatedBuilding", xElements));

            xDoc.Save(fileName);
        }

        public void SerializeJSON(IEnumerable<HeatedBuilding> xxx, string fileName)
        {
            using (StreamWriter sw = new StreamWriter(fileName, false, System.Text.Encoding.Default))
                sw.WriteLine(JsonSerializer.Serialize<IEnumerable<HeatedBuilding>>(xxx));
        }
    }
}
