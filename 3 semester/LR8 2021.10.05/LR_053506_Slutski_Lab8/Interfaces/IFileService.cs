using System.Collections.Generic;
using LR_053506_Slutski_Lab8.Entities;

namespace LR_053506_Slutski_Lab8.Interfaces
{
    public interface IFileService
    {
        IEnumerable<Employee> ReadFile(string fileName);
        void SaveData(IEnumerable<Employee> data, string fileName);
    }
}