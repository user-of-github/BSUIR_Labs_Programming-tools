using System;
using System.Collections.Generic;

namespace LR_053506_Slutski_Lab8.Entities
{
    public class EmployeeComparer : IComparer<Employee>
    {
        public int Compare(Employee? x, Employee? y) =>
            string.Compare(x?.Name, y?.Name, StringComparison.InvariantCulture);
    }
}