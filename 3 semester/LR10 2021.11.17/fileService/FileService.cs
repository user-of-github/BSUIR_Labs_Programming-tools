using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;


namespace fileService
{
    public interface IFileService<ValueType> where ValueType : class
    {
        IEnumerable<ValueType> ReadFile(string fileName);

        void SaveData(IEnumerable<ValueType> data, string fileName);
    }

    public class FileService<ValueType> : IFileService<ValueType> where ValueType : class
    {
        public IEnumerable<ValueType> ReadFile(string fileName)
        {
            try
            {
                using StreamReader sr = new(fileName);
                var json = sr.ReadToEnd();
                var restored = JsonSerializer.Deserialize<List<ValueType>>(json);
                return restored;
            }
            catch (Exception ex)
            {
               Console.Error.WriteLine(ex.Message);
            }
            
            return new List<ValueType>();
        }

        public void SaveData(IEnumerable<ValueType> data, string fileName)
        {
            try
            {
                using StreamWriter sw = new(fileName, false, System.Text.Encoding.Default);
                sw.WriteLine(JsonSerializer.Serialize<IEnumerable<ValueType>>(data));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
        }
    }
}
