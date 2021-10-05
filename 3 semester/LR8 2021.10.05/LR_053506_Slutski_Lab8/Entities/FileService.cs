using System.Collections.Generic;
using System.IO;
using LR_053506_Slutski_Lab8.Interfaces;

namespace LR_053506_Slutski_Lab8.Entities
{
    public class FileService : IFileService
    {
        #region Read File

        public IEnumerable<Employee> ReadFile(string fileName)
        {
            using (BinaryReader reader = new(File.Open(fileName, FileMode.Open)))
                while (reader.PeekChar() > -1)
                {
                    var (name, salary, isRemoted) =
                        (reader.ReadString(), reader.ReadUInt16(), reader.ReadBoolean());
                    yield return new Employee(name, salary, isRemoted);
                }
        }

        #endregion


        #region Save Data

        public void SaveData(IEnumerable<Employee> data, string fileName)
        {
            using (BinaryWriter writer = new(File.Open(fileName, FileMode.Create)))
                foreach (var worker in data)
                {
                    writer.Write(worker.Name);
                    writer.Write(worker.Salary);
                    writer.Write(worker.Remote);
                }
        }

        #endregion
    }
}